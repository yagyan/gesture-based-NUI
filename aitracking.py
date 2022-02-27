import sys

import cv2
import numpy as np
import pyautogui

import HandTrackingModule as htm
import autopy
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import findDistance as FD
import time
from pynput.keyboard import Key, Controller
import guiv1

keyboard = Controller()
##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=2)
wScr, hScr = autopy.screen.size()
# print(wScr, hScr)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (255, 0, 0)
dominant = guiv1.dominant
left = guiv1.left
right = guiv1.right
Evol = guiv1.volume
Ebri = guiv1.brightness
cancel = guiv1.cancel
movement= guiv1.movement
value = 1
flag = "00"
f= 0
if dominant == 'Right':
    value = 1
if dominant == 'Left':
    value = 0

if cancel:
    sys.exit()
while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img, draw=True)
    lmList, bbox, label = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers

    print(label)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:3]
        x2, y2 = lmList[12][1:3]
        # print(x1, y1, x2, y2)
        if flag == "00" or flag == "01":
            cv2.putText(img, "int= Off", (450, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        if flag == "11":
            cv2.putText(img, "int= On", (450, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        # cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),(255, 0, 255), 2)

        if flag == "00" and label == dominant and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[
            4] == 0 and \
                fingers[0] == value:
            flag = "01"

        if flag == "01" and label == dominant and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[
            4] == 1 and fingers[0] != value:
            flag = "11"
        print(flag)
        if flag == "11":
            # 4. Only Index Finger : Moving Mode
            if movement== 'Enable' and label == dominant and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and \
                    fingers[0] == value:
                # 5. Convert Coordinates
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                # 6. Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                # 7. Move Mouse
                f = 0
                autopy.mouse.move(clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

            # 5. Both Index and middle fingers are up : left Clicking Mode
            if left == "Enable" and label == dominant and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0 and \
                    fingers[0] == value:
                # 9. Find distance between fingers

                length, img, lineInfo = FD.findDistance(lmList, 8, 12, img)
                # print(length)
                # 10. Click mouse if distance short
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]),
                               15, (0, 255, 0), cv2.FILLED)
                    pyautogui.click(button='left')

            #right click gesture
            if right == 'Enable' and label == dominant and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and \
                    fingers[0] != value and f == 0:
                pyautogui.click(button='right')
                f = 1
            #volume gesture
            if Evol == "Enable" and label != dominant and fingers[0] == value and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and \
                    fingers[4] == 0:
                # Filter based on size
                area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
                # print(area)
                if 250 < area < 1000:
                    # Find Distance between index and Thumb
                    length, img, lineInfo = FD.findDistance(lmList, 4, 8, img)
                    # print(length)

                    # Convert Volume
                    volBar = np.interp(length, [50, 200], [400, 150])
                    volPer = np.interp(length, [50, 200], [0, 100])

                    # Reduce Resolution to make it smoother
                    smoothness = 10
                    volPer = smoothness * round(volPer / smoothness)
                    volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    colorVol = (0, 255, 0)
                    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
                    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

            if Ebri == "Enable" and label != dominant and fingers[0] == value and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and \
                    fingers[4] == 0:
                # Filter based on size
                area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
                # print(area)
                if 250 < area < 1000:
                    length1, img, lineInfo = FD.findDistance(lmList, 4, 8, img)
                    bBar = np.interp(length1, [50, 200], [400, 150])
                    bPer = np.interp(length1, [50, 200], [0, 100])
                    # Reduce Resolution to make it smoother
                    smoothness = 10
                    bPer = smoothness * round(bPer / smoothness)
                    sbc.set_brightness(bPer)
                    cv2.rectangle(img, (50, int(bBar)), (85, 400), (255, 0, 0), cv2.FILLED)
                    cv2.putText(img, f'{int(bPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)


    # cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)

    # cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
    # cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,
    #             1, colorVol, 3)

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # 12. Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
