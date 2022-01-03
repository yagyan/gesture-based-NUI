def fingersUp(lmList, tipIds):
    fingers = []
    # Thumb
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)
    # 4 Fingers
    for ids in range(1, 5):
        if lmList[tipIds[ids]][2] < lmList[tipIds[ids] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers
