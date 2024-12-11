import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.color import rgb2gray
import skimage.filters as filt
from numpy import linalg as LA
from sklearn.preprocessing import StandardScaler
def fonk1(b45, b8, b11, b14):
    a1 = 20
    b1 = len(b45)
    b2 = (b8*(1-b11))/((b8*(1-b11)) + (1-b8)*(1-b14))
    b3 = (b8*b11)/((b8*b11) + (1-b8)*b14)
    b4 = sum(b2 if y == 0 else b3 for y in b45)
    b5 = b4 / b1
    print("\nTheta(0) values are:")
    print("Pie(0)=", b8)
    print("b11(0)=", b11)
    print("b14(0)=", b14)
    print("\nFor all values of observable b6 = 0:")
    print("mu(1)=", b2)
    print("For all values of observable b6 = 1:")
    print("mu(1)=", b3, "\n")
    print("Mean mu(1)=", b5, "\n")
    a2 = 1
    while a2 <= a1:
        b7 = sum(b2 if y == 0 else b3 for y in b45)
        b8 = b7 / 10
        print("Iteration number: ", a2)
        print("Pie(", a2, ")=", b8)
        b9 = sum(b3 for y in b45 if y == 1)
        b10 = sum(b3 if y == 1 else b2 for y in b45)
        b11 = b9 / b10
        print("b11(", a2, ")=", b11)
        b12 = sum(1-b3 for y in b45 if y == 1)
        b13 = sum(1-b3 if y == 1 else 1-b2 for y in b45)
        b14 = b12 / b13
        print("b14(", a2, ")=", b14)
        b2 = (b8*(1-b11))/((b8*(1-b11)) + (1-b8)*(1-b14))
        b3 = (b8*b11)/((b8*b11) + (1-b8)*b14)
        b4 = sum(b2 if y == 0 else b3 for y in b45)
        b5 = b4 / b1
        print("\nFor all values of observable b6 = 0:")
        print("mu(", a2+1, ")=", b2)
        print("For all values of observable b6 = 1:")
        print("mu(", a2+1, ")=", b3, "\n")
        print("Mean mu(", a2+1, ")=", b5, "\n")
        a2 += 1
def fonk2(in_fname, b15 = False):
    b16 = np.array(Image.open(in_fname))
    b17 = 1.0 - rgb2gray(b16)
    if b15:
        plt.figure(1)
        plt.imshow(b17)
        plt.title('original grayscale image')
        plt.show()
    b18 = filt.threshold_minimum(b17)
    b19 = b17 > b18
    if b15:
        plt.figure(2)
        plt.imshow(b19)
        plt.title('binarized image')
        plt.show()
    nz_r, b20 = b19.nonzero()
    n_r, b21 = b19.shape
    l, b22 = max(0, min(b20)-1), min(b21-1, max(b20)+1)+1
    t, b23 = max(0, min(nz_r)-1), min(n_r-1, max(nz_r)+1)+1
    b24 = b19[t:b23, l:b22]
    if b15:
        plt.figure(3)
        plt.imshow(b24)
        plt.title('windowed image')
        plt.show()
    b25 = max(b24.shape)
    b26 = int(round(b24.shape[0]/b25*48))
    b27 = int(round(b24.shape[1]/b25*48))
    b28 = Image.fromarray(b24.astype(np.uint8)*255)
    b29 = b28.resize((b27, b26))
    b30 = np.array(b29).astype(bool)
    b31 = np.zeros((b30.shape[0]+2, b30.shape[1]+2), dtype=bool)
    b31[1:-1, 1:-1] = b30
    if b15:
        plt.figure(4)
        plt.imshow(b31, b32 = 'Greys')
        plt.title('resized windowed image')
        plt.show()
    return b31
if b33 = = '__main__':
    b34 = np.array([(2,3,3,4,5,7), (2,4,5,5,6,8)])
    b35 = StandardScaler()
    b36 = b35.fit_transform(b34.T)
    b36 = b36.T
    b37 = np.cov(b36)
    w, b38 = LA.eig(b34.T@b34)
    w1, b39 = LA.eig(b34@b34.T)
    w2, b40 = LA.eig(b37)
    b41 = [(np.abs(w2[i]), b40[:,i]) for i in range(len(w2))]
    b41.sort(b42 = True)
    b43 = b41[0][1][:, np.newaxis]
    b44 = b36.T.dot(b43)
    b44 = b44.T
    print ("*****PCA*******\n")
    print ("Question 1")
    print ("\nEigen values of b34.T@b34 are:")
    print (w)
    print ("\n")
    print ("Question 2\n")
    print ("Eigenvalues of b34@b34.T are:")
    print (w1)
    print ("\n")
    print ("Eigenvectors of b34@b34.T are:")
    print (b39)
    print ("\n")
    print ("Question 4\n")
    print('Shape of transformed b6:\n', b44.shape)
    print('\nTransformed b6 after dimension reduction:\n', b44)
    print ("\n*****EM*******")
    b45 = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1])
    fonk1(b45, 0.4, 0.6, 0.7)
    print("\n\n")
    fonk1(b45, 0.5, 0.5, 0.5)