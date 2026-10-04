import numpy as np
import cv2
import sys
import argparse
def split_image(image):
    h, w = image.shape[:2]
    if w >= h:
        mid_x = w
        img1 = image[:, :mid_x]
        img2 = image[:, mid_x:]
        return 0, 0, img1, mid_x, 0, img2
    else:
        mid_y = h
        img1 = image[:mid_y, :]
        img2 = image[mid_y:, :]
        return 0, 0, img1, 0, mid_y, img2
class QuadTree:
    def __init__(self, img, std_min, size_min):
        self.roi_list = []
        self.quadtree(img, std_min, size_min, 0, 0)
    def quadtree(self, image, min_std, min_size, offset_x, offset_y):
        h, w = image.shape[:2]
        mean, std_dev = cv2.meanStdDev(image)
        if std_dev >= min_std and max(h, w) > min_size:
            off1_x, off1_y, img1, off2_x, off2_y, img2 = split_image(image)
            self.quadtree(img1, min_std, min_size, offset_x + off1_x, offset_y + off1_y)
            self.quadtree(img2, min_std, min_size, offset_x + off2_x, offset_y + off2_y)
        else:
            self.roi_list.append([offset_x, offset_y, w, h, mean, std_dev])
def load_and_process_image(image_path):
    raw_image = cv2.imread(image_path)
    if raw_image is not None:
        if raw_image.ndim > 2:
            return cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
        return raw_image
    else:
        print(f'Error: Unable to load image: {image_path}')
        sys.exit(1)
def draw_quadtree_rois(image, rois, min_std_dev):
    output_image = image.copy()
    for roi in rois:
        color = 255 if roi[5] >= min_std_dev else 0
        cv2.rectangle(output_image, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), color, 1)
    return output_image
def main():
    parser = argparse.ArgumentParser(description='Compute best bars cuts')
    parser.add_argument('-img', required=True, type=str, help='Image to load')
    parser.add_argument('-sz', required=True, type=int, help='Quadtree min size')
    parser.add_argument('-std', required=True, type=float, help='Standard deviation to split')
    args = parser.parse_args()
    image_path = args.img
    min_size = args.sz
    min_std_dev = args.std
    gray_image = load_and_process_image(image_path)
    print('Processing image...')
    cv2.imshow('Original Image', gray_image)
    quad_tree = QuadTree(gray_image, min_std_dev, min_size)
    output_image = draw_quadtree_rois(gray_image, quad_tree.roi_list, min_std_dev)
    cv2.imshow('QuadTree Segmented Image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()