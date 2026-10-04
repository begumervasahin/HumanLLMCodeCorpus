import cv2
import os
import numpy as np
import array
b1 = []
def fonk1(a3):
    b2 = cv2.imread("words.png")
    if b2 is None:
        print("error: image not read from file \n\n")
        os.system("pause")
        return
    height, width, b3 = b2.shape
    print("Height:")
    print(height)
    print("Width:")
    print(width)
    b4 = float(width) / float(height)
    print("Ratio:")
    print(b4)
    if b4 >= 0.9:
        a1 = 9999
        a2 = -999
        b5 = array.array('i', (0,) * 100)
        for i in range(0, int(height)
            for j in range(0, width):
                if np.any(b2[i, j] == 0):
                    b5[i] += 1
            if b5[i] < a1:
                a1 = b5[i]
                b6 = i
            elif b5[i] - a1 <= int(width / 3):
                a2 = i
        if a2 > b6:
            b7 = a2
        else:
            b7 = b6
        for i in range(b6 - 2, b7 + 2):
            for j in range(0, width):
                b2[i, j] = 1
    b8 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    b9 = cv2.adaptiveThreshold(b8, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 111, 2)
    b1.append(b9)
    b10 = f"CreS2
    cv2.imwrite(b10, b1[a3 - 1])
    cv2.imwrite("wordseg.png", b1[a3])
    cv2.imshow("shown", b9)
    cv2.waitKey(0)
    return b9
if b11 = = "__main__":
    a3 = 1
    fonk1(a3)