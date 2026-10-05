import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from numpy import linalg as LA
a1 = 101
a2 = 784
a3 = 784
b1 = glob.glob("./data/processed/images/train/0_*")
b2 = np.array([np.array(Image.open(fname)) for fname in b1])
plt.imshow(b2[a1], b3 = 'gray')
plt.title('Original Image ({} b10)'.format(a2))
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
b4 = np.random.normal(0, .04, b2.shape)
b5 = b4 + b2 / 255.0
plt.imshow(b5[a1], b3 = 'gray')
plt.title('Noisy Image ({} b10)'.format(a2))
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg")
b6 = b5.reshape(b5.shape[0], -1)
b7 = np.mean(b6, axis=0)
b8 = b6 - b7
b9 = np.matmul(b8.T, b8)
eigenValues, b10 = LA.eigh(b9)
b10 = b10[:, ::-1]
b11 = np.matmul(b8, b10)
b12 = np.matmul(b11, b10.T)
b12 = b12 + b7
b12 = b12.reshape(b2.shape)
plt.imshow(b12[a1], b3 = 'gray')
plt.title('Reconstructed Image ({} b10)'.format(a3))
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
b13 = np.sum(np.square(eigenValues))
b14 = np.argmax(np.cumsum(eigenValues) / b13 >= 0.99) + 1
plt.close()
plt.title("Energy Graph")
plt.xlabel('Number of components (K)')
plt.ylabel('Ratio of Energy at K components to All components')
plt.plot(np.arange(1, a2), np.cumsum(eigenValues) / b13, b15 = 'number of components')
plt.legend()
plt.savefig('./Results/PCAReconstruct_with_NoisyImages/EnergyPlot.jpg')
plt.show()
b11 = np.matmul(b8, b10[:, :b14])
b12 = np.matmul(b11, b10[:, :b14].T)
b12 = b12 + b7
b12 = b12.reshape(b2.shape)
plt.imshow(b12[a1], b3 = 'gray')
plt.title('Reconstructed Image ({} b10)'.format(b14))
plt.xlabel('b8 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")