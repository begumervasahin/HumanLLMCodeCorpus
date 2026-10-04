import cv2
import os
import numpy as np
import array
b1 = []
def fonk1(a3):
    b2 = "words.png"
    b3 = cv2.imread(b2)
    if b3 is None:
        print("Error: Image not read from file\n\n")
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
        for i in range(height
            for j in range(width):
                if np.any(b3[i, j] == 0):
                    b6[i] += 1
            if b6[i] < a1:
                a1 = b6[i]
                a2 = i
            elif b6[i] - a1 <= int(width / 3):
                b7 = i
        b8 = max(b7, a2)
        for i in range(a2 - 2, b8 + 2):
            for j in range(width):
                b3[i, j] = 255
    b9 = cv2.cvtColor(b3, cv2.COLOR_BGR2GRAY)
    b10 = cv2.adaptiveThreshold(b9, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 111, 2)
    b1.append(b10)
    b11 = f"CreS2/c{a3 - 1}.png" if a3 != 0 else "CreS2/c-1.png"
    os.makedirs(os.path.dirname(b11), b12 = True)
    cv2.imwrite(b11, b1[a3 - 1])
    cv2.imwrite("wordseg.png", b1[a3])
    cv2.imshow("Segmented Word", b10)
    cv2.waitKey(0)
    return b10
if b13 = = "__main__":
    a3 = 1
    fonk1(a3)