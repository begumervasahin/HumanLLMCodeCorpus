import argparse
import os
import sys
import cv2
import numpy as np
a1 = 100
a2 = 20
a3 = 30
def fonk1():
    b1 = fonk2()
    if b1.image_train:
        b2 = fonk3(b1.image_train)
        if b2 is None:
            print("Error: Failed to read the image from file")
            return
    else:
        print("Please provide the path to the training image using the '-d' or '--image_train' argument.")
        return
    b3 = fonk4(b2)
    fonk5(b3)
    fonk6()
    fonk7()
    cv2.destroyAllWindows()
def fonk2():
    b4 = argparse.ArgumentParser()
    b4.add_argument("-d", "--image_train", b5 = "Path to the training image")
    return b4.parse_args()
def fonk3(image_path):
    b6 = cv2.imread(image_path)
    return b6
def fonk4(b6):
    b7 = cv2.cvtColor(b6, cv2.COLOR_BGR2GRAY)
    b8 = cv2.GaussianBlur(b7, (5, 5), 0)
    b3 = cv2.adaptiveThreshold(b8, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow("imgThresh", b3)
    return b3
def fonk5(b3):
    b9, contours, b9 = cv2.findContours(b3.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    b10 = np.empty((0, a2 * a3))
    b11 = []
    for contour in contours:
        if cv2.contourArea(contour) > a1:
            x, y, w, b12 = cv2.boundingRect(contour)
            cv2.rectangle(b2, (x, y), (x + w, y + b12), (0, 0, 255), 2)
            b13 = b3[y:y + b12, x:x + w]
            b14 = cv2.resize(b13, (a2, a3))
            cv2.imshow("imgROI", b13)
            cv2.imshow("imgROIResized", b14)
            cv2.imshow("training_numbers.png", b2)
            b15 = cv2.waitKey(0)
            if b15 = = 27:
                sys.exit()
            elif 48 <= b15 <= 122:
                b11.append(b15)
                b16 = b14.reshape((1, a2 * a3))
                b10 = np.append(b10, b16, 0)
    return b11, b10
def fonk6():
    np.savetxt("b11.txt", b11)
    np.savetxt("b10.txt", b10)
    print("\nTraining complete!!\n")
def fonk7():
    b17 = np.loadtxt("b11.txt")
    b17 = np.where((b17 >= 97) & (b17 <= 122), b17 - 32, b17)
    np.savetxt("b11.txt", b17)
if b18 = = "__main__":
    fonk1()