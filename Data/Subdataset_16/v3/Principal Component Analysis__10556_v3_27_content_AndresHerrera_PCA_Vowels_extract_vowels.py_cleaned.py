import os
import cv2
import numpy as np
WIDTH, b1 = 20, 20
a1 = 100
def fonk1(b12):
    b2 = cv2.imread(b12)
    if b2 is None:
        raise FileNotFoundError(f"Error: Image '{b12}' not a2 or unable to read image.")
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
    return b5, b2
def fonk2(b5, b2):
    b6 = b5.copy()
    contours, b7 = cv2.findContours(
        b6,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    a2 = 0
    for contour in contours:
        if cv2.contourArea(contour) > a1:
            x, y, w, b8 = cv2.boundingRect(contour)
            cv2.rectangle(b2, (x, y), (x + w, y + b8), (0, 0, 255), 2)
            b9 = b5[y:y + b8, x:x + w]
            b10 = cv2.resize(b9, (WIDTH, b1))
            cv2.imshow("Original File", b2)
            a2 += 1
            os.makedirs('vowels', b11 = True)
            cv2.imwrite(f'vowels/vowel_{a2}.png', cv2.bitwise_not(b10))
    return a2
def fonk3():
    b12 = "raw_vowels.jpg"
    try:
        b5, b2 = fonk1(b12)
        cv2.imshow("Threshold Image", b5)
        b13 = fonk2(b5, b2)
        print(f"{b13} files written into (vowels) folder!")
        print("Notice: You have to arrange (vowels) files into (training) folder tree!")
        print("in folder :  training/A  <-  store only A images")
        print("in folder :  training/E  <-  store only E images")
        print("in folder :  training/I  <-  store only I images")
        print("in folder :  training/O  <-  store only O images")
        print("in folder :  training/U  <-  store only U images")
        cv2.waitKey(0)
    except FileNotFoundError as e:
        print(e)
    finally:
        cv2.destroyAllWindows()
if b14 = = "__main__":
    fonk3()