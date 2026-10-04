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
            if b3 is not None:
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
def fonk3(b7):
    b9 = np.cov(b7, rowvar=False)
    print(f"Covariance matrix shape: {b9.shape}")
    b12, b10 = sl.eig(b9)
    b11 = b12.argsort()[::-1]
    b12 = b12[b11]
    b10 = b10[:, b11]
    return b12, b10
def fonk4(b10, image_vector, b13 = 75):
    b14 = b10[:, :b13].real
    b15 = b14.T @ image_vector
    b16 = b14 @ b15
    return b16
def fonk5(b21, b16):
    plt.figure(b17 = (10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(b21, b18 = 'gray')
    plt.title("Original Image")
    plt.subplot(1, 2, 2)
    plt.imshow(b16, b18 = 'gray')
    plt.title("Reconstructed Image")
    plt.show()
b19 = "GImagesTrain/GoodImages"
b2 = fonk1(b19)
b7 = fonk2(b2)
b12, b10 = fonk3(b7)
b20 = b7[250]
b21 = b20.reshape(64, 64).astype(np.float32)
b16 = fonk4(b10, b20)
b21 /= 255
b16 = b16.reshape(64, 64) / 255
fonk5(b21, b16)