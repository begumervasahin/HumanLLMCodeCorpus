import cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
def fonk1(b15, b16):
    b1 = sorted(glob.glob(os.path.join(b15, '**/*.TIF'), recursive=True))
    if not b1:
        print("No .TIF files found in the specified directory.")
        return
    print(f'Number of singularity index images: {len(b1)}')
    b2 = cv2.imread(b1[0], cv2.IMREAD_UNCHANGED)
    b3 = b2.shape
    for step_size in b16:
        b4 = (len(b1) - step_size) + 1
        print(f'\nStep size: {step_size}')
        print(f'Number of windows: {b4}')
        b5 = np.zeros((step_size, *b3), dtype='float32')
        b6 = []
        b7 = list(range(b4))
        for window_start in range(b4):
            for j in range(window_start, window_start + step_size):
                b8 = cv2.imread(b1[j], cv2.IMREAD_UNCHANGED)
                b5[j - window_start] = b8
            b9 = np.var(b5, axis=0)
            b10 = np.mean(b9)
            print(f'Window {window_start}: Average b11 = {b10}')
            b6.append(b10)
        fonk2(b7, b6, step_size, b15)
    print('Processing completed.')
def fonk2(x_values, y_values, step_size, output_dir):
    plt.scatter(x_values, y_values)
    plt.xlabel('Window Number')
    plt.ylabel('Average b11 for Window Images')
    plt.title(f'Sliding Window Plot (Step Size: {step_size})')
    b12 = os.path.join(output_dir, f"demo_slidingwindow_{step_size}.TIF")
    b13 = os.path.join(output_dir, f"demo_slidingwindow_{step_size}.eps")
    plt.savefig(b12)
    plt.savefig(b13, b14 = 'eps')
    plt.close()
b15 = '/home/engrla/rivamap/SIESD related/SlidingWindow/demo_PSIs'
b16 = range(15, 60, 5)
fonk1(b15, b16)