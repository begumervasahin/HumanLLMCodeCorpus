import cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from rivamap import singularity_index, georef
def fonk1(b12, b13):
    b1 = sorted(glob.glob(os.path.join(b12, '*/*.TIF')))
    if not b1:
        print("No .TIF files found in the specified directory.")
        return
    print(f'Number of singularity index images: {len(b1)}')
    b2 = cv2.imread(b1[0], cv2.IMREAD_UNCHANGED)
    for step_size in b13:
        b3 = (len(b1) - step_size) + 1
        print(f'\nStep size: {step_size}')
        print(f'Number of windows: {b3}')
        b4 = np.zeros((step_size, b2.shape[0], b2.shape[1]), dtype='float32')
        b5 = []
        b6 = list(range(0, b3))
        for i in range(b3):
            for j in range(i, i + step_size):
                b7 = cv2.imread(b1[j], cv2.IMREAD_UNCHANGED)
                b4[j - i, :, :] = b7
            b8 = np.var(b4, axis=0)
            b9 = np.mean(b8)
            print(f'Window {i}: Average b10 = {b9}')
            b5.append(b9)
        plt.scatter(b6, b5)
        plt.xlabel('Window Number')
        plt.ylabel('Average b10 for Window Images')
        plt.title(f'Sliding Window Plot (Step Size: {step_size})')
        plt.savefig(os.path.join(b12, f"demo_slidingwindow_{step_size}.TIF"))
        plt.savefig(os.path.join(b12, f"demo_slidingwindow_{step_size}.eps"), b11 = 'eps')
        plt.close()
    print('Processing completed.')
b12 = '/home/engrla/rivamap/SIESD related/SlidingWindow/demo_PSIs'
b13 = range(15, 60, 5)
fonk1(b12, b13)