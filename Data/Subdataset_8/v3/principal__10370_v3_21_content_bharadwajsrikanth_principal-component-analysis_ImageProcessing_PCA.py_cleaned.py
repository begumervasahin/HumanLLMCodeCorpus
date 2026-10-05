import cv2
import numpy as np
from PIL import Image
from sklearn.feature_extraction import image
import matplotlib.pyplot as plt
def load_image(image_path):
    return cv2.imread(image_path).astype(np.float64)
def extract_patches(image_channel, patch_size=(16, 16), num_patches=1000):
    return image.extract_patches_2d(image_channel, patch_size=patch_size, max_patches=num_patches)
def compute_correlation_matrix(patches):
    correlation_matrix = np.zeros((256, 256))
    for patch in patches:
        patch_vector = patch.reshape(256, 1)
        outer_product = patch_vector.dot(patch_vector.T)
        correlation_matrix += outer_product
    return correlation_matrix
def save_patches_as_images(eigenvectors, num_patches=64, patch_size=(16, 16)):
    for i in range(num_patches):
        patch = np.reshape(eigenvectors[:, i], patch_size)
        plt.imsave(f"Result{i}.png", patch.real, cmap='Greys')
def create_result_image(patch_filenames, result_size=(142, 142), patch_offset=18):
    result_image = Image.new('RGB', result_size, "white")
    y_coordinate = 0
    for _ in range(8):
        x_coordinate = 0
        for filename in patch_filenames:
            patch_image = Image.open(filename)
            result_image.paste(patch_image, (x_coordinate, y_coordinate))
            x_coordinate += patch_offset
        y_coordinate += patch_offset
    return result_image
original_image = load_image('clockwork-angels.jpg')
blue_channel, green_channel, red_channel = cv2.split(original_image)
patches = extract_patches(red_channel)
correlation_matrix = compute_correlation_matrix(patches)
eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
save_patches_as_images(eigenvectors, num_patches=64)
patch_filenames = [f"Result{i}.png" for i in range(64)]
result_image = create_result_image(patch_filenames)
result_image.show()