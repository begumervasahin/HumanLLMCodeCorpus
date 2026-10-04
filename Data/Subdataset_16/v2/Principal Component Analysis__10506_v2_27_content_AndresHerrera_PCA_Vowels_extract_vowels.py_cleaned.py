import os
import cv2
import numpy as np
w, b1 = 20, 20
a1 = 100
def fonk1(b11):
    b2 = cv2.imread(b11)
    if b2 is None:
        print("Error: Image not a2 or unable to read image.")
        return 0
    b3 = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    b4 = cv2.GaussianBlur(b3, (5, 5), 0)
    b5 = cv2.adaptiveThreshold(
        b4,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
    )
    cv2.imshow("Threshold Image", b5)
    b6 = b5.copy()
    contours, b7 = cv2.findContours(
        b6,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    a2 = 0
    for contour in contours:
        if cv2.contourArea(contour) > a1:
            x, y, w, b1 = cv2.boundingRect(contour)
            cv2.rectangle(b2, (x, y), (x + w, y + b1), (0, 0, 255), 2)
            b8 = b5[y:y + b1, x:x + w]
            b9 = cv2.resize(b8, (w, b1))
            cv2.imshow("Original File", b2)
            a2 += 1
            os.makedirs('vowels', b10 = True)
            cv2.imwrite(f'vowels/vowel_{a2}.png', cv2.bitwise_not(b9))
    return a2
def fonk2():
    b11 = "raw_vowels.jpg"
    b12 = fonk1(b11)
    print(f"{b12} files written into (vowels) folder!")
    print("Notice: You have to arrange (vowels) files into (training) folder tree!")
    print("in folder :  training/A  <-  store only A images")
    print("in folder :  training/E  <-  store only E images")
    print("in folder :  training/I  <-  store only I images")
    print("in folder :  training/O  <-  store only O images")
    print("in folder :  training/U  <-  store only U images")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b13 = = "__main__":
    fonk2()