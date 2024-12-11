import numpy as np
import cv2
import sys
import argparse
class class1:
    def fonk1(self, b16, min_std, b14):
        self.b1 = []
        self.fonk2(b16, min_std, b14, 0, 0)
    def fonk2(self, in_img, min_std, b14, off_x, off_y):
        h, b2 = in_img.shape[:2]
        m, b3 = cv2.meanStdDev(in_img)
        if b3 >= min_std and max(h, b2) > b14:
            o_x1, o_y1, im1, o_x2, o_y2, b4 = self.fonk3(in_img)
            self.fonk2(im1, min_std, b14, off_x + o_x1, off_y + o_y1)
            self.fonk2(b4, min_std, b14, off_x + o_x2, off_y + o_y2)
        else:
            self.b1.append([off_x, off_y, b2, h, m, b3])
    def fonk3(self, in_img):
        h, b2 = in_img.shape[:2]
        off1_x, off1_y, b6, b5 = 0, 0, 0, 0
        if b2 >= h:
            b6 = b2
            b7 = in_img[0:h, 0:b6]
            b8 = in_img[0:h, b6:b2]
        else:
            b5 = h
            b7 = in_img[0:b5, 0:b2]
            b8 = in_img[b5:h, 0:b2]
        return off1_x, off1_y, b7, b6, b5, b8
def fonk4():
    b9 = argparse.ArgumentParser(description='Compute best bars cuts')
    b9.add_argument('-b16', b10 = '', type=str, help='image to load')
    b9.add_argument('-sz', b10 = '', type=int, help='quadtree min size')
    b9.add_argument('-std', b10 = '', type=float, help='standard deviation to split')
    b11 = b9.parse_args()
    b12 = b11.b16
    b13 = b11.sz
    b14 = b11.std
    b15 = cv2.imread(b12)
    if b15 is not None:
        b16 = cv2.cvtColor(b15, cv2.COLOR_BGR2GRAY) if b15.ndim > 1 else b15
    else:
        print('Error on input image:', b12)
        return
    print('Execution...')
    cv2.imshow('Start Image', b16)
    b17 = class1(b16, b13, b14)
    b18 = b17.b1
    b19 = b16.copy()
    for e in b18:
        b20 = 255 if e[5] < b13 else 0
        cv2.rectangle(b19, (e[0], e[1]), (e[0] + e[2], e[1] + e[3]), b20, 1)
    cv2.imshow('Quad Image', b19)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b21 = = '__main__':
    fonk4()