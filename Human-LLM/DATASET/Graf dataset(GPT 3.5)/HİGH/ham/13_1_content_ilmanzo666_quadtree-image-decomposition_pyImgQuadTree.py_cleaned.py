import numpy as np
import cv2
import sys
import argparse
def fonk1(inImg):
    h,b1 = inImg.shape[0], inImg.shape[1]
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    if b1 >= h:
        a1 = 0
        a3 = b1/2
        b2 = inImg[0:h, 0:a3]
        b3 = inImg[0:h, a3:b1]
    else:
        a2 = 0
        a4 = h/2
        b2 = inImg[0:a4, 0:b1]
        b3 = inImg[a4:h, 0:b1]
    return a1,a2,b2, a3,a4,b3
class class1:
    def fonk2(self, inImg, minStd, minSize, offX, offY):
        h,b1 = inImg.shape[0], inImg.shape[1]
        m,b4 = cv2.meanStdDev(inImg)
        if b4>=minStd and max(h,b1)>minSize:
            oX1,oY1,im1, oX2,oY2,b5 = fonk1(inImg)
            self.fonk2(im1, minStd, minSize, offX+oX1, offY+oY1)
            self.fonk2(b5, minStd, minSize, offX+oX2, offY+oY2)
        else:
            self.b6.append([offX,offY,b1,h,m,b4])
    def fonk3(self, b16, stdmin, sizemin):
        self.b6 = []
        self.fonk2(b16, stdmin, sizemin, 0, 0)
a5 = 0
a6 = 0
def fonk4(inImg, minStd, minSize, offX, offY, roiList):
    h,b1 = inImg.shape[0], inImg.shape[1]
    m,b4 = cv2.meanStdDev(inImg)
    if b4>=minStd and max(h,b1)>minSize:
        oX1,oY1,im1, oX2,oY2,b5 = fonk1(inImg)
        fonk4(im1, minStd, minSize,offX+oX1,offY+oY1, roiList)
        fonk4(b5, minStd, minSize,offX+oX2,offY+oY2, roiList)
    else:
        roiList.append([offX,offY,b1,h,m,b4])
def fonk5(file_):
    b7 = argparse.ArgumentParser(description='Compute best bars cuts')
    b7.add_argument('-b16',
                        b8 = '',
                        b9 = str,
                        b10 = 'image to load')
    b7.add_argument('-sz',
                        b8 = '',
                        b9 = int,
                        b10 = 'quadtree min size')
    b7.add_argument('-std',
                        b8 = '',
                        b9 = float,
                        b10 = 'standard deviation to split')
    b11 = b7.parse_args()
    b12 = b11.b16
    b13 = b11.sz
    b14 = b11.std
    b15 = cv2.imread(b12)
    if not b9(b15)==b9(None):
        if b15.ndim > 1 :
            b16 = cv2.cvtColor(b15, cv2.COLOR_BGR2GRAY)
        else :
            b16 = b15
    else :
        print 'Error on input image: ', b12
        exit();
    print 'execution...'
    cv2.imshow('Start Image',b16)
    h,b1 = b16.shape[0], b16.shape[1]
    m,b4 = cv2.meanStdDev(b16)
    b17 = class1(b16,b13,b14)
    b18 = b17.b6
    b19 = b16
    for e in b18:
        a7 = 255
        if e[5]<b13:
            a7 = 0
        cv2.rectangle(b19, (e[0],e[1]), (e[0]+e[2],e[1]+e[3]), a7, 1)
    cv2.imshow('Quad Image',b19)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b20 = = '__main__':
    fonk5( sys.argv[1] )