import numpy as np
import sys
from sklearn.decomposition import PCA
import os
import pickle
def fonk1(b27):
    with open(b27, 'rb') as fo:
        b1 = pickle.load(fo, encoding='latin1')
    return b1
def fonk2(b1, b26):
    b2 = b1['b2']
    b3 = b1['b3']
    b4 = b2[:b26].reshape(b26, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b5 = b2[b26:1000].reshape(1000 - b26, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    b6 = np.array(b3[:b26])
    b7 = np.array(b3[b26:1000])
    return b4, b5, b6, b7
def fonk3(b2):
    num, height, width, b8 = b2.shape
    b9 = np.zeros((num, height, width), float)
    for b26 in range(num):
        b9[b26] = 0.299 * b2[b26, :, :, 0] + 0.587 * b2[b26, :, :, 1] + 0.114 * b2[b26, :, :, 2]
    return b9
def fonk4(test_data, train_data, train_labels, b24):
    b10 = test_data.shape[0]
    b11 = np.zeros(b10, int)
    for i in range(b10):
        b12 = np.sqrt(((train_data - test_data[i]) ** 2).sum(axis=1))
        b13 = b12.argsort()
        b14 = {}
        for j in range(b24):
            b15 = train_labels[b13[j]]
            b14[b15] = b14.get(b15, 0) + 1
        b11[i] = max(b14, b16 = b14.get)
    return b11
def fonk5(b11, b3, b17 = '4251258720.txt'):
    if os.path.exists(b17):
        os.remove(b17)
    with open(b17, 'a') as f:
        for pred, b15 in zip(b11, b3):
            f.write(f"{pred} {b15}\b26")
def fonk6(b24, b25, b26, b27):
    b1 = fonk1(b27)
    b4, b5, b6, b7 = fonk2(b1, b26)
    b18 = fonk3(b4).reshape(b26, -1)
    b19 = fonk3(b5).reshape(1000 - b26, -1)
    b20 = PCA(n_components=b25, svd_solver='full')
    b21 = b20.fit_transform(b19)
    b22 = b20.transform(b18)
    b11 = fonk4(b22, b21, b7, b24)
    fonk5(b11, b6)
    for pred, b15 in zip(b11, b6):
        print(pred, b15)
if b23 = = "__main__":
    b24 = int(sys.argv[1])
    b25 = int(sys.argv[2])
    b26 = int(sys.argv[3])
    b27 = sys.argv[4]
    fonk6(b24, b25, b26, b27)