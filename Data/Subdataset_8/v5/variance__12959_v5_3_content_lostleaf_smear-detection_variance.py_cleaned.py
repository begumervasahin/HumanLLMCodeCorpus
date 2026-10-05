import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
import os
def calculate_variance(file_paths):
    first_img = cv2.imread(file_paths[0], cv2.IMREAD_GRAYSCALE)
    img_sum = np.zeros_like(first_img, dtype=np.float64)
    img_sqr_sum = np.zeros_like(first_img, dtype=np.float64)
    for file_path in file_paths:
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE).astype(np.float64)
        img_sum += img
        img_sqr_sum += img ** 2
    num_images = len(file_paths)
    variance = img_sqr_sum / num_images - ((img_sum / num_images) ** 2)
    return variance
def main(argv):
    if len(argv) != 2:
        print("Usage: python %s [folder of images]" % argv[0])
        sys.exit(-1)
    folder_path = argv[1]
    variance = calculate_variance(glob.glob(os.path.join(folder_path, "*.jpg")))
    plt.imshow(variance)
    plt.colorbar()
    plt.show()
    if folder_path.endswith('/'):
        folder_path = folder_path[:-1]
    folder_name = os.path.basename(folder_path)
    np.save("%s_variance.npy" % folder_name, variance)
if __name__ == '__main__':
    main(sys.argv)