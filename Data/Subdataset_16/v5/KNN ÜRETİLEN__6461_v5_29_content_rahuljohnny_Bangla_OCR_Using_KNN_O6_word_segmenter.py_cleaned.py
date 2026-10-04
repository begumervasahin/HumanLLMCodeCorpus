import os
import array
import numpy as np
import cv2
b1 = []
def fonk1(b12):
    b2 = "words.png"
    b3 = cv2.imread(b2)
    if b3 is None:
        print("Error: image not read from file")
        os.system("pause")
        return
    height, width, b4 = b3.shape
    print(f"Height: {height}")
    print(f"Width: {width}")
    b5 = float(width) / float(height)
    print(f"Ratio: {b5}")
    if b5 >= 0.9:
        a1 = 9999
        a2 = -999
        b6 = array.array('i', (0,) * 100)
        a3 = -1
        a4 = -1
        for i in range(0, height
            for j in range(width):
                if np.any(b3[i, j] == 0):
                    b6[i] += 1
            if b6[i] < a1:
                a1 = b6[i]
                a3 = i
            elif b6[i] - a1 <= width
                a4 = i
        b7 = max(a3, a4)
        for i in range(a3 - 2, b7 + 2):
            for j in range(width):
                b3[i, j] = 1
    b8 = cv2.cvtColor(b3, cv2.COLOR_BGR2GRAY)
    b9 = cv2.adaptiveThreshold(
        b8,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        111,
        2
    )
    b1.append(b9)
    fonk2(b12, b1[b12 - 1])
    cv2.imwrite("wordseg.png", b1[b12])
    cv2.imshow("Segmented Image", b9)
    cv2.waitKey(0)
    return b9
def fonk2(b12, image):
    b10 = f"CreS2/c{b12 - 1}.png" if b12 > 0 else "CreS2/c-1.png"
    cv2.imwrite(b10, image)
if b11 = = "__main__":
    b12 = int(input("Enter b12: "))
    fonk1(b12)