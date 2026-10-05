import sys
from PIL import Image
import glob
import cv2
import random
import numpy as np
import pandas as pd
import struct
from numpy import linalg as LA
import matplotlib
import matplotlib.pyplot as plt
image_no = 101
Total_components = 784
print("Hey!, We are using MNISt Data. So there are total 784 components.")
number_of_components = 784
X_data = np.zeros(shape=(28,28), dtype=int)
files = glob.glob("./data/processed/images/train/0_*")
OriginalData = np.array([np.array(Image.open(fname)) for fname in files])
print("Shape of original data ", OriginalData.shape)
import matplotlib.pyplot as plt
plt.imshow(OriginalData[ image_no,:,:],cmap='gray')
plt.title('Original Image ( ' + str(Total_components) + ' eigenVectors) ')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
OriginalData = OriginalData/float(255.0)
gauss = np.random.normal(0, .04,(OriginalData.shape[0], OriginalData.shape[1], OriginalData.shape[2]))
gauss = gauss.reshape(OriginalData.shape[0], OriginalData.shape[1], OriginalData.shape[2])
NoisyData = gauss + OriginalData
import matplotlib.pyplot as plt
plt.imshow(NoisyData[ image_no,:,:],cmap='gray')
plt.title('Noisy Image ( ' + str(Total_components) + ' eigenVectors) ')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg")
flat_arr = NoisyData.ravel()
flat_arr = np.asarray(flat_arr).reshape(NoisyData.shape[0], NoisyData.shape[1]*NoisyData.shape[2])
print("Shape of flattened data ,",flat_arr.shape)
flat_arr = flat_arr
def mean(Data):
    sum_vector = np.zeros(shape=(Data.shape[1]),dtype = int)
    mean_vector = np.zeros(shape=(Data.shape[1]),dtype= int)
    for sample in Data:
        sum_vector = sum_vector + sample
    mean_vector = (sum_vector)/int(Data.shape[0])
    return mean_vector
def Energy(eigenvalues, K):
    EnergyValue = 0
    count = 0
    for i in eigenValues :
        EnergyValue = EnergyValue + pow(i,2)
        count = count + 1
        if count == K:
            break
    return EnergyValue
mean = mean(flat_arr)
print("Shape of mean vector ", mean.shape)
X = flat_arr
X = X - mean
print("Shape of X ,", X.shape)
cov_mat = np.matmul(X.transpose(),X   )
print("Shape of covariance matrix :", cov_mat.shape)
eigenValues, eigenVectors = LA.eigh(cov_mat)
print("Shape of eigen vectors ",eigenVectors.shape)
index = eigenValues.argsort()[::-1]
eigenValues = eigenValues[index]
eigenVectors = eigenVectors[:,index]
print("Number of components in case 1", number_of_components)
eigenVectors = eigenVectors[:,:-(Total_components- (number_of_components-1))]
projected_data = np.matmul(X , eigenVectors)
reconstruct_data  =np.matmul(projected_data, eigenVectors.transpose())
reconstruct_data = reconstruct_data + mean
reconstruct_data = reconstruct_data.reshape(OriginalData.shape[0],OriginalData.shape[1],  OriginalData.shape[2])
plt.imshow( reconstruct_data[image_no,:,:], cmap='gray')
plt.title('Reconstructed Image ( ' + str(number_of_components) + ' eigenVectors)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
images = [Image.open(x) for x in ['./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg', './Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg','./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg']]
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)
new_im = Image.new('RGB', (total_width, max_height))
x_offset =0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]
new_im.show()
new_im.save('./Results/PCAReconstruct_with_NoisyImages/PCA_all_EVs.jpg')
Total_Energy = Energy(eigenValues, Total_components)
Effective_numberOfComponents = 0
x_list = []
y_list = []
for k in range(1,Total_components):
    Energy_for_K = Energy(eigenValues, k)
    y_list.append(Energy_for_K/ Total_Energy)
    x_list.append(k)
    if Energy_for_K/Total_Energy >= 0.99 :
        Effective_numberOfComponents = k
        break
plt.close()
plt.title("Energy Graph")
plt.xlabel('Number of components (K)')
plt.ylabel('Ratio of Energy at K components to All components')
plt.plot(x_list, y_list , label='number of components')
plt.legend()
plt.savefig('./Results/PCAReconstruct_with_NoisyImages/EnergyPlot.jpg')
plt.show()
print("Number of Top eigen vectors ", Effective_numberOfComponents)
eigenVectors = eigenVectors[:,:-(Total_components- (Effective_numberOfComponents-1))]
projected_data = np.matmul(X , eigenVectors)
reconstruct_data  =np.matmul(projected_data, eigenVectors.transpose())
reconstruct_data = reconstruct_data + mean
reconstruct_data = reconstruct_data.reshape(OriginalData.shape[0],OriginalData.shape[1],  OriginalData.shape[2])
plt.imshow( reconstruct_data[image_no,:,:], cmap='gray')
plt.title('Reconstructed Image ( ' + str(Effective_numberOfComponents) + ' eigenVectors)')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")
images = [Image.open(x) for x in ['./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg', './Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg','./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg']]
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)
new_im = Image.new('RGB', (total_width, max_height))
x_offset =0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]
new_im.show()
new_im.save('./Results/PCAReconstruct_with_NoisyImages/PCA_Effective_EVs.jpg')