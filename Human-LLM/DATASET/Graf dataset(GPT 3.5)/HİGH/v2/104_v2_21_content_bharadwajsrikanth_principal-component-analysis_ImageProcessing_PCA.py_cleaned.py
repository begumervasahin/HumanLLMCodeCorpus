import cv2
from PIL import Image
from sklearn.feature_extraction import image
import numpy as np
import matplotlib.pyplot as plt
b1 = cv2.imread('clockwork-angels.jpg')
b1 = b1.astype(np.float64)
blue_channel, green_channel, b2 = cv2.split(b1)
b3 = (16, 16)
b4 = image.extract_patches_2d(b2, b3=b3)
b5 = np.zeros((256, 256))
for index in range(1000):
    b6 = np.array(b4[index]).reshape(256, 1)
    b7 = b6.dot(b6.T)
    b5 = np.add(b5, b7)
eigenvalues, b8 = np.linalg.eig(b5)
b9 = np.argsort(eigenvalues)[::-1]
for i in range(64):
    b10 = b8[:, b9[i]]
    b11 = np.reshape(b10, b3)
    plt.imsave(f"Result{i}.png", b11.real, b12 = 'Greys')
b13 = Image.new('RGB', (142, 142), "white")
a1 = 0
a2 = 0
for _ in range(8):
    a3 = 0
    for _ in range(8):
        b14 = Image.open(f"Result{a2}.png")
        a2 += 1
        b13.paste(b14, (a3, a1))
        a3 += 18
    a1 += 18
b13.show()