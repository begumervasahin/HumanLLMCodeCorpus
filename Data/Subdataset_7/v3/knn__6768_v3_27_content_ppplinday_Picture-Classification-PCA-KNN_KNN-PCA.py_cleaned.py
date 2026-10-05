import numpy as np
import sys
from sklearn.decomposition import PCA
import os
import pickle
def fonk1(b14):
    with open(b14, 'rb') as fo:
        return pickle.load(fo, b1 = 'latin1')
def fonk2(data, labels, n):
    b2 = data[:n].reshape(n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b3 = data[n:1000].reshape(1000 - n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b4 = np.array(labels[:n])
    b5 = np.array(labels[n:1000])
    return b2, b3, b4, b5
def fonk3(data):
    return np.dot(data[..., :3], [0.299, 0.587, 0.114])
def fonk4(test, b3, data_labels, k):
    b6 = np.zeros([test.shape[0]], int)
    for i in range(test.shape[0]):
        b7 = np.tile(test[i], (b3.shape[0], 1)) - b3
        b8 = b7 ** 2
        b9 = b8.sum(axis=1)
        b10 = b9.argsort()
        b11 = {}
        for j in range(k):
            b12 = data_labels[b10[j]]
            b11[b12] = b11.get(b12, 0) + 1
        a1 = 0
        a2 = -1
        for key in b11:
            if b11[key] > a1:
                a1 = b11[key]
                a2 = key
        b6[i] = a2
    return b6
def fonk5(b21, labels):
    with open('4251258720.txt', 'w') as f:
        for i in range(b21.shape[0]):
            f.write(str(b21[i]) + " " + str(labels[i]) + "\n")
if b13 = = "__main__":
    K, D, N, b14 = map(int, sys.argv[1:])
    b15 = fonk1(b14)
    b2, b3, b4, b5 = fonk2(b15['data'], b15['labels'], N)
    b16 = fonk3(b2)
    b17 = fonk3(b3)
    b18 = b17.reshape(1000 - N, 1024)
    b19 = b16.reshape(N, 1024)
    b20 = PCA(n_components=D, svd_solver='full')
    b18 = b20.fit_transform(b18)
    b19 = b20.transform(b19)
    b21 = fonk4(b19, b18, b5, K)
    fonk5(b21, b4)
    for i in range(b21.shape[0]):
        print(b21[i], b4[i])