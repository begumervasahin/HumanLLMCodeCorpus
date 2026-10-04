import cv2
import os
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt
def fonk1(directory, b1 = 3000, image_size=(64, 64)):
    b2 = []
    for i, file in enumerate(os.listdir(directory)):
        if i < b1:
            b3 = cv2.imread(os.path.join(directory, file), 0)
            b3 = cv2.resize(b3, image_size)
            b2.append(b3)
    return b2
def fonk2(b2):
    print("Creating data matrix", b4 = " ... ")
    b5 = len(b2)
    b6 = b2[0].shape
    b7 = np.zeros((b5, b6[0] * b6[1]), dtype=np.float32)
    for i in range(b5):
        b8 = b2[i].flatten()
        b7[i, :] = b8
    print("DONE")
    return b7
b9 = "GImagesTrain/GoodImages"
b2 = fonk1(b9)
b10 = b2[0].shape
b7 = fonk2(b2)
b11 = np.cov(b7, rowvar=False)
print(f"Covariance matrix shape: {b11.shape}")
b14, b12 = sl.eig(b11)
b13 = b14.argsort()[::-1]
b14 = b14[b13]
b12 = b12[:, b13]
b15 = b7[250]
b15 = np.matrix(b15).transpose()
b16 = b15.reshape(64, 64).astype(np.float32)
print(f"Original b8 shape: {b16.shape}")
b12 = b12.transpose()
b17 = b12[:75].real
print(f"Top eigenvectors shape: {b17.shape}")
b18 = b17 @ b15
print(f"Projected b8 shape: {b18.shape}")
b19 = (b17.transpose() @ b18).reshape(64, 64)
print(f"Reconstructed b8 shape: {b19.shape}")
b19 /= 255
b16 /= 255
plt.imshow(b19, b20 = 'gray')
plt.title("Reconstructed Image")
plt.show()
plt.imshow(b16, b20 = 'gray')
plt.title("Original Image")
plt.show()