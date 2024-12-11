import numpy as np
import cv2
import sys
import argparse
class class1:
    def fonk1(self, b16, min_std, min_size):
        self.b1 = []
        self.fonk3(b16, min_std, min_size, 0, 0)
    def fonk2(self, in_img):
        h, b2 = in_img.shape[0], in_img.shape[1]
        if b2 >= h:
            b3 = b2
            b4 = in_img[0:h, 0:b3]
            b5 = in_img[0:h, b3:b2]
        else:
            b6 = h
            b4 = in_img[0:b6, 0:b2]
            b5 = in_img[b6:h, 0:b2]
        return b4, b5
    def fonk3(self, in_img, min_std, min_size, off_x, off_y):
        h, b2 = in_img.shape[0], in_img.shape[1]
        m, b7 = cv2.meanStdDev(in_img)
        if b7 >= min_std and max(h, b2) > min_size:
            im1, b8 = self.fonk2(in_img)
            self.fonk3(im1, min_std, min_size, off_x, off_y)
            self.fonk3(b8, min_std, min_size, off_x + (b2
        else:
            self.b1.append([off_x, off_y, b2, h, m, b7])
def fonk4():
    b9 = argparse.ArgumentParser(description='Compute best bars cuts')
    b9.add_argument('-b16', b10 = '', type=str, help='image to load')
    b9.add_argument('-sz', b10 = '', type=int, help='quadtree min size')
    b9.add_argument('-std', b10 = '', type=float, help='standard deviation to split')
    b11 = b9.parse_args()
    if not (b11.b16 and b11.sz and b11.std):
        b9.error('Please provide all arguments: -b16, -sz, -std')
    b12 = b11.b16
    b13 = b11.sz
    b14 = b11.std
    b15 = cv2.imread(b12)
    if b15 is not None:
        if b15.ndim > 1:
            b16 = cv2.cvtColor(b15, cv2.COLOR_BGR2GRAY)
        else:
            b16 = b15
    else:
        print('Error loading input image:', b12)
        return
    print('Executing...')
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