import os
import cv2
import numpy as np
a1 = 20
a2 = 20
a3 = 100
def fonk1(b9, b10):
    b1 = cv2.imread(b9)
    b2 = cv2.cvtColor(b1, cv2.COLOR_BGR2GRAY)
    b3 = cv2.GaussianBlur(b2, (5, 5), 0)
    b4 = cv2.adaptiveThreshold(b3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow("Threshold Image", b4)
    contours, b5 = cv2.findContours(b4.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    a4 = 0
    for contour in contours:
        if cv2.contourArea(contour) > a3:
            x, y, w, b6 = cv2.boundingRect(contour)
            cv2.rectangle(b1, (x, y), (x + w, y + b6), (0, 0, 255), 2)
            b7 = b4[y:y + b6, x:x + w]
            b8 = cv2.resize(b7, (a1, a2))
            cv2.imshow("Processed Image", b1)
            a4 += 1
            cv2.imwrite(f'{b10}/vowel_{a4}.png', cv2.bitwise_not(b8))
    return a4
def fonk2():
    b9 = "raw_vowels.jpg"
    b10 = "vowels"
    os.makedirs(b10, b11 = True)
    a4 = fonk1(b9, b10)
    print(f"{a4} files written into '{b10}' folder!")
    print("Notice: You have to arrange the files into the 'training' folder tree:")
    print(" - training/A  <-  store only A images")
    print(" - training/E  <-  store only E images")
    print(" - training/I  <-  store only I images")
    print(" - training/O  <-  store only O images")
    print(" - training/U  <-  store only U images")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b12 = = "__main__":
    fonk2()