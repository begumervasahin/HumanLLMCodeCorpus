import cv2
import os
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt
def fonk1(b7):
    b1 = []
    for i, file in enumerate(os.listdir(b7)):
        if i < 3000:
            b2 = cv2.imread(os.path.join(b7, file), 0)
            b2 = cv2.resize(b2, (64, 64))
            b1.append(b2)
    return b1
def fonk2(b1):
    print("Creating data matrix", b3 = " ... ")
    b4 = len(b1)
    b5 = b1[0].shape
    b6 = np.zeros((b4, b5[0] * b5[1]), dtype=np.float32)
    for i, image in enumerate(b1):
        b6[i, :] = image.flatten()
    print("DONE")
    return b6
b7 = "GImagesTrain/GoodImages"
b1 = fonk1(b7)
b6 = fonk2(b1)
b8 = np.cov(b6, rowvar=False)
print(f"Covariance matrix shape: {b8.shape}")
b11, b9 = sl.eig(b8)
b10 = b11.argsort()[::-1]
b11 = b11[b10]
b9 = b9[:, b10]
b12 = b6[250]
b13 = np.matrix(b12).transpose()
b14 = b13.reshape(64, 64)
b14 = np.array(b14)
print(f"Original image shape: {b14.shape}")
b9 = b9.transpose()
b15 = b9[:75].real
print(f"Eigenvectors shape: {b15.shape}")
b16 = b15 @ b13
print(f"Projected shape: {b16.shape}")
b17 = np.matmul(b15.transpose(), b16)
b17 = b17.reshape(64, 64)
print(f"Reconstructed shape: {b17.shape}")
b17 /= 255
b14 /= 255
plt.imshow(b17, b18 = 'gray')
plt.title('Reconstructed Image')
plt.show()
plt.imshow(b14, b18 = 'gray')
plt.title('Original Image')
plt.show()