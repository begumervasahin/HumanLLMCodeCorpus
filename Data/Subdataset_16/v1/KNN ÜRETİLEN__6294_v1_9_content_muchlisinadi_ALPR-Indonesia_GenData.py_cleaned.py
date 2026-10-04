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
    b1.add_argument("-d", "--image_train", b2 = True, help="path for the images that you're going to train")
    b3 = vars(b1.parse_args())
    b4 = cv2.imread(b3["image_train"])
    if b4 is None:
        print("Error: Image not read from file\n\n")
        os.system("pause")
        return
    b5 = cv2.cvtColor(b4, cv2.COLOR_BGR2GRAY)
    b6 = cv2.GaussianBlur(b5, (5, 5), 0)
    b7 = cv2.adaptiveThreshold(b6,
                                      255,
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY_INV,
                                      11,
                                      2)
    cv2.imshow("b7", b7)
    b8 = b7.copy()
    npaContours, b9 = cv2.findContours(b8,
                                                 cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_SIMPLE)
    b10 = np.empty((0, a2 * a3))
    b11 = []
    b12 = [ord(ch) for ch in '0123456789abcdefghijklmnopqrstuvwxyz']
    for npaContour in npaContours:
        if cv2.contourArea(npaContour) > a1:
            [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
            cv2.rectangle(b4,
                          (intX, intY),
                          (intX + intW, intY + intH),
                          (0, 0, 255),
                          2)
            b13 = b7[intY:intY + intH, intX:intX + intW]
            b14 = cv2.resize(b13, (a2, a3))
            cv2.imshow("b13", b13)
            cv2.imshow("b14", b14)
            cv2.imshow("training_numbers.png", b4)
            b15 = cv2.waitKey(0)
            if b15 = = 27:
                sys.exit()
            elif b15 in b12:
                b11.append(b15)
                b16 = b14.reshape((1, a2 * a3))
                b10 = np.append(b10, b16, 0)
    b17 = np.array(b11, np.float32)
    b18 = b17.reshape((b17.size, 1))
    print("\n\nTraining complete!\n")
    np.savetxt("classifications.txt", b18)
    np.savetxt("flattened_images.txt", b10)
    fonk2()
    cv2.destroyAllWindows()
def fonk2():
    b19 = np.loadtxt("classifications.txt")
    a4 = 0
    for b20 in b19:
        b20 = int(round(b20))
        if b20 >= ord('b20') and b20 <= ord('z'):
            b19[a4] = ord(chr(b20).upper())
        a4 += 1
    b21 = np.array(b19, np.float32)
    b18 = b21.reshape((b21.size, 1))
    np.savetxt("classifications.txt", b18)
if b22 = = "__main__":
    fonk1()