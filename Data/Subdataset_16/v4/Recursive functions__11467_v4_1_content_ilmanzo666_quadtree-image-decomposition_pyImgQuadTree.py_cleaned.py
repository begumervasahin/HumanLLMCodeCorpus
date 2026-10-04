import numpy as np
import cv2
import sys
import argparse
def fonk1(in_img):
    h, b1 = in_img.shape[0], in_img.shape[1]
    if b1 >= h:
        a1 = 0
        b2 = b1
        b3 = in_img[0:h, 0:b2]
        b4 = in_img[0:h, b2:b1]
    else:
        a2 = 0
        b5 = h
        b3 = in_img[0:b5, 0:b1]
        b4 = in_img[b5:h, 0:b1]
    return a1, a2, b3, b2, b5, b4
class class1:
    def fonk2(self, b16, std_min, size_min):
        self.b6 = []
        self.fonk3(b16, std_min, size_min, 0, 0)
    def fonk3(self, in_img, min_std, min_size, off_x, off_y):
        h, b1 = in_img.shape[0], in_img.shape[1]
        m, b7 = cv2.meanStdDev(in_img)
        if b7 >= min_std and max(h, b1) > min_size:
            o_x1, o_y1, im1, o_x2, o_y2, b8 = fonk1(in_img)
            self.fonk3(im1, min_std, min_size, off_x + o_x1, off_y + o_y1)
            self.fonk3(b8, min_std, min_size, off_x + o_x2, off_y + o_y2)
        else:
            self.b6.append([off_x, off_y, b1, h, m, b7])
def fonk4(in_img, min_std, min_size, off_x, off_y, roi_list):
    h, b1 = in_img.shape[0], in_img.shape[1]
    m, b7 = cv2.meanStdDev(in_img)
    if b7 >= min_std and max(h, b1) > min_size:
        o_x1, o_y1, im1, o_x2, o_y2, b8 = fonk1(in_img)
        fonk4(im1, min_std, min_size, off_x + o_x1, off_y + o_y1, roi_list)
        fonk4(b8, min_std, min_size, off_x + o_x2, off_y + o_y2, roi_list)
    else:
        roi_list.append([off_x, off_y, b1, h, m, b7])
def fonk5():
    b9 = argparse.ArgumentParser(description='Compute best bars cuts')
    b9.add_argument('-b16', b10 = str, required=True, help='image to load')
    b9.add_argument('-sz', b10 = int, required=True, help='quadtree min size')
    b9.add_argument('-std', b10 = float, required=True, help='standard deviation to split')
    b11 = b9.parse_args()
    b12 = b11.b16
    b13 = b11.std
    b14 = b11.sz
    b15 = cv2.imread(b12)
    if b15 is None:
        print(f'Error on input image: {b12}')
        sys.exit()
    b16 = cv2.cvtColor(b15, cv2.COLOR_BGR2GRAY) if b15.ndim > 1 else b15
    print('Execution...')
    cv2.imshow('Start Image', b16)
    b17 = class1(b16, b13, b14)
    b18 = b17.b6
    b19 = b16.copy()
    for e in b18:
        b20 = 0 if e[5] < b13 else 255
        cv2.rectangle(b19, (e[0], e[1]), (e[0] + e[2], e[1] + e[3]), b20, 1)
    cv2.imshow('Quad Image', b19)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b21 = = '__main__':
    fonk5()