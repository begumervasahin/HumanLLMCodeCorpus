import numpy as np
import sys
from sklearn.decomposition import PCA
import os
import pickle
def fonk1(b30):
    with open(b30, 'rb') as fo:
        b1 = pickle.load(fo, encoding='latin1')
    return b1
def fonk2(b1, b29):
    b2 = b1['b2']
    b3 = b1['b3']
    b4 = b2[:b29].reshape(b29, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b5 = b2[b29:1000].reshape(1000 - b29, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b6 = np.array(b3[:b29])
    b7 = np.array(b3[b29:1000])
    return b4, b5, b6, b7
def fonk3(b2):
    num, height, width, b8 = b2.shape
    b9 = np.zeros((num, height, width), float)
    for b29 in range(num):
        for row in range(height):
            for col in range(width):
                r, g, b10 = b2[b29, row, col]
                b9[b29, row, col] = 0.299 * r + 0.587 * g + 0.114 * b10
    return b9
def fonk4(test_data, train_data, train_labels, b27):
    if b27 <= 0:
        return None
    b11 = test_data.shape[0]
    b12 = np.zeros(b11, int)
    for i in range(b11):
        b13 = np.tile(test_data[i], (train_data.shape[0], 1)) - train_data
        b14 = b13 ** 2
        b15 = b14.sum(axis=1)
        b16 = b15.argsort()
        b17 = {}
        for j in range(b27):
            b18 = train_labels[b16[j]]
            b17[b18] = b17.get(b18, 0) + 1
        b12[i] = max(b17, b19 = b17.get)
    return b12
def fonk5(b12, b3):
    b20 = '4251258720.txt'
    if os.path.exists(b20):
        os.remove(b20)
    with open(b20, 'a') as f:
        for pred, b18 in zip(b12, b3):
            f.write(f"{pred} {b18}\b29")
def fonk6(b27, b28, b29, b30):
    b1 = fonk1(b30)
    b4, b5, b6, b7 = fonk2(b1, b29)
    b21 = fonk3(b4).reshape(b29, -1)
    b22 = fonk3(b5).reshape(1000 - b29, -1)
    b23 = PCA(n_components=b28, svd_solver='full')
    b24 = b23.fit_transform(b22)
    b25 = b23.transform(b21)
    b12 = fonk4(b25, b24, b7, b27)
    fonk5(b12, b6)
    for pred, b18 in zip(b12, b6):
        print(pred, b18)
if b26 = = "__main__":
    b27 = int(sys.argv[1])
    b28 = int(sys.argv[2])
    b29 = int(sys.argv[3])
    b30 = sys.argv[4]
    fonk6(b27, b28, b29, b30)