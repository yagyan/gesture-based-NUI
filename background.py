import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
while True:
    ret, img = cap.read()
    if img is None:
        break
    blur = cv.GaussianBlur(img, (3, 3), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_RGB2HSV)

    lower_color = np.array([108, 23, 82])
    upper_color = np.array([179, 255, 255])

    mask = cv.inRange(hsv, lower_color, upper_color)
    blur = cv.medianBlur(mask, 5)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (8, 8))
    hsv_d = cv.dilate(blur, kernel)
    ret, thresh = cv.threshold(hsv_d, 0, 255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2:]
    contours = max(contours, key=lambda x: cv.contourArea(x))
    cv.drawContours(img, [contours], -1, (255, 255, 0), 2)
    cv.imshow("contours", img)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyWindow()