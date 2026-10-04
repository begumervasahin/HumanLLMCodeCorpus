import argparse
import os
import sys
import cv2
import numpy as np
a1 = 100
a2 = 20
a3 = 30
def fonk1():
    b1 = argparse.ArgumentParser()
    b1.add_argument("-d", "--image_train", b2 = True, help="Path for the images that you're going to train")
    b3 = b1.parse_args()
    b4 = cv2.imread(b3.image_train)
    if b4 is None:
        print("Error: Image not read from file\n")
        sys.exit()
    b5 = fonk2(b4)
    cv2.imshow("Threshold Image", b5)
    b11, b6 = fonk3(b5, b4)
    print("\nTraining complete!\n")
    np.savetxt("b6.txt", b6)
    np.savetxt("b11.txt", b11)
    fonk4()
    cv2.destroyAllWindows()
def fonk2(img):
    b7 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b8 = cv2.GaussianBlur(b7, (5, 5), 0)
    b5 = cv2.adaptiveThreshold(
        b8, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    return b5
def fonk3(b5, b4):
    b9 = b5.copy()
    contours, b10 = cv2.findContours(
        b9, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    b11 = np.empty((0, a2 * a3))
    b6 = []
    b12 = [ord(char) for char in '0123456789abcdefghijklmnopqrstuvwxyz']
    for contour in contours:
        if cv2.contourArea(contour) > a1:
            x, y, w, b13 = cv2.boundingRect(contour)
            cv2.rectangle(b4, (x, y), (x + w, y + b13), (0, 0, 255), 2)
            b14 = b5[y:y + b13, x:x + w]
            b15 = cv2.resize(b14, (a2, a3))
            cv2.imshow("ROI", b14)
            cv2.imshow("Resized ROI", b15)
            cv2.imshow("Training Numbers", b4)
            b16 = cv2.waitKey(0)
            if b16 = = 27:
                sys.exit()
            elif b16 in b12:
                b6.append(b16)
                b17 = b15.reshape((1, a2 * a3))
                b11 = np.append(b11, b17, axis=0)
    b6 = np.array(b6, np.float32).reshape((-1, 1))
    return b11, b6
def fonk4():
    b18 = np.loadtxt("b6.txt", dtype=np.float32)
    b19 = [(val - 32 if ord('a') <= val <= ord('z') else val) for val in b18]
    b20 = np.array(b19, np.float32).reshape((-1, 1))
    np.savetxt("b6.txt", b20)
if b21 = = "__main__":
    fonk1()