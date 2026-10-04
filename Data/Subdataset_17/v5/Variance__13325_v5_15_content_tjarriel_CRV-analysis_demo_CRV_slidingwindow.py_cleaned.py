import cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
def process_singularity_index_images(base_dir, step_sizes):
    psi_images = sorted(glob.glob(os.path.join(base_dir, '**/*.TIF'), recursive=True))
    if not psi_images:
        print("No .TIF files found in the specified directory.")
        return
    print(f'Number of singularity index images: {len(psi_images)}')
    first_image = cv2.imread(psi_images[0], cv2.IMREAD_UNCHANGED)
    image_shape = first_image.shape
    for step_size in step_sizes:
        number_sections = (len(psi_images) - step_size) + 1
        print(f'\nStep size: {step_size}')
        print(f'Number of windows: {number_sections}')
        psi_array = np.zeros((step_size, *image_shape), dtype='float32')
        averages = []
        window_indices = list(range(number_sections))
        for window_start in range(number_sections):
            for j in range(window_start, window_start + step_size):
                psi_image = cv2.imread(psi_images[j], cv2.IMREAD_UNCHANGED)
                psi_array[j - window_start] = psi_image
            channel_var = np.var(psi_array, axis=0)
            avg_crv = np.mean(channel_var)
            print(f'Window {window_start}: Average CRV = {avg_crv}')
            averages.append(avg_crv)
        plot_and_save_results(window_indices, averages, step_size, base_dir)
    print('Processing completed.')
def plot_and_save_results(x_values, y_values, step_size, output_dir):
    plt.scatter(x_values, y_values)
    plt.xlabel('Window Number')
    plt.ylabel('Average CRV for Window Images')
    plt.title(f'Sliding Window Plot (Step Size: {step_size})')
    output_tif = os.path.join(output_dir, f"demo_slidingwindow_{step_size}.TIF")
    output_eps = os.path.join(output_dir, f"demo_slidingwindow_{step_size}.eps")
    plt.savefig(output_tif)
    plt.savefig(output_eps, format='eps')
    plt.close()
base_dir = '/home/engrla/rivamap/SIESD related/SlidingWindow/demo_PSIs'
step_sizes = range(15, 60, 5)
process_singularity_index_images(base_dir, step_sizes)