import numpy as np
import cv2
import sys
import argparse
def split_image(in_img):
    h, w = in_img.shape[0], in_img.shape[1]
    if w >= h:
        off1_x = 0
        off2_x = w
        img1 = in_img[0:h, 0:off2_x]
        img2 = in_img[0:h, off2_x:w]
    else:
        off1_y = 0
        off2_y = h
        img1 = in_img[0:off2_y, 0:w]
        img2 = in_img[off2_y:h, 0:w]
    return off1_x, off1_y, img1, off2_x, off2_y, img2
class QuadTree:
    def __init__(self, img, std_min, size_min):
        self.list_roi = []
        self.qt(img, std_min, size_min, 0, 0)
    def qt(self, in_img, min_std, min_size, off_x, off_y):
        h, w = in_img.shape[0], in_img.shape[1]
        m, s = cv2.meanStdDev(in_img)
        if s >= min_std and max(h, w) > min_size:
            o_x1, o_y1, im1, o_x2, o_y2, im2 = split_image(in_img)
            self.qt(im1, min_std, min_size, off_x + o_x1, off_y + o_y1)
            self.qt(im2, min_std, min_size, off_x + o_x2, off_y + o_y2)
        else:
            self.list_roi.append([off_x, off_y, w, h, m, s])
def quadtree(in_img, min_std, min_size, off_x, off_y, roi_list):
    h, w = in_img.shape[0], in_img.shape[1]
    m, s = cv2.meanStdDev(in_img)
    if s >= min_std and max(h, w) > min_size:
        o_x1, o_y1, im1, o_x2, o_y2, im2 = split_image(in_img)
        quadtree(im1, min_std, min_size, off_x + o_x1, off_y + o_y1, roi_list)
        quadtree(im2, min_std, min_size, off_x + o_x2, off_y + o_y2, roi_list)
    else:
        roi_list.append([off_x, off_y, w, h, m, s])
def main():
    parser = argparse.ArgumentParser(description='Compute best bars cuts')
    parser.add_argument('-img', type=str, required=True, help='image to load')
    parser.add_argument('-sz', type=int, required=True, help='quadtree min size')
    parser.add_argument('-std', type=float, required=True, help='standard deviation to split')
    args = parser.parse_args()
    image_to_load = args.img
    min_dev = args.std
    min_sz = args.sz
    raw = cv2.imread(image_to_load)
    if raw is None:
        print(f'Error on input image: {image_to_load}')
        sys.exit()
    img = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY) if raw.ndim > 1 else raw
    print('Execution...')
    cv2.imshow('Start Image', img)
    qt = QuadTree(img, min_dev, min_sz)
    rois = qt.list_roi
    img_out = img.copy()
    for e in rois:
        col = 0 if e[5] < min_dev else 255
        cv2.rectangle(img_out, (e[0], e[1]), (e[0] + e[2], e[1] + e[3]), col, 1)
    cv2.imshow('Quad Image', img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()