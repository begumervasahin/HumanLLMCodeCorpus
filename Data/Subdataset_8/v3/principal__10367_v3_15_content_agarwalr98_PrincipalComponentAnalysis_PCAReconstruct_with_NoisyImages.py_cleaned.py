import glob
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from PIL import Image
image_no = 101
Total_components = 784
print("Hey! We are using MNIST Data. So there are a total of 784 components.")
files = glob.glob("./data/processed/images/train/0_*")
OriginalData = np.array([np.array(Image.open(fname)) for fname in files])
print("Shape of original data:", OriginalData.shape)
plt.imshow(OriginalData[image_no,:,:], cmap='gray')
plt.title('Original Image')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
plt.show()
OriginalData = OriginalData / 255.0
noise = np.random.normal(0, 0.04, OriginalData.shape)
NoisyData = OriginalData + noise
plt.imshow(NoisyData[image_no,:,:], cmap='gray')
plt.title('Noisy Image')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg")
plt.show()
flat_arr = NoisyData.reshape(NoisyData.shape[0], -1)
print("Shape of flattened data:", flat_arr.shape)
mean_vector = np.mean(flat_arr, axis=0)
print("Shape of mean vector:", mean_vector.shape)
X = flat_arr - mean_vector
cov_mat = np.matmul(X.T, X)
print("Shape of covariance matrix:", cov_mat.shape)
eigenValues, eigenVectors = LA.eigh(cov_mat)
print("Shape of eigen vectors:", eigenVectors.shape)
sorted_indices = eigenValues.argsort()[::-1]
eigenValues = eigenValues[sorted_indices]
eigenVectors = eigenVectors[:,sorted_indices]
eigenVectors = eigenVectors[:,:Total_components]
projected_data = np.matmul(X, eigenVectors)
reconstruct_data = np.matmul(projected_data, eigenVectors.T)
reconstruct_data = reconstruct_data + mean_vector
reconstruct_data = reconstruct_data.reshape(OriginalData.shape)
plt.imshow(reconstruct_data[image_no,:,:], cmap='gray')
plt.title('Reconstructed Image')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
plt.show()
def cumulative_energy(eigenvalues, K):
    return np.sum(np.square(eigenvalues[:K]))
Total_Energy = cumulative_energy(eigenValues, Total_components)
Effective_numberOfComponents = 0
x_list = []
y_list = []
for k in range(1, Total_components):
    Energy_for_K = cumulative_energy(eigenValues, k)
    y_list.append(Energy_for_K / Total_Energy)
    x_list.append(k)
    if Energy_for_K / Total_Energy >= 0.99:
        Effective_numberOfComponents = k
        break
plt.plot(x_list, y_list, label='cumulative energy')
plt.title("Energy Graph")
plt.xlabel('Number of components (K)')
plt.ylabel('Cumulative Energy Ratio')
plt.legend()
plt.savefig('./Results/PCAReconstruct_with_NoisyImages/EnergyPlot.jpg')
plt.show()
print("Number of Top eigen vectors:", Effective_numberOfComponents)
eigenVectors = eigenVectors[:,:Effective_numberOfComponents]
projected_data = np.matmul(X, eigenVectors)
reconstruct_data = np.matmul(projected_data, eigenVectors.T)
reconstruct_data = reconstruct_data + mean_vector
reconstruct_data = reconstruct_data.reshape(OriginalData.shape)
plt.imshow(reconstruct_data[image_no,:,:], cmap='gray')
plt.title('Reconstructed Image')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")
plt.show()