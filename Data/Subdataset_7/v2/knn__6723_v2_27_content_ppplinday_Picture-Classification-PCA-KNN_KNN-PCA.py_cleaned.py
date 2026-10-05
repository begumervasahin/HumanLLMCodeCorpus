import numpy as np
import sys
from sklearn.decomposition import PCA
import os
def fonk1(b16):
    import pickle
    with open(b16, 'rb') as fo:
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
    return np.dot(b2[..., :3], [0.299, 0.587, 0.114])
def fonk4(test, b4, data_labels, k):
    b8 = np.zeros([test.shape[0]], int)
    for i in range(test.shape[0]):
        b9 = np.tile(test[i], (b4.shape[0], 1)) - b4
        b10 = b9 ** 2
        b11 = b10.sum(axis=1)
        b12 = b11.argsort()
        b13 = {}
        for j in range(k):
            b14 = data_labels[b12[j]]
            b13[b14] = b13.get(b14, 0) + 1
        a1 = 0
        a2 = -1
        for key in b13:
            if b13[key] > a1:
                a1 = b13[key]
                a2 = key
        b8[i] = a2
    return b8
def fonk5(pred, b5):
    with open('4251258720.txt', 'w') as f:
        for i in range(pred.shape[0]):
            f.fonk5(str(pred[i]) + " " + str(b5[i]) + "\n")
if b15 = = "__main__":
    K, D, N, b16 = map(int, sys.argv[1:])
    b1 = fonk1(b16)
    b3, b4, b6, b7 = fonk2(b1, N)
    b17 = fonk3(b3)
    b18 = fonk3(b4)
    b19 = b18.reshape(1000 - N, 1024)
    b20 = b17.reshape(N, 1024)
    b21 = PCA(n_components=D, svd_solver='full')
    b19 = b21.fit_transform(b19)
    b20 = b21.transform(b20)
    b22 = fonk4(b20, b19, b7, K)
    fonk5(b22, b6)
    for i in range(b22.shape[0]):
        print(b22[i], b6[i])