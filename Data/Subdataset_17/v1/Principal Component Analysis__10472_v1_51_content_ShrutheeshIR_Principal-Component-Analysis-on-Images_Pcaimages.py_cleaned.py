import cv2
import os
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt
def readImages(dirName):
    matr = []
    for i, file in enumerate(os.listdir(dirName)):
        if i < 3000:
            img = cv2.imread(os.path.join(dirName, file), 0)
            img = cv2.resize(img, (64, 64))
            matr.append(img)
    return matr
def createDataMatrix(images):
    print("Creating data matrix", end=" ... ")
    numImages = len(images)
    sz = images[0].shape
    data = np.zeros((numImages, sz[0] * sz[1]), dtype=np.float32)
    for i in range(numImages):
        image = images[i].flatten()
        data[i, :] = image
    print("DONE")
    return data
dirName = "GImagesTrain/GoodImages"
images = readImages(dirName)
data = createDataMatrix(images)
sigm = np.cov(data, rowvar=False)
print(f"Covariance matrix shape: {sigm.shape}")
eigenValues, u = sl.eig(sigm)
idx = eigenValues.argsort()[::-1]
eigenValues = eigenValues[idx]
u = u[:, idx]
x = data[250]
x = np.matrix(x).transpose()
ims = x.reshape(64, 64)
ims = np.array(ims)
print(f"Original image shape: {ims.shape}")
u = u.transpose()
eigenvectors = u[:75].real
print(f"Eigenvectors shape: {eigenvectors.shape}")
z = eigenvectors @ x
print(f"Projected shape: {z.shape}")
reconstructed = np.matmul(eigenvectors.transpose(), z)
recons = reconstructed.reshape(64, 64)
print(f"Reconstructed shape: {reconstructed.shape}")
recons /= 255
ims /= 255
plt.imshow(recons, cmap='gray')
plt.title('Reconstructed Image')
plt.show()
plt.imshow(ims, cmap='gray')
plt.title('Original Image')
plt.show()