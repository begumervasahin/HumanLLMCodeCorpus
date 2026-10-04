import numpy as np
import cv2
import sys
import argparse
def fonk1(inImg):
    h, b1 = inImg.shape[0], inImg.shape[1]
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    if b1 >= h:
        a3 = b1
        b2 = inImg[0:h, 0:a3]
        b3 = inImg[0:h, a3:b1]
    else:
        a4 = h
        b2 = inImg[0:a4, 0:b1]
        b3 = inImg[a4:h, 0:b1]
    return a1, a2, b2, a3, a4, b3
class class1:
    def fonk2(self, inImg, minStd, minSize, offX, offY):
        h, b1 = inImg.shape[0], inImg.shape[1]
        m, b4 = cv2.meanStdDev(inImg)
        if b4 >= minStd and max(h, b1) > minSize:
            oX1, oY1, im1, oX2, oY2, b5 = fonk1(inImg)
            self.fonk2(im1, minStd, minSize, offX + oX1, offY + oY1)
            self.fonk2(b5, minStd, minSize, offX + oX2, offY + oY2)
        else:
            self.b6.append([offX, offY, b1, h, m, b4])
    def fonk3(self, b14, stdmin, sizemin):
        self.b6 = []
        self.fonk2(b14, stdmin, sizemin, 0, 0)
a5 = 0
a6 = 0
def fonk4(inImg, minStd, minSize, offX, offY, roiList):
    h, b1 = inImg.shape[0], inImg.shape[1]
    m, b4 = cv2.meanStdDev(inImg)
    if b4 >= minStd and max(h, b1) > minSize:
        oX1, oY1, im1, oX2, oY2, b5 = fonk1(inImg)
        fonk4(im1, minStd, minSize, offX + oX1, offY + oY1, roiList)
        fonk4(b5, minStd, minSize, offX + oX2, offY + oY2, roiList)
    else:
        roiList.append([offX, offY, b1, h, m, b4])
def fonk5():
    b7 = argparse.ArgumentParser(description='Compute best bars cuts')
    b7.add_argument('-b14', b8 = '', type=str, help='image to load')
    b7.add_argument('-sz', b8 = '', type=int, help='quadtree min size')
    b7.add_argument('-std', b8 = '', type=float, help='standard deviation to split')
    b9 = b7.parse_args()
    b10 = b9.b14
    b11 = b9.sz
    b12 = b9.std
    b13 = cv2.imread(b10)
    if b13 is not None:
        if b13.ndim > 1:
            b14 = cv2.cvtColor(b13, cv2.COLOR_BGR2GRAY)
        else:
            b14 = b13
    else:
        print(f'Error on input image: {b10}')
        exit()
    print('execution...')
    cv2.imshow('Start Image', b14)
    b15 = class1(b14, b12, b11)
    b16 = b15.b6
    b17 = b14.copy()
    for e in b16:
        a7 = 255
        if e[5] < b12:
            a7 = 0
        cv2.rectangle(b17, (e[0], e[1]), (e[0] + e[2], e[1] + e[3]), a7, 1)
    cv2.imshow('Quad Image', b17)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b18 = = '__main__':
    fonk5()