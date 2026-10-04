import cv2
import os
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt
def fonk1(b18, b1 = 3000, img_size=(64, 64)):
    b2 = []
    for i, file in enumerate(os.listdir(b18)):
        if i >= b1:
            break
        b3 = os.path.join(b18, file)
        b4 = cv2.imread(b3, 0)
        if b4 is not None:
            b4 = cv2.resize(b4, img_size)
            b2.append(b4)
    return b2
def fonk2(b2):
    print("Creating data matrix", b5 = " ... ")
    b6 = len(b2)
    b7 = b2[0].shape
    b8 = np.zeros((b6, b7[0] * b7[1]), dtype=np.float32)
    for i, image in enumerate(b2):
        b8[i, :] = image.flatten()
    print("DONE")
    return b8
def fonk3(b8, b9 = 75):
    b10 = np.cov(b8, rowvar=False)
    print(f"Covariance matrix shape: {b10.shape}")
    b13, b11 = sl.eig(b10)
    b12 = b13.argsort()[::-1]
    b13 = b13[b12]
    b11 = b11[:, b12]
    b14 = b11[:, :b9].real
    print(f"Eigenvectors shape: {b14.shape}")
    return b13, b14
def fonk4(b11, image_vector):
    b15 = b11 @ image_vector
    b16 = b11.T @ b15
    return b16
def fonk5(image, b17 = 255):
    return image / b17
def fonk6():
    b18 = "GImagesTrain/GoodImages"
    b2 = fonk1(b18)
    b8 = fonk2(b2)
    _, b11 = fonk3(b8)
    b19 = b8[250]
    b20 = np.matrix(b19).transpose()
    b21 = b20.reshape(64, 64)
    print(f"Original image shape: {b21.shape}")
    b16 = fonk4(b11, b20)
    b16 = b16.reshape(64, 64)
    print(f"Reconstructed shape: {b16.shape}")
    b22 = fonk5(b16)
    b23 = fonk5(b21)
    plt.imshow(b22, b24 = 'gray')
    plt.title('Reconstructed Image')
    plt.show()
    plt.imshow(b23, b24 = 'gray')
    plt.title('Original Image')
    plt.show()
if b25 = = "__main__":
    fonk6()