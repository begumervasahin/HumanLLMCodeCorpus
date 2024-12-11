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
a1 = 101
a2 = 784
print("Hey!, We are using MNISt Data. So there are total 784 components.")
a3 = 784
b1 = np.zeros(shape=(28,28), dtype=int)
b2 = glob.glob("./data/processed/b18/train/0_*")
b3 = np.array([np.array(Image.open(fname)) for fname in b2])
print("Shape of original data ", b3.shape)
import matplotlib.pyplot as plt
plt.imshow(b3[ a1,:,:],b4 = 'gray')
plt.title('Original Image ( ' + str(a2) + ' b13) ')
plt.xlabel('b11 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg")
b3 = b3/float(255.0)
b5 = np.random.normal(0, .04,(b3.shape[0], b3.shape[1], b3.shape[2]))
b5 = b5.reshape(b3.shape[0], b3.shape[1], b3.shape[2])
b6 = b5 + b3
import matplotlib.pyplot as plt
plt.imshow(b6[ a1,:,:],b4 = 'gray')
plt.title('Noisy Image ( ' + str(a2) + ' b13) ')
plt.xlabel('b11 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg")
b7 = b6.ravel()
b7 = np.asarray(b7).reshape(b6.shape[0], b6.shape[1]*b6.shape[2])
print("Shape of flattened data ,",b7.shape)
b7 = b7
def fonk1(Data):
    b8 = np.zeros(shape=(Data.shape[1]),dtype = int)
    b9 = np.zeros(shape=(Data.shape[1]),dtype= int)
    for sample in Data:
        b8 = b8 + sample
    b9 = (b8)/int(Data.shape[0])
    return b9
def fonk2(eigenvalues, K):
    a4 = 0
    a5 = 0
    for i in b15 :
        a4 = a4 + pow(i,2)
        a5 = a5 + 1
        if a5 = = K:
            break
    return a4
b10 = fonk1(b7)
print("Shape of b10 vector ", b10.shape)
b11 = b7
b11 = b11 - b10
print("Shape of b11 ,", b11.shape)
b12 = np.matmul(b11.transpose(),b11   )
print("Shape of covariance matrix :", b12.shape)
b15, b13 = LA.eigh(b12)
print("Shape of eigen vectors ",b13.shape)
b14 = b15.argsort()[::-1]
b15 = b15[b14]
b13 = b13[:,b14]
print("Number of components in case 1", a3)
b13 = b13[:,:-(a2- (a3-1))]
b16 = np.matmul(b11 , b13)
b17 = np.matmul(b16, b13.transpose())
b17 = b17 + b10
b17 = b17.reshape(b3.shape[0],b3.shape[1],  b3.shape[2])
plt.imshow( b17[a1,:,:], b4 = 'gray')
plt.title('Reconstructed Image ( ' + str(a3) + ' b13)')
plt.xlabel('b11 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg")
b18 = [Image.open(x) for x in ['./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg', './Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg','./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_all_EVs.jpg']]
widths, b19 = zip(*(i.size for i in b18))
b20 = sum(widths)
b21 = max(b19)
b22 = Image.new('RGB', (b20, b21))
a6 = 0
for im in b18:
  b22.paste(im, (a6,0))
  a6 += im.size[0]
b22.show()
b22.save('./Results/PCAReconstruct_with_NoisyImages/PCA_all_EVs.jpg')
b23 = fonk2(b15, a2)
a7 = 0
b24 = []
b25 = []
for k in range(1,a2):
    b26 = fonk2(b15, k)
    b25.append(b26/ b23)
    b24.append(k)
    if b26/b23 >= 0.99 :
        a7 = k
        break
plt.close()
plt.title("Energy Graph")
plt.xlabel('Number of components (K)')
plt.ylabel('Ratio of Energy at K components to All components')
plt.plot(b24, b25 , b27 = 'number of components')
plt.legend()
plt.savefig('./Results/PCAReconstruct_with_NoisyImages/EnergyPlot.jpg')
plt.show()
print("Number of Top eigen vectors ", a7)
b13 = b13[:,:-(a2- (a7-1))]
b16 = np.matmul(b11 , b13)
b17 = np.matmul(b16, b13.transpose())
b17 = b17 + b10
b17 = b17.reshape(b3.shape[0],b3.shape[1],  b3.shape[2])
plt.imshow( b17[a1,:,:], b4 = 'gray')
plt.title('Reconstructed Image ( ' + str(a7) + ' b13)')
plt.xlabel('b11 axis')
plt.ylabel('Y axis')
plt.savefig("./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg")
b18 = [Image.open(x) for x in ['./Results/PCAReconstruct_with_NoisyImages/OriginalImage.jpg', './Results/PCAReconstruct_with_NoisyImages/NoisyImage.jpg','./Results/PCAReconstruct_with_NoisyImages/ReconstructImage_Effective_EVs.jpg']]
widths, b19 = zip(*(i.size for i in b18))
b20 = sum(widths)
b21 = max(b19)
b22 = Image.new('RGB', (b20, b21))
a6 = 0
for im in b18:
  b22.paste(im, (a6,0))
  a6 += im.size[0]
b22.show()
b22.save('./Results/PCAReconstruct_with_NoisyImages/PCA_Effective_EVs.jpg')