import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from numpy import linalg as LA
image_no = 101
Total_components = 784
number_of_components = 784
files = glob.glob("./data/processed/images/train/0_*")
OriginalData = np.array([np.array(Image.open(fname)) for fname in files])
plt.imshow(OriginalData[image_no], cmap='gray')
plt.title('Original Image ({} eigenVectors)'.format(Total_components))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
gauss = np.random.normal(0, .04, OriginalData.shape)
NoisyData = gauss + OriginalData / 255.0
plt.imshow(NoisyData[image_no], cmap='gray')
plt.title('Noisy Image ({} eigenVectors)'.format(Total_components))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg")
flat_arr = NoisyData.reshape(NoisyData.shape[0], -1)
mean_vector = np.mean(flat_arr, axis=0)
X = flat_arr - mean_vector
cov_mat = np.matmul(X.T, X)
eigenValues, eigenVectors = LA.eigh(cov_mat)
eigenVectors = eigenVectors[:, ::-1]
projected_data = np.matmul(X, eigenVectors)
reconstruct_data = np.matmul(projected_data, eigenVectors.T)
reconstruct_data = reconstruct_data + mean_vector
reconstruct_data = reconstruct_data.reshape(OriginalData.shape)
plt.imshow(reconstruct_data[image_no], cmap='gray')
plt.title('Reconstructed Image ({} eigenVectors)'.format(number_of_components))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
Total_Energy = np.sum(np.square(eigenValues))
Effective_numberOfComponents = np.argmax(np.cumsum(eigenValues) / Total_Energy >= 0.99) + 1
plt.close()
plt.title("Energy Graph")
plt.xlabel('Number of components (K)')
plt.ylabel('Ratio of Energy at K components to All components')
plt.plot(np.arange(1, Total_components), np.cumsum(eigenValues) / Total_Energy, label='number of components')
plt.legend()
plt.savefig('./Results/PCAReconstruct_with_NoisyImages/EnergyPlot.jpg')
plt.show()
projected_data = np.matmul(X, eigenVectors[:, :Effective_numberOfComponents])
reconstruct_data = np.matmul(projected_data, eigenVectors[:, :Effective_numberOfComponents].T)
reconstruct_data = reconstruct_data + mean_vector
reconstruct_data = reconstruct_data.reshape(OriginalData.shape)
plt.imshow(reconstruct_data[image_no], cmap='gray')
plt.title('Reconstructed Image ({} eigenVectors)'.format(Effective_numberOfComponents))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")