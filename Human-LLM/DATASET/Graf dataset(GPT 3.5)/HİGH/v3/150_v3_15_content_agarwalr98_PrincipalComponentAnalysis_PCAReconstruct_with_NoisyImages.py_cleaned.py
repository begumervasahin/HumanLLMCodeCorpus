import glob
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from PIL import Image
a1 = 101
a2 = 784
print("Hey! We are using MNIST Data. So there are a total of 784 components.")
b1 = glob.glob("./data/processed/images/train/0_*")
b2 = np.array([np.array(Image.open(fname)) for fname in b1])
print("Shape of original data:", b2.shape)
plt.imshow(b2[a1,:,:], b3 = 'gray')
plt.title('Original Image')
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
plt.show()
b2 = b2 / 255.0
b4 = np.random.normal(0, 0.04, b2.shape)
b5 = b2 + b4
plt.imshow(b5[a1,:,:], b3 = 'gray')
plt.title('Noisy Image')
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
b10 = b10[:,:a2]
b13 = np.matmul(b8, b10)
b14 = np.matmul(b13, b10.T)
b14 = b14 + b7
b14 = b14.reshape(b2.shape)
plt.imshow(b14[a1,:,:], b3 = 'gray')
plt.title('Reconstructed Image')
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
plt.show()
def fonk1(eigenvalues, K):
    return np.sum(np.square(eigenvalues[:K]))
b15 = fonk1(b12, a2)
a3 = 0
b16 = []
b17 = []
for k in range(1, a2):
    b18 = fonk1(b12, k)
    b17.append(b18 / b15)
    b16.append(k)
    if b18 / b15 >= 0.99:
        a3 = k
        break
plt.plot(b16, b17, b19 = 'cumulative energy')
plt.title("Energy Graph")
plt.xlabel('Number of components (K)')
plt.ylabel('Cumulative Energy Ratio')
plt.legend()
plt.savefig('./Results/PCAReconstruct_with_NoisyImages/EnergyPlot.jpg')
plt.show()
print("Number of Top eigen vectors:", a3)
b10 = b10[:,:a3]
b13 = np.matmul(b8, b10)
b14 = np.matmul(b13, b10.T)
b14 = b14 + b7
b14 = b14.reshape(b2.shape)
plt.imshow(b14[a1,:,:], b3 = 'gray')
plt.title('Reconstructed Image')
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")
plt.show()