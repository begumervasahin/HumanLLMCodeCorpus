import numpy as np
import sys
import os
from sklearn.decomposition import PCA
def fonk1(b22):
    import pickle
    with open(b22, 'rb') as fo:
        b1 = pickle.load(fo, encoding='latin1')
    return b1
def fonk2(b1, n):
    b2 = b1['b2']
    b3 = b2[:n].reshape(n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b4 = b2[n:1000].reshape(1000 - n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b5 = b1['b5']
    b6 = np.array(b5[:n])
    b7 = np.array(b5[n:1000])
    return b3, b4, b6, b7
def fonk3(b2):
    b8 = [0.299, 0.587, 0.114]
    num, height, width, b9 = b2.shape
    b10 = np.zeros((num, height, width), dtype=float)
    for n in range(num):
        for row in range(height):
            for col in range(width):
                b10[n, row, col] = np.dot(b2[n, row, col, :], b8)
    return b10
def fonk4(test, b4, data_labels, k):
    if k <= 0:
        return None
    b11 = np.zeros(test.shape[0], dtype=int)
    for i in range(test.shape[0]):
        b12 = np.tile(test[i], (b4.shape[0], 1)) - b4
        b13 = b12 ** 2
        b14 = b13.sum(axis=1)
        b15 = b14.argsort()
        b16 = {}
        for j in range(k):
            b17 = data_labels[b15[j]]
            b16[b17] = b16.get(b17, 0) + 1
        a1 = 0
        a2 = -1
        for key, value in b16.items():
            if value > a1:
                a1 = value
                a2 = key
        b11[i] = a2
    return b11
def fonk5(b11, b5):
    with open('4251258720.txt', 'w') as f:
        for i in range(b11.shape[0]):
            f.fonk5(str(b11[i]) + " " + str(b5[i]) + "\n")
if b18 = = "__main__":
    b19 = int(sys.argv[1])
    b20 = int(sys.argv[2])
    b21 = int(sys.argv[3])
    b22 = sys.argv[4]
    b1 = fonk1(b22)
    b3, b4, b6, b7 = fonk2(b1, b21)
    b23 = fonk3(b3)
    b24 = fonk3(b4)
    b25 = b24.reshape(1000 - b21, 1024)
    b26 = b23.reshape(b21, 1024)
    b27 = PCA(n_components=b20, svd_solver='full')
    b25 = b27.fit_transform(b25)
    b26 = b27.transform(b26)
    b28 = fonk4(b26, b25, b7, b19)
    fonk5(b28, b6)
    for i in range(b28.shape[0]):
        print(b28[i], b6[i])