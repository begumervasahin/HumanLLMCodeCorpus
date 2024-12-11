import sys
from PIL import Image
import glob
import cv2
import random
import numpy as np
import pandas as pd
from numpy import linalg as LA
import matplotlib.pyplot as plt
a1 = 101
a2 = 784
a3 = 784
print("Hey!, We are using MNIST Data. So there are total 784 components.")
b1 = glob.glob("./data/processed/images/train/0_*")
b2 = np.array([np.array(Image.open(fname)) for fname in b1])
print("Shape of original data:", b2.shape)
plt.imshow(b2[a1,:,:], b3 = 'gray')
plt.title('Original Image (' + str(a2) + ' b10)')
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
plt.show()
b2 = b2 / float(255.0)
b4 = np.random.normal(0, .04, b2.shape)
b5 = b4 + b2
plt.imshow(b5[a1,:,:], b3 = 'gray')
plt.title('Noisy Image (' + str(a2) + ' b10)')
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg")
plt.show()
b6 = b5.reshape(b5.shape[0], -1)
print("Shape of flattened data:", b6.shape)
b7 = np.mean(b6, axis=0)
print("Shape of mean vector:", b7.shape)
b8 = b6 - b7
b9 = np.matmul(b8.T, b8)
print("Shape of covariance matrix:", b9.shape)
b12, b10 = LA.eigh(b9)
print("Shape of eigen vectors:", b10.shape)
b11 = b12.argsort()[::-1]
b12 = b12[b11]
b10 = b10[:,b11]
b10 = b10[:,:-(a2 - (a3 - 1))]
b13 = np.matmul(b8, b10)
b14 = np.matmul(b13, b10.T)
b14 = b14 + b7
b14 = b14.reshape(b2.shape)
plt.imshow(b14[a1,:,:], b3 = 'gray')
plt.title('Reconstructed Image (' + str(a3) + ' b10)')
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
plt.show()
def fonk1(eigenvalues, K):
    b15 = np.sum(np.square(eigenvalues[:K]))
    return b15
b16 = fonk1(b12, a2)
a4 = 0
b17 = []
b18 = []
for k in range(1, a2):
    b19 = fonk1(b12, k)
    b18.append(b19 / b16)
    b17.append(k)
    if b19 / b16 >= 0.99:
        a4 = k
        break
plt.plot(b17, b18, b20 = 'number of components')
plt.title("Energy Graph")
plt.xlabel('Number of components (K)')
plt.ylabel('Ratio of Energy at K components to All components')
plt.legend()
plt.savefig('./Results/PCAReconstruct_with_NoisyImages/EnergyPlot.jpg')
plt.show()
print("Number of Top eigen vectors:", a4)
b10 = b10[:,:-(a2 - (a4 - 1))]
b13 = np.matmul(b8, b10)
b14 = np.matmul(b13, b10.T)
b14 = b14 + b7
b14 = b14.reshape(b2.shape)
plt.imshow(b14[a1,:,:], b3 = 'gray')
plt.title('Reconstructed Image (' + str(a4) + ' b10)')
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")
plt.show()