import cv2
import numpy as np
def fonk1(count):
    b1 = []
    b2 = cv2.imread("words.png")
    if b2 is None:
        print("Error: image not read from file")
        return
    height, width, b3 = b2.shape
    print("Height:", height)
    print("Width:", width)
    b4 = width / height
    print("Ratio:", b4)
    if b4 >= 0.9:
        a1 = 9999
        a2 = -999
        b5 = np.zeros(100, dtype=int)
        for i in range(height
            for j in range(width):
                if np.any(b2[i, j] == 0):
                    b5[i] += 1
            if b5[i] < a1:
                a1 = b5[i]
                a2 = i
            elif b5[i] - a1 <= width / 3:
                b6 = i
        if b6 > a2:
            b7 = b6
        else:
            b7 = a2
        for i in range(a2 - 2, b7 + 2):
            for j in range(width):
                b2[i, j] = 1
    b8 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    b9 = cv2.adaptiveThreshold(b8, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 111, 2)
    b1.append(b9)
    b10 = f"CreS2
    cv2.imwrite(b10, b1[count - 1])
    cv2.imwrite("wordseg.png", b1[count - 1])
    cv2.imshow("shown", b9)
    cv2.waitKey(0)
    return b9
fonk1(1)
