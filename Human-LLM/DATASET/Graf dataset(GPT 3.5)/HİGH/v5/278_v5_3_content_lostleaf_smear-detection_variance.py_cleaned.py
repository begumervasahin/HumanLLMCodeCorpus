import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
import os
def fonk1(file_paths):
    b1 = cv2.imread(file_paths[0], cv2.IMREAD_GRAYSCALE)
    b2 = np.zeros_like(b1, dtype=np.float64)
    b3 = np.zeros_like(b1, dtype=np.float64)
    for file_path in file_paths:
        b4 = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE).astype(np.float64)
        b2 += b4
        b3 += b4 ** 2
    b5 = len(file_paths)
    b6 = b3 / b5 - ((b2 / b5) ** 2)
    return b6
def fonk2(argv):
    if len(argv) != 2:
        print("Usage: python %s [folder of images]" % argv[0])
        sys.exit(-1)
    b7 = argv[1]
    b6 = fonk1(glob.glob(os.path.join(b7, "*.jpg")))
    plt.imshow(b6)
    plt.colorbar()
    plt.show()
    if b7.endswith('/'):
        b7 = b7[:-1]
    b8 = os.path.basename(b7)
    np.save("%s_variance.npy" % b8, b6)
if b9 = = '__main__':
    fonk2(sys.argv)