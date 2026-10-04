import cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from rivamap import singularity_index, georef
def process_singularity_index_images(base_dir, step_sizes):
    psi_images = sorted(glob.glob(os.path.join(base_dir, '*/*.TIF')))
    if not psi_images:
        print("No .TIF files found in the specified directory.")
        return
    print(f'Number of singularity index images: {len(psi_images)}')
    I1 = cv2.imread(psi_images[0], cv2.IMREAD_UNCHANGED)
    for step_size in step_sizes:
        number_sections = (len(psi_images) - step_size) + 1
        print(f'\nStep size: {step_size}')
        print(f'Number of windows: {number_sections}')
        psi_array = np.zeros((step_size, I1.shape[0], I1.shape[1]), dtype='float32')
        averages = []
        xval = list(range(0, number_sections))
        for i in range(number_sections):
            for j in range(i, i + step_size):
                psi = cv2.imread(psi_images[j], cv2.IMREAD_UNCHANGED)
                psi_array[j - i, :, :] = psi
            channel_var = np.var(psi_array, axis=0)
            avg = np.mean(channel_var)
            print(f'Window {i}: Average CRV = {avg}')
            averages.append(avg)
        plt.scatter(xval, averages)
        plt.xlabel('Window Number')
        plt.ylabel('Average CRV for Window Images')
        plt.title(f'Sliding Window Plot (Step Size: {step_size})')
        plt.savefig(os.path.join(base_dir, f"demo_slidingwindow_{step_size}.TIF"))
        plt.savefig(os.path.join(base_dir, f"demo_slidingwindow_{step_size}.eps"), format='eps')
        plt.close()
    print('Processing completed.')
base_dir = '/home/engrla/rivamap/SIESD related/SlidingWindow/demo_PSIs'
step_sizes = range(15, 60, 5)
process_singularity_index_images(base_dir, step_sizes)