import cv2
import os
import numpy as np
import scipy.linalg as sl
def readImages(dirName):
    matr = []
    for i,file in enumerate(os.listdir(dirName)):
        if i<3000:
            img = cv2.imread(str(dirName + "/" + file),0)
            img = cv2.resize(img, (64,64))
            matr.append(img)
    return matr
def createDataMatrix(images):
    print("Creating data matrix",end=" ... ")
    '''
    Allocate space for all images in one data matrix.
        The size of the data matrix is
        ( w  * h  * 3, numImages )
        where,
        w = width of an image in the dataset.
        h = height of an image in the dataset.
        3 is for the 3 color channels.
        '''
    numImages = len(images)
    sz = images[0].shape
    data = np.zeros((numImages, sz[0] * sz[1]), dtype=np.float32)
    for i in range(0, numImages):
        image = images[i].flatten()
        data[i,:] = image
    print("DONE")
    return data
dirName = "GImagesTrain/GoodImages"
images = readImages(dirName)
sz = images[0].shape
data = createDataMatrix(images)
sigm = np.cov(data, rowvar = False)
print(sigm.shape)
eigenValues, u = sl.eig(sigm)
idx = eigenValues.argsort()[::-1]
eigenValues = eigenValues[idx]
u = u[:,idx]
x = data[250]
x = np.matrix(x)
x = x.transpose()
ims = x.reshape(64, 64)
ims = np.array(ims)
print(ims.shape)
u = u.transpose()
eigenvectors = u[:75].real
print(eigenvectors.shape)
z = eigenvectors*x
print(z.shape)
reconstucted = np.matmul(eigenvectors.transpose(),z)
recons = reconstucted.reshape(64,64)
print(reconstucted.shape)
import matplotlib.pyplot as plt
recons /= 255
ims /= 255
print(recons)
plt.imshow(recons)
plt.show()
plt.imshow(ims)
plt.show()