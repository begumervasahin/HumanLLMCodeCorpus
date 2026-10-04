import cv2
import os
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt
def fonk1(b8):
    b1 = []
    for i, file in enumerate(os.listdir(b8)):
        if i < 3000:
            b2 = cv2.imread(os.path.join(b8, file), 0)
            b2 = cv2.resize(b2, (64, 64))
            b1.append(b2)
    return b1
def fonk2(b9):
    print("Creating b6 matrix", b3 = " ... ")
    b4 = len(b9)
    b5 = b9[0].shape
    b6 = np.zeros((b4, b5[0] * b5[1]), dtype=np.float32)
    for i in range(b4):
        b7 = b9[i].flatten()
        b6[i, :] = b7
    print("DONE")
    return b6
b8 = "GImagesTrain/GoodImages"
b9 = fonk1(b8)
b6 = fonk2(b9)
b10 = np.cov(b6, rowvar=False)
print(f"Covariance matrix shape: {b10.shape}")
b13, b11 = sl.eig(b10)
b12 = b13.argsort()[::-1]
b13 = b13[b12]
b11 = b11[:, b12]
b14 = b6[250]
b14 = np.matrix(b14).transpose()
b15 = b14.reshape(64, 64)
b15 = np.array(b15)
print(f"Original b7 shape: {b15.shape}")
b11 = b11.transpose()
b16 = b11[:75].real
print(f"Eigenvectors shape: {b16.shape}")
b17 = b16 @ b14
print(f"Projected shape: {b17.shape}")
b18 = np.matmul(b16.transpose(), b17)
b19 = b18.reshape(64, 64)
print(f"Reconstructed shape: {b18.shape}")
b19 /= 255
b15 /= 255
plt.imshow(b19, b20 = 'gray')
plt.title('Reconstructed Image')
plt.show()
plt.imshow(b15, b20 = 'gray')
plt.title('Original Image')
plt.show()