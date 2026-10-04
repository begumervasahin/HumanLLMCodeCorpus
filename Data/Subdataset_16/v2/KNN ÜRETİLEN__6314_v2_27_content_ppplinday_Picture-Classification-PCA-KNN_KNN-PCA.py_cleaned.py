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
    b3 = b1['b3']
    b4 = b2[:n].reshape(n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b5 = b2[n:1000].reshape(1000 - n, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b6 = np.array(b3[:n])
    b7 = np.array(b3[n:1000])
    return b4, b5, b6, b7
def fonk3(b2):
    num, height, width, b8 = b2.shape
    b9 = np.zeros([num, height, width], float)
    for n in range(num):
        for row in range(height):
            for col in range(width):
                b9[n, row, col] = 0.299 * b2[n, row, col, 0] + 0.587 * b2[n, row, col, 1] + 0.114 * b2[n, row, col, 2]
    return b9
def fonk4(test, b5, data_labels, k):
    if k <= 0:
        return None
    b10 = np.zeros(test.shape[0], int)
    for i in range(test.shape[0]):
        b11 = np.tile(test[i], (b5.shape[0], 1)) - b5
        b12 = b11 ** 2
        b13 = b12.sum(axis=1)
        b14 = b13.argsort()
        b15 = {}
        for j in range(k):
            b16 = data_labels[b14[j]]
            b15[b16] = b15.get(b16, 0) + 1
        b10[i] = max(b15, b17 = b15.get)
    return b10
def fonk5(b10, b3):
    b18 = '4251258720.txt'
    if os.path.exists(b18):
        os.remove(b18)
    with open(b18, 'a') as f:
        for pred, b16 in zip(b10, b3):
            f.fonk5(f"{pred} {b16}\n")
if b19 = = "__main__":
    b20 = int(sys.argv[1])
    b21 = int(sys.argv[2])
    b22 = int(sys.argv[3])
    b23 = sys.argv[4]
    b1 = fonk1(b23)
    b4, b5, b6, b7 = fonk2(b1, b22)
    b24 = fonk3(b4)
    b25 = fonk3(b5)
    b26 = b25.reshape(1000 - b22, 1024)
    b27 = b24.reshape(b22, 1024)
    b28 = PCA(n_components=b21, svd_solver='full')
    b26 = b28.fit_transform(b26)
    b27 = b28.transform(b27)
    b10 = fonk4(b27, b26, b7, b20)
    fonk5(b10, b6)
    for pred, b16 in zip(b10, b6):
        print(pred, b16)