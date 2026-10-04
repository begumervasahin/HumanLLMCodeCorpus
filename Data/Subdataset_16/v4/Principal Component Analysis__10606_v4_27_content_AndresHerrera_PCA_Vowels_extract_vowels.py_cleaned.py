import os
import cv2
import numpy as np
a1 = 20
a2 = 20
a3 = 100
def fonk1():
    b1 = cv2.imread("raw_vowels.jpg")
    b2 = cv2.cvtColor(b1, cv2.COLOR_BGR2GRAY)
    b3 = cv2.GaussianBlur(b2, (5, 5), 0)
    b4 = cv2.adaptiveThreshold(b3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow("Threshold Image", b4)
    b5 = b4.copy()
    contours, b6 = cv2.findContours(b5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    a4 = 0
    for contour in contours:
        if cv2.contourArea(contour) > a3:
            intX, intY, intW, b7 = cv2.boundingRect(contour)
            cv2.rectangle(b1, (intX, intY), (intX + intW, intY + b7), (0, 0, 255), 2)
            b8 = b4[intY:intY + b7, intX:intX + intW]
            b9 = cv2.resize(b8, (a1, a2))
            cv2.imshow("Original File", b1)
            a4 += 1
            cv2.imwrite(f'vowels/vowel_{a4}.png', cv2.bitwise_not(b9))
    print(f"{a4} files written into (vowels) folder!")
    print("Notice: You have to arrange (vowels) files into (training) folder tree!")
    print("in folder :  training/A  <-  store only A images")
    print("in folder :  training/E  <-  store only E images")
    print("in folder :  training/I  <-  store only I images")
    print("in folder :  training/O  <-  store only O images")
    print("in folder :  training/U  <-  store only U images")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b10 = = "__main__":
    fonk1()