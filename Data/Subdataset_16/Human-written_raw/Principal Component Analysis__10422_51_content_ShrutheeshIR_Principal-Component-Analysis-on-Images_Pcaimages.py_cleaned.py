import cv2
import os
import numpy as np
import scipy.linalg as sl
def fonk1(b10):
    b1 = []
    for i,file in enumerate(os.listdir(b10)):
        if i<3000:
            b2 = cv2.imread(str(b10 + "/" + file),0)
            b2 = cv2.resize(b2, (64,64))
            b1.append(b2)
    return b1
def fonk2(b11):
    print("Creating b8 matrix",b3 = " ... ")
    '''
    Allocate space for all b11 in one b8 matrix.
        The size of the b8 matrix is
        ( b4  * b5  * 3, b6 )
        where,
        b4 = width of an b9 in the dataset.
        b5 = height of an b9 in the dataset.
        3 is for the 3 color channels.
        '''
    b6 = len(b11)
    b7 = b11[0].shape
    b8 = np.zeros((b6, b7[0] * b7[1]), dtype=np.float32)
    for i in range(0, b6):
        b9 = b11[i].flatten()
        b8[i,:] = b9
    print("DONE")
    return b8
b10 = "GImagesTrain/GoodImages"
b11 = fonk1(b10)
b7 = b11[0].shape
b8 = fonk2(b11)
b12 = np.cov(b8, rowvar = False)
print(b12.shape)
b15, b13 = sl.eig(b12)
b14 = b15.argsort()[::-1]
b15 = b15[b14]
b13 = b13[:,b14]
b16 = b8[250]
b16 = np.matrix(b16)
b16 = b16.transpose()
b17 = b16.reshape(64, 64)
b17 = np.array(b17)
print(b17.shape)
b13 = b13.transpose()
b18 = b13[:75].real
print(b18.shape)
b19 = b18*b16
print(b19.shape)
b20 = np.matmul(b18.transpose(),b19)
b21 = b20.reshape(64,64)
print(b20.shape)
import matplotlib.pyplot as plt
b21 /= 255
b17 /= 255
print(b21)
plt.imshow(b21)
plt.show()
plt.imshow(b17)
plt.show()