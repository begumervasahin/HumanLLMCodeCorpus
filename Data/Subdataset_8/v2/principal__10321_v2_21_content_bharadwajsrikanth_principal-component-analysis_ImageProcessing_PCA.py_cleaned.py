import cv2
from PIL import Image
from sklearn.feature_extraction import image
import numpy as np
import matplotlib.pyplot as plt
original_image = cv2.imread('clockwork-angels.jpg')
original_image = original_image.astype(np.float64)
blue_channel, green_channel, red_channel = cv2.split(original_image)
patch_size = (16, 16)
patches = image.extract_patches_2d(red_channel, patch_size=patch_size)
correlation_matrix = np.zeros((256, 256))
for index in range(1000):
    patch_vector = np.array(patches[index]).reshape(256, 1)
    outer_product = patch_vector.dot(patch_vector.T)
    correlation_matrix = np.add(correlation_matrix, outer_product)
eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
for i in range(64):
    sorted_eigenvector = eigenvectors[:, sorted_indices[i]]
    patch = np.reshape(sorted_eigenvector, patch_size)
    plt.imsave(f"Result{i}.png", patch.real, cmap='Greys')
result_image = Image.new('RGB', (142, 142), "white")
y_coordinate = 0
patch_index = 0
for _ in range(8):
    x_coordinate = 0
    for _ in range(8):
        patch_image = Image.open(f"Result{patch_index}.png")
        patch_index += 1
        result_image.paste(patch_image, (x_coordinate, y_coordinate))
        x_coordinate += 18
    y_coordinate += 18
result_image.show()