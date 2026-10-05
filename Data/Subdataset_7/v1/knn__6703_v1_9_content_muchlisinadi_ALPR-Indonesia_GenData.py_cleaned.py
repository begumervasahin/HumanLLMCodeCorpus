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
    b1.add_argument("-d", "--image_train", b2 = "path for the images that you're going to train")
    b3 = vars(b1.parse_args())
    if b3.get("image_train", True):
        b4 = cv2.imread(b3["image_train"])
        if b4 is None:
            print("error: image not read from file \n\n")
            os.system("pause")
            return
    else:
        print("Please add -d or --image_train argument")
        return
    b5 = cv2.cvtColor(b4, cv2.COLOR_BGR2GRAY)
    b6 = cv2.GaussianBlur(b5, (5, 5), 0)
    b7 = cv2.adaptiveThreshold(b6, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow("b7", b7)
    b8 = b7.copy()
    imgContours, npaContours, b9 = cv2.findContours(b8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    b10 = np.empty((0, a2 * a3))
    b11 = []
    b12 = [ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9'),
                     ord('b20'), ord('b'), ord('c'), ord('d'), ord('e'), ord('f'), ord('g'), ord('h'), ord('a4'), ord('j'),
                     ord('k'), ord('l'), ord('m'), ord('n'), ord('o'), ord('p'), ord('q'), ord('r'), ord('s'), ord('t'),
                     ord('u'), ord('v'), ord('w'), ord('x'), ord('y'), ord('z')]
    for npaContour in npaContours:
        if cv2.contourArea(npaContour) > a1:
            [intX, intY, intW, intH] = cv2.boundingRect(npaContour)
            cv2.rectangle(b4, (intX, intY), (intX + intW, intY + intH), (0, 0, 255), 2)
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
    print("\n\ntraining complete !!\n")
    np.savetxt("classifications.txt", b18)
    np.savetxt("flattened_images.txt", b10)
    fonk2()
    cv2.destroyAllWindows()
def fonk2():
    b19 = np.loadtxt("classifications.txt")
    a4 = 0
    for b20 in b19:
        b20 = int(round(b20))
        if (b20 = = ord('b20')):
            b19[a4] = ord('A')
        if (b20 = = ord('b')):
            b19[a4] = ord('B')
        if (b20 = = ord('c')):
            b19[a4] = ord('C')
        if (b20 = = ord('d')):
            b19[a4] = ord('D')
        if (b20 = = ord('e')):
            b19[a4] = ord('E')
        if (b20 = = ord('f')):
            b19[a4] = ord('F')
        if (b20 = = ord('g')):
            b19[a4] = ord('G')
        if (b20 = = ord('h')):
            b19[a4] = ord('H')
        if (b20 = = ord('a4')):
            b19[a4] = ord('I')
        if (b20 = = ord('j')):
            b19[a4] = ord('J')
        if (b20 = = ord('k')):
            b19[a4] = ord('K')
        if (b20 = = ord('l')):
            b19[a4] = ord('L')
        if (b20 = = ord('m')):
            b19[a4] = ord('M')
        if (b20 = = ord('n')):
            b19[a4] = ord('N')
        if (b20 = = ord('o')):
            b19[a4] = ord('O')
        if (b20 = = ord('p')):
            b19[a4] = ord('P')
        if (b20 = = ord('q')):
            b19[a4] = ord('Q')
        if (b20 = = ord('r')):
            b19[a4] = ord('R')
        if (b20 = = ord('s')):
            b19[a4] = ord('S')
        if (b20 = = ord('t')):
            b19[a4] = ord('T')
        if (b20 = = ord('u')):
            b19[a4] = ord('U')
        if (b20 = = ord('v')):
            b19[a4] = ord('V')
        if (b20 = = ord('w')):
            b19[a4] = ord('W')
        if (b20 = = ord('x')):
            b19[a4] = ord('X')
        if (b20 = = ord('y')):
            b19[a4] = ord('Y')
        if (b20 = = ord('z')):
            b19[a4] = ord('Z')
        a4 = a4 + 1
    b21 = np.array(b19, np.float32)
    b18 = b21.reshape((b21.size, 1))
    np.savetxt("classifications.txt", b18)
if b22 = = "__main__":
    fonk1()