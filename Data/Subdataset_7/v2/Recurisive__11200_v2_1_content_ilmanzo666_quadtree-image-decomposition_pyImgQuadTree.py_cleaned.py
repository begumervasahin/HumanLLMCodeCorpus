import numpy as np
import cv2
import sys
import argparse
def fonk1(in_img):
    h, b1 = in_img.shape[0], in_img.shape[1]
    off1_x, off1_y, b3, b2 = 0, 0, 0, 0
    if b1 >= h:
        b3 = b1
        b4 = in_img[0:h, 0:b3]
        b5 = in_img[0:h, b3:b1]
    else:
        b2 = h
        b4 = in_img[0:b2, 0:b1]
        b5 = in_img[b2:h, 0:b1]
    return b4, b5, off1_x, off1_y, b3, b2
class class1:
    def fonk2(self, b16, min_std, min_size):
        self.b6 = []
        self.fonk3(b16, min_std, min_size, 0, 0)
    def fonk3(self, in_img, min_std, min_size, off_x, off_y):
        h, b1 = in_img.shape[0], in_img.shape[1]
        m, b7 = cv2.meanStdDev(in_img)
        if b7 >= min_std and max(h, b1) > min_size:
            im1, im2, o_x1, o_y1, o_x2, b8 = fonk1(in_img)
            self.fonk3(im1, min_std, min_size, off_x + o_x1, off_y + o_y1)
            self.fonk3(im2, min_std, min_size, off_x + o_x2, off_y + b8)
        else:
            self.b6.append([off_x, off_y, b1, h, m, b7])
def fonk4(file_path):
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
        if b15.ndim > 1:
            b16 = cv2.cvtColor(b15, cv2.COLOR_BGR2GRAY)
        else:
            b16 = b15
    else:
        print('Error on input image:', b12)
        return
    print('Execution...')
    cv2.imshow('Start Image', b16)
    b17 = class1(b16, b13, b14)
    b18 = b17.b6
    b19 = b16.copy()
    for e in b18:
        b20 = 255 if e[5] < b13 else 0
        cv2.rectangle(b19, (e[0], e[1]), (e[0] + e[2], e[1] + e[3]), b20, 1)
    cv2.imshow('Quad Image', b19)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b21 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py image_path")
    else:
        fonk4(sys.argv[1])