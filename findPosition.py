import cv2


def findPosition(results, img, handNo=0, draw=True):
    xlist = []
    ylist = []
    bbox = []
    label = ''
    lmlist = []
    if results.multi_hand_landmarks:
        myhand = results.multi_hand_landmarks[handNo]
        for ids, lm in enumerate(myhand.landmark):
            # print(ids, lm)
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            xlist.append(cx)
            ylist.append(cy)
            # print(ids, cx, cy)
            label = results.multi_handedness[0].classification[0].label
            lmlist.append([ids, cx, cy, label])
            # if draw:
            #     cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        xmin, xmax = min(xlist), max(xlist)
        ymin, ymax = min(ylist), max(ylist)
        bbox = xmin, ymin, xmax, ymax

        if draw:
            cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                          (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)

    return lmlist, bbox, label
