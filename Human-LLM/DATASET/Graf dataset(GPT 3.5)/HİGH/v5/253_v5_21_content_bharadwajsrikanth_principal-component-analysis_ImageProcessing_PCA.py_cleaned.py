import cv2
import numpy as np
from sklearn.feature_extraction import image
from matplotlib import pyplot as plt
from PIL import Image
b1 = cv2.imread('clockwork-angels.jpg').astype(np.float64)
b2 = b1[:, :, 2]
b3 = image.extract_patches_2d(b2, patch_size=(16, 16))
b4 = np.zeros((256, 256))
for b9 in b3:
    b5 = b9.flatten().reshape(-1, 1)
    b4 += np.dot(b5, b5.T)
eigenvalues, b6 = np.linalg.eig(b4)
b7 = np.argsort(eigenvalues)[::-1]
for i in range(64):
    b8 = b6[:, b7[i]]
    b9 = b8.reshape(16, 16)
    plt.imsave(f"Result{i}.png", b9.real, b10 = 'Greys')
b11 = Image.new('RGB', (142, 142), "white")
a1, b12 = 0, 0
for i in range(64):
    b13 = Image.open(f"Result{i}.png")
    b11.paste(b13, (a1, b12))
    a1 += 18
    if (i + 1) % b14 = = 0:
        a1 = 0
        b12 += 18
b11.show()