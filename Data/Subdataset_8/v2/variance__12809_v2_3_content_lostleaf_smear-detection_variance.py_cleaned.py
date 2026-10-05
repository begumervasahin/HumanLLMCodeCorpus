import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
import os
def calculate_variance(file_names):
    img = cv2.imread(file_names[0], cv2.IMREAD_GRAYSCALE)
    img_sum = np.zeros_like(img, dtype=np.float64)
    img_sqr_sum = np.zeros_like(img, dtype=np.float64)
    for name in file_names:
        img = cv2.imread(name, cv2.IMREAD_GRAYSCALE).astype(np.float64)
        img_sum += img
        img_sqr_sum += img ** 2
    n = len(file_names)
    mean = img_sum / n
    variance = img_sqr_sum / n - (mean ** 2)
    return variance
def main(argv):
    if len(argv) != 2:
        print("Usage: python %s [folder of images]" % argv[0])
        sys.exit(-1)
    path = argv[1]
    variance = calculate_variance(glob.glob(os.path.join(path, "*.jpg")))
    plt.imshow(variance, cmap='gray')
    plt.colorbar()
    plt.show()
    if path.endswith('/'):
        path = path[:-1]
    folder_name = os.path.basename(path)
    np.save("%s_variance.npy" % folder_name, variance)
if __name__ == '__main__':
    main(sys.argv)