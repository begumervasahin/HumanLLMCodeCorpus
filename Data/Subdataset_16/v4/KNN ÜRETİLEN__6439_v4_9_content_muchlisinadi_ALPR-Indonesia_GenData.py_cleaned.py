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
        print("Error: Image not read from file\n\n")
        sys.exit()
    b5 = cv2.cvtColor(b4, cv2.COLOR_BGR2GRAY)
    b6 = cv2.GaussianBlur(b5, (5, 5), 0)
    b7 = cv2.adaptiveThreshold(b6, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow("Threshold Image", b7)
    b8 = b7.copy()
    contours, b9 = cv2.findContours(b8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    b10 = np.empty((0, a2 * a3))
    b11 = []
    b12 = [ord(char) for char in '0123456789abcdefghijklmnopqrstuvwxyz']
    for contour in contours:
        if cv2.contourArea(contour) > a1:
            x, y, w, b13 = cv2.boundingRect(contour)
            cv2.rectangle(b4, (x, y), (x + w, y + b13), (0, 0, 255), 2)
            b14 = b7[y:y + b13, x:x + w]
            b15 = cv2.resize(b14, (a2, a3))
            cv2.imshow("ROI", b14)
            cv2.imshow("Resized ROI", b15)
            cv2.imshow("Training Numbers", b4)
            b16 = cv2.waitKey(0)
            if b16 = = 27:
                sys.exit()
            elif b16 in b12:
                b11.append(b16)
                b17 = b15.reshape((1, a2 * a3))
                b10 = np.append(b10, b17, axis=0)
    b11 = np.array(b11, np.float32).reshape((-1, 1))
    print("\nTraining complete!\n")
    np.savetxt("b11.txt", b11)
    np.savetxt("b10.txt", b10)
    fonk2()
    cv2.destroyAllWindows()
def fonk2():
    b18 = np.loadtxt("b11.txt", dtype=np.float32)
    b19 = []
    for b20 in b18:
        b20 = int(round(b20))
        if ord('a') <= b20 <= ord('z'):
            b19.append(b20 - 32)
        else:
            b19.append(b20)
    b21 = np.array(b19, np.float32).reshape((-1, 1))
    np.savetxt("b11.txt", b21)
if b22 = = "__main__":
    fonk1()