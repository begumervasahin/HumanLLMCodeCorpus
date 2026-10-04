import cv2
import numpy as np
from rivamap import singularity_index, georef
import glob
import os
import matplotlib.pyplot as plt
def calculate_crv(base_dir, step_size):
    psi_images = sorted(glob.glob(os.path.join(base_dir, '*/*.TIF')))
    number_sections = (len(psi_images) - step_size) + 1
    print(f'Number of singularity index images: {len(psi_images)}')
    print(f'Number of windows: {number_sections}')
    print(f'Step size: {step_size}')
    I1 = cv2.imread(psi_images[0], cv2.IMREAD_UNCHANGED)
    psi_array = np.zeros((step_size, I1.shape[0], I1.shape[1]), dtype='float32')
    averages = []
    xval = list(range(number_sections))
    for i in range(number_sections):
        for j in range(i, i + step_size):
            psi = cv2.imread(psi_images[j], cv2.IMREAD_UNCHANGED)
            psi_array[j - i, :, :] = psi
        channel_var = np.var(psi_array, axis=0)
        avg = np.mean(channel_var)
        print(f'Window {i}')
        averages.append(avg)
        psi_array.fill(0)
    plt.scatter(xval, averages)
    plt.xlabel('Window number')
    plt.ylabel('Average CRV for window images')
    output_filename_base = os.path.join(base_dir, f"demo_slidingwindow_{step_size}")
    plt.savefig(f"{output_filename_base}.TIF")
    plt.savefig(f"{output_filename_base}.eps", format='eps')
    plt.close()
    print('Completed')
if __name__ == "__main__":
    base_dir = '/home/engrla/rivamap/SIESD_related/SlidingWindow/demo_PSIs'
    for step_size in range(15, 60, 5):
        calculate_crv(base_dir, step_size)