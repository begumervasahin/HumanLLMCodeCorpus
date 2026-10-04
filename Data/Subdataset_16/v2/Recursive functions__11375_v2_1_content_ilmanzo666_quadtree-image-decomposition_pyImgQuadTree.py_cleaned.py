import numpy as np
import cv2
import sys
import argparse
def fonk1(image):
    h, b1 = image.shape[:2]
    if b1 >= h:
        b2 = b1
        b3 = image[:, :b2]
        b4 = image[:, b2:]
        return 0, 0, b3, b2, 0, b4
    else:
        b5 = h
        b3 = image[:b5, :]
        b4 = image[b5:, :]
        return 0, 0, b3, 0, b5, b4
class class1:
    def fonk2(self, img, std_min, size_min):
        self.b6 = []
        self.fonk3(img, std_min, size_min, 0, 0)
    def fonk3(self, image, min_std, b12, offset_x, offset_y):
        h, b1 = image.shape[:2]
        mean, b7 = cv2.meanStdDev(image)
        if b7 >= min_std and max(h, b1) > b12:
            off1_x, off1_y, b3, off2_x, off2_y, b4 = fonk1(image)
            self.fonk3(b3, min_std, b12, offset_x + off1_x, offset_y + off1_y)
            self.fonk3(b4, min_std, b12, offset_x + off2_x, offset_y + off2_y)
        else:
            self.b6.append([offset_x, offset_y, b1, h, mean, b7])
def fonk4():
    b8 = argparse.ArgumentParser(description='Compute best bars cuts')
    b8.add_argument('-img', b9 = True, type=str, help='Image to load')
    b8.add_argument('-sz', b9 = True, type=int, help='Quadtree min size')
    b8.add_argument('-std', b9 = True, type=float, help='Standard deviation to split')
    b10 = b8.parse_args()
    b11 = b10.img
    b12 = b10.sz
    b13 = b10.std
    b14 = cv2.imread(b11)
    if b14 is not None:
        if b14.ndim > 2:
            b15 = cv2.cvtColor(b14, cv2.COLOR_BGR2GRAY)
        else:
            b15 = b14
    else:
        print(f'Error: Unable to load image: {b11}')
        sys.exit(1)
    print('Processing image...')
    cv2.imshow('Original Image', b15)
    b16 = class1(b15, b13, b12)
    b17 = b16.b6
    b18 = b15.copy()
    for roi in b17:
        b19 = 255 if roi[5] >= b13 else 0
        cv2.rectangle(b18, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), b19, 1)
    cv2.imshow('class1 Segmented Image', b18)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b20 = = '__main__':
    fonk4()