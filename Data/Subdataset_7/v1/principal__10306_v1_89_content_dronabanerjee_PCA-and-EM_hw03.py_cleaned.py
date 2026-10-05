import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import skimage.filters as filt
from numpy import linalg as LA
from sklearn.preprocessing import StandardScaler
def fonk1(b35, a5, a6, a7):
    a1 = 20
    b1 = b35.shape[0]
    b2 = (a5*(1-a6))/((a5*(1-a6)) + (1-a5)*(1-a7))
    b3 = (a5*a6)/((a5*a6) + (1-a5)*a7)
    a2 = 0
    a3 = 0
    for i in range(b1):
        if b35[i] == 0:
            a2 = a2 + b2
        else:
            a2 = a2 + b3
    a3 = a2/b1
    print("\nTheta(0) values are:")
    print("Pie(0)=", a5)
    print("a6(0)=", a6)
    print("a7(0)=", a7)
    print("\nFor all values of observable b4 = 0:")
    print("mu(1)=", b2)
    print("For all values of observable b4 = 1:")
    print("mu(1)=", b3, "\n")
    print("Mean mu(1)=", a3, "\n")
    a4 = 1
    while a4 <= a1:
        a5 = 0
        a6 = 0
        a7 = 0
        print("Iteration number: ", a4)
        for j in range(b1):
            if b35[j] == 0:
                a5 = a5 + b2
            else:
                a5 = a5 + b3
        a5 = a5/10
        print("Pie(",a4,")=",a5)
        a8 = 0
        a9 = 0
        for j in range(b1):
            if b35[j] == 1:
                a8 = a8 + b3
                a9 = a9 + b3
            else:
                a9 = a9 + b2
        a6 = a8/a9
        print("a6(",a4,")=",a6)
        a10 = 0
        a11 = 0
        for j in range(b1):
            if b35[j] == 1:
                a10 = a10 + (1-b3)
                a11 = a11 + (1-b3)
            else:
                a11 = a11 + (1-b2)
        a7 = a10/a11
        print("a7(",a4,")=",a7)
        b2 = (a5*(1-a6))/((a5*(1-a6)) + (1-a5)*(1-a7))
        b3 = (a5*a6)/((a5*a6) + (1-a5)*a7)
        a2 = 0
        a3 = 0
        for i in range(b1):
            if b35[i] == 0:
                a2 = a2 + b2
            else:
                a2 = a2 + b3
        a3 = a2/b1
        print("\nFor all values of observable b4 = 0:")
        print("mu(",a4+1,")=",b2)
        print("For all values of observable b4 = 1:")
        print("mu(",a4+1,")=",b3,"\n")
        print("Mean mu(",a4+1,")=",a3,"\n")
        a4 = a4 + 1
def fonk2(in_fname, b5 = False):
    b6 = np.array(Image.open(in_fname))
    b7 = 1.0 - rgb2gray(b6)
    if b5:
        plt.figure(1)
        plt.imshow(b7)
        plt.title('original grayscale image')
        plt.show()
    b8 = filt.threshold_minimum(b7)
    b9 = b7 > b8
    if b5:
        plt.figure(2)
        plt.imshow(b9)
        plt.title('binarized image')
        plt.show()
    nz_r, b10 = b9.nonzero()
    n_r, b11 = b9.shape
    l, b12 = max(0, min(b10) - 1), min(b11 - 1, max(b10) + 1) + 1
    t, b13 = max(0, min(nz_r) - 1), min(n_r - 1, max(nz_r) + 1) + 1
    b14 = b9[t:b13, l:b12]
    if b5:
        plt.figure(3)
        plt.imshow(b14)
        plt.title('windowed image')
        plt.show()
    b15 = max(b14.shape)
    b16 = int(round(b14.shape[0] / b15 * 48))
    b17 = int(round(b14.shape[1] / b15 * 48))
    b18 = Image.fromarray(b14.astype(np.uint8) * 255)
    b19 = b18.resize((b17, b16))
    b20 = np.array(b19).astype(bool)
    b21 = np.zeros((b20.shape[0] + 2, b20.shape[1] + 2), dtype=bool)
    b21[1:-1, 1:-1] = b20
    if b5:
        plt.figure(4)
        plt.imshow(b21, b22 = 'Greys')
        plt.title('resized windowed image')
        plt.show()
    return b21
if b23 = = '__main__':
    b24 = np.array([(2,3,3,4,5,7), (2,4,5,5,6,8)])
    b25 = StandardScaler()
    b26 = b25.fit_transform(b24.T)
    b26 = b26.T
    b27 = np.cov(b26)
    w, b28 = LA.eig(b24.T@b24)
    w1, b29 = LA.eig(b24@b24.T)
    w2, b30 = LA.eig(b27)
    b31 = [(np.abs(w2[i]), b30[:,i]) for i in range(len(w2))]
    b31.sort(b32 = True)
    b33 = b31[0][1][:, np.newaxis]
    b34 = b26.T.dot(b33)
    b34 = b34.T
    print ("*****PCA*******\n")
    print ("Question 1")
    print ("\nEigen values of b24.T@b24 are:")
    print (w)
    print ("\n")
    print ("Question 2\n")
    print ("Eigenvalues of b24@b24.T are:")
    print (w1)
    print ("\n")
    print ("Eigenvectors of b24@b24.T are:")
    print (b29)
    print ("\n")
    print ("Question 4\n")
    print('Shape of transformed b4:\n', b34.shape)
    print('\nTransformed b4 after dimension reduction:\n', b34)
    print ("\n*****EM*******")
    b35 = np.array([1, 1, 0, 1, 0, 0, 1,
0, 1, 1, 0, 1, 1])
fonk1(b35, 0.4, 0.6, 0.7)
print("\n\n")
fonk1(b35, 0.5, 0.5, 0.5)