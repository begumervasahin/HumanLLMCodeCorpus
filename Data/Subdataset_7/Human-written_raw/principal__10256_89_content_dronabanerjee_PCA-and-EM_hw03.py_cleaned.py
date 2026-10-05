
import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import skimage.filters as filt
from numpy import linalg as LA
from sklearn.preprocessing import StandardScaler
def fonk1(b28, a5, a6, a7):
    a1 = 20
    b1 = b28.shape[0]
    b2 = (a5*(1-a6))/((a5*(1-a6)) + (1-a5)*(1-a7))
    b3 = (a5*a6)/((a5*a6) + (1-a5)*a7)
    a2 = 0
    a3 = 0
    for i in range(b1):
        if b28[i] == 0:
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
            if b28[j] == 0:
                a5 = a5 + b2
            else:
                a5 = a5 + b3
        a5 = a5/10
        print("Pie(",a4,")=",a5)
        a8 = 0
        a9 = 0
        for j in range(b1):
            if b28[j] == 1:
                a8 = a8 + b3
                a9 = a9 + b3
            else:
                a9 = a9 + b2
        a6 = a8/a9
        print("a6(",a4,")=",a6)
        a10 = 0
        a11 = 0
        for j in range(b1):
            if b28[j] == 1:
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
            if b28[i] == 0:
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
def fonk2(in_fname,b5 = False):
    b6 = np.array(Image.open(in_fname))
    b7 = 1.0-rgb2gray(b6)
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
    nz_r,b10 = b9.nonzero()
    n_r,b11 = b9.shape
    l,b12 = max(0,min(b10)-1),min(b11-1,max(b10)+1)+1
    t,b13 = max(0,min(nz_r)-1),min(n_r-1,max(nz_r)+1)+1
    b14 = b9[t:b13,l:b12]
    if b5:
        plt.figure(3)
        plt.imshow(b14)
        plt.title('windowed image')
        plt.show()
    b15 = max(b14.shape)
    b16 = int(round(b14.shape[0]/b15*48))
    b17 = int(round(b14.shape[1]/b15*48))
    b18 = Image.fromarray(b14.astype(np.uint8)*255)
    b19 = b18.resize((b17,b16))
    b20 = np.array(b19).astype(bool)
    b21 = np.zeros((b20.shape[0]+2,b20.shape[1]+2),dtype=bool)
    b21[1:-1,1:-1] = b20
    if b5:
        plt.figure(4)
        plt.imshow(b21,b22 = 'Greys')
        plt.title('resized windowed image')
        plt.show()
    return b21
if b23 = = '__main__':
    """
    ***************Code to generate b4 for assignment 3C*********************
    b24 = []
    for i in range(1, 81):
        b25 = fonk2('C:\\Users\\user\\Desktop\\MS\\Fall_2019\\FML\\ass3\\3C\\{}.jpeg'.format(i),b5=False)
        b24.append(b25)
    b24 = np.asarray(b24)
    np.save('b4.npy',b24)
    b4 = np.load('b4.npy', allow_pickle =True)
    print("Shape of b4.npy is:\n", b4.shape)
    b26 = np.arange(80)
    for i in range(80):
        if i>=0 and i<=9:
            b26[i] = 1
        if i>=10 and i<=19:
            b26[i] = 2
        if i>=20 and i<=29:
            b26[i] = 3
        if i>=30 and i<=39:
            b26[i] = 4
        if i>=40 and i<=49:
            b26[i] = 5
        if i>=50 and i<=59:
            b26[i] = 6
        if i>=60 and i<=69:
            b26[i] = 7
        if i>=70 and i<=79:
            b26[i] = 8
    np.save('b26.npy',b26)
    b26 = np.load('b26.npy', allow_pickle =True)
    print("\nShape of b26.npy is:\n", b26.shape)
    print ("v:\n",X_std)
    print ("\n\n")
    print ("sd of X: \n",np.std(X, b27 = 1))
    """
    print ("*****PCA*******\n")
    print ("Question 1")
    print ("\nEigen values of X.T@X are:")
    print (w)
    print ("\n")
    print ("Question 2\n")
    print ("Eigenvalues of X@X.T are:")
    print (w1)
    print ("\n")
    print ("Eigenvectors of X@X.T are:")
    print (v1)
    print ("\n")
    print ("Question 4\n")
    print('Shape of transformed b4:\n', X_pca.shape)
    print('\nTransformed b4 after dimension reduction:\n', X_pca)
    print ("\n*****EM*******")
    b28 = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1])
    fonk1(b28, 0.4, 0.6, 0.7)
    print("\n\n")
    fonk1(b28, 0.5, 0.5, 0.5)