import numpy as np
import cv2
import sys
import argparse
def fonk1(in_img):
    h, b1 = in_img.shape[0], in_img.shape[1]
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    if b1 >= h:
        a1 = 0
        a3 = b1 / 2
        b2 = in_img[0:h, 0:a3]
        b3 = in_img[0:h, a3:b1]
    else:
        a2 = 0
        a4 = h / 2
        b2 = in_img[0:a4, 0:b1]
        b3 = in_img[a4:h, 0:b1]
    return a1, a2, b2, a3, a4, b3
class class1:
    def fonk2(self, b16, std_min, size_min):
        self.b4 = []
        self.fonk3(b16, std_min, size_min, 0, 0)
    def fonk3(self, in_img, min_std, b14, off_x, off_y):
        h, b1 = in_img.shape[0], in_img.shape[1]
        m, b5 = cv2.meanStdDev(in_img)
        if b5 >= min_std and max(h, b1) > b14:
            o_x1, o_y1, im1, o_x2, o_y2, b6 = fonk1(in_img)
            self.fonk3(im1, min_std, b14, off_x + o_x1, off_y + o_y1)
            self.fonk3(b6, min_std, b14, off_x + o_x2, off_y + o_y2)
        else:
            self.b4.append([off_x, off_y, b1, h, m, b5])
def fonk4(file_path):
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
    if b15 is not None:
        if b15.ndim > 1:
            b16 = cv2.cvtColor(b15, cv2.COLOR_BGR2GRAY)
        else:
            b16 = b15
    else:
        print('Error on input image:', b12)
        exit()
    print('Execution...')
    cv2.imshow('Start Image', b16)
    h, b1 = b16.shape[0], b16.shape[1]
    b17 = class1(b16, b13, b14)
    b18 = b17.b4
    b19 = b16
    for e in b18:
        a5 = 255
        if e[5] < b13:
            a5 = 0
        cv2.rectangle(b19, (e[0], e[1]), (e[0] + e[2], e[1] + e[3]), a5, 1)
    cv2.imshow('Quad Image', b19)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b20 = = '__main__':
    fonk4(sys.argv[1])