import numpy as np
import sys
from sklearn.decomposition import PCA
import os
import pickle
def fonk1(b23):
    with open(b23, 'rb') as fo:
        b1 = pickle.load(fo, encoding='latin1')
    return b1
def fonk2(b1, n):
    b2 = b1['b2']
    b3 = b2[:n]
    b3 = b3.reshape(n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b4 = b2[n:1000]
    b4 = b4.reshape(1000 - n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b5 = b1['b5']
    b6 = np.array(b5[:n])
    b7 = np.array(b5[n:1000])
    return b3, b4, b6, b7
def fonk3(b2):
    b8 = np.zeros([b2.shape[0], b2.shape[1], b2.shape[2]], float)
    b9 = b2.shape[0]
    b10 = b2.shape[1]
    b11 = b2.shape[2]
    for n in range(b9):
        for row in range(b10):
            for col in range(b11):
                b8[n, row, col] = 0.299 * b2[n, row, col, 0] + 0.587 * b2[n, row, col, 1] + 0.114 * b2[n, row, col, 2]
    return b8
def fonk4(test, b4, data_labels, k):
    if k <= 0:
        return None
    b12 = np.zeros([test.shape[0]], int)
    for i in range(test.shape[0]):
        b13 = np.tile(test[i], (b4.shape[0], 1)) - b4
        b14 = b13 ** 2
        b15 = b14.sum(axis=1)
        b16 = b15.argsort()
        b17 = {}
        for j in range(k):
            b18 = data_labels[b16[j]]
            b17[b18] = b17.get(b18, 0) + 1
        a1 = 0
        a2 = -1
        for key in b17:
            if b17[key] > a1:
                a1 = b17[key]
                a2 = key
        b12[i] = a2
    return b12
def fonk5(pred, b5):
    if os.path.exists('4251258720.txt'):
        os.remove('4251258720.txt')
    with open('4251258720.txt', 'a') as f:
        for i in range(pred.shape[0]):
            f.fonk5(str(pred[i]) + " " + str(b5[i]) + "\n")
if b19 = = "__main__":
    b20 = int(sys.argv[1])
    b21 = int(sys.argv[2])
    b22 = int(sys.argv[3])
    b23 = sys.argv[4]
    b1 = fonk1(b23)
    b3, b4, b6, b7 = fonk2(b1, b22)
    b24 = fonk3(b3)
    b25 = fonk3(b4)
    b26 = b25.reshape(1000 - b22, 1024)
    b27 = b24.reshape(b22, 1024)
    b28 = PCA(n_components=b21, svd_solver='full')
    b26 = b28.fit_transform(b26)
    b27 = b28.transform(b27)
    b29 = fonk4(b27, b26, b7, b20)
    fonk5(b29, b6)
    for i in range(b29.shape[0]):
        print(b29[i], b6[i])