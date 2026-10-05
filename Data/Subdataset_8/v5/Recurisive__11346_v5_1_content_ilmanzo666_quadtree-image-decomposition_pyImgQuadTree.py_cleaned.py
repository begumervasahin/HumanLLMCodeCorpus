import numpy as np
import cv2
import sys
import argparse
class QuadTree:
    def __init__(self, img, min_std, min_size):
        self.list_roi = []
        self.quad_tree(img, min_std, min_size, 0, 0)
    def quad_tree(self, in_img, min_std, min_size, off_x, off_y):
        h, w = in_img.shape[:2]
        m, s = cv2.meanStdDev(in_img)
        if s >= min_std and max(h, w) > min_size:
            o_x1, o_y1, im1, o_x2, o_y2, im2 = self.split_image(in_img)
            self.quad_tree(im1, min_std, min_size, off_x + o_x1, off_y + o_y1)
            self.quad_tree(im2, min_std, min_size, off_x + o_x2, off_y + o_y2)
        else:
            self.list_roi.append([off_x, off_y, w, h, m, s])
    def split_image(self, in_img):
        h, w = in_img.shape[:2]
        off1_x, off1_y, off2_x, off2_y = 0, 0, 0, 0
        if w >= h:
            off2_x = w
            img1 = in_img[0:h, 0:off2_x]
            img2 = in_img[0:h, off2_x:w]
        else:
            off2_y = h
            img1 = in_img[0:off2_y, 0:w]
            img2 = in_img[off2_y:h, 0:w]
        return off1_x, off1_y, img1, off2_x, off2_y, img2
def main():
    parser = argparse.ArgumentParser(description='Compute best bars cuts')
    parser.add_argument('-img', metavar='', type=str, help='image to load')
    parser.add_argument('-sz', metavar='', type=int, help='quadtree min size')
    parser.add_argument('-std', metavar='', type=float, help='standard deviation to split')
    args = parser.parse_args()
    image_to_load = args.img
    min_deviation = args.sz
    min_size = args.std
    raw = cv2.imread(image_to_load)
    if raw is not None:
        img = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY) if raw.ndim > 1 else raw
    else:
        print('Error on input image:', image_to_load)
        return
    print('Execution...')
    cv2.imshow('Start Image', img)
    qt = QuadTree(img, min_deviation, min_size)
    rois = qt.list_roi
    img_out = img.copy()
    for e in rois:
        col = 255 if e[5] < min_deviation else 0
        cv2.rectangle(img_out, (e[0], e[1]), (e[0] + e[2], e[1] + e[3]), col, 1)
    cv2.imshow('Quad Image', img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()