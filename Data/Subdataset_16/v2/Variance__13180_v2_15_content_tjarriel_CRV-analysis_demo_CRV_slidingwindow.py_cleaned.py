import cv2
import numpy as np
from rivamap import singularity_index, georef
import glob
import os
import matplotlib.pyplot as plt
def fonk1(b13, step_size):
    b1 = sorted(glob.glob(os.path.join(b13, '*/*.TIF')))
    b2 = (len(b1) - step_size) + 1
    print(f'Number of singularity index images: {len(b1)}')
    print(f'Number of windows: {b2}')
    print(f'Step size: {step_size}')
    b3 = cv2.imread(b1[0], cv2.IMREAD_UNCHANGED)
    b4 = np.zeros((step_size, b3.shape[0], b3.shape[1]), dtype='float32')
    b5 = []
    b6 = list(range(b2))
    for i in range(b2):
        for j in range(i, i + step_size):
            b7 = cv2.imread(b1[j], cv2.IMREAD_UNCHANGED)
            b4[j - i, :, :] = b7
        b8 = np.var(b4, axis=0)
        b9 = np.mean(b8)
        print(f'Window {i}')
        b5.append(b9)
        b4.fill(0)
    plt.scatter(b6, b5)
    plt.xlabel('Window number')
    plt.ylabel('Average CRV for window images')
    b10 = os.path.join(b13, f"demo_slidingwindow_{step_size}")
    plt.savefig(f"{b10}.TIF")
    plt.savefig(f"{b10}.eps", b11 = 'eps')
    plt.close()
    print('Completed')
if b12 = = "__main__":
    b13 = '/home/engrla/rivamap/SIESD_related/SlidingWindow/demo_PSIs'
    for step_size in range(15, 60, 5):
        fonk1(b13, step_size)