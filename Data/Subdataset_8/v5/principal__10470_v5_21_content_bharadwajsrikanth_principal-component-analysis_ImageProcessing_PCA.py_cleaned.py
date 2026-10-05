import cv2
import numpy as np
from sklearn.feature_extraction import image
from matplotlib import pyplot as plt
from PIL import Image
img = cv2.imread('clockwork-angels.jpg').astype(np.float64)
R_channel = img[:, :, 2]
patches = image.extract_patches_2d(R_channel, patch_size=(16, 16))
correlation_matrix = np.zeros((256, 256))
for patch in patches:
    flattened_patch = patch.flatten().reshape(-1, 1)
    correlation_matrix += np.dot(flattened_patch, flattened_patch.T)
eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
for i in range(64):
    eigenvector = eigenvectors[:, sorted_indices[i]]
    patch = eigenvector.reshape(16, 16)
    plt.imsave(f"Result{i}.png", patch.real, cmap='Greys')
back_img = Image.new('RGB', (142, 142), "white")
x, y = 0, 0
for i in range(64):
    patch_img = Image.open(f"Result{i}.png")
    back_img.paste(patch_img, (x, y))
    x += 18
    if (i + 1) % 8 == 0:
        x = 0
        y += 18
back_img.show()