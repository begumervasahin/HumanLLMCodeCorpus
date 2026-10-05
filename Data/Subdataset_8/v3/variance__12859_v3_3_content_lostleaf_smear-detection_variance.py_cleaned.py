import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
import os
def calculate_variance(file_paths):
    first_image = cv2.imread(file_paths[0], cv2.IMREAD_GRAYSCALE)
    img_sum = np.zeros_like(first_image, dtype=np.float64)
    img_sqr_sum = np.zeros_like(first_image, dtype=np.float64)
    for file_path in file_paths:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE).astype(np.float64)
        img_sum += image
        img_sqr_sum += image ** 2
    num_images = len(file_paths)
    mean = img_sum / num_images
    variance = img_sqr_sum / num_images - (mean ** 2)
    return variance
def main(argv):
    if len(argv) != 2:
        print("Usage: python %s [folder of images]" % argv[0])
        sys.exit(1)
    folder_path = argv[1]
    variance = calculate_variance(glob.glob(os.path.join(folder_path, "*.jpg")))
    plt.imshow(variance, cmap='gray')
    plt.colorbar()
    plt.show()
    folder_name = os.path.basename(folder_path.rstrip('/'))
    np.save(f"{folder_name}_variance.npy", variance)
if __name__ == '__main__':
    main(sys.argv)