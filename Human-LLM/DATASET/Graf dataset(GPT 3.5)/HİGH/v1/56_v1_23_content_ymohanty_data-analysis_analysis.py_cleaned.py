import random
import sys
import numpy as np
import scipy.stats
import scipy.cluster.vq as vq
import scipy.spatial.distance as norms
import data
import math
b1 = "Yashaswi Mohanty"
b2 = "ymohanty@colby.edu"
b3 = "2/21/2016"
def fonk1(b24, b15, b4 = None):
    b5 = []
    b6 = b24
    b7 = b6.shape[0]
    if b4 is None:
        for i in range(b15):
            b5.append(b6[np.random.randint(0, b7)].tolist()[0])
    else:
        if b15 != max(b4) + 1:
            print("The highest category label and specified clusters should be the same")
            return
        for i in range(b15):
            b8 = np.zeros(b6.shape[1])
            a1 = 0
            for j in range(len(b4)):
                if b4[j] == i:
                    b8 = np.add(b8, b6[j].tolist()[0])
                    a1 += 1
            b8 = 1 / float(a1) * b8
            b5.append(b8)
    return np.matrix(b5)
def fonk2(b6, b5, metric):
    b9 = []
    b10 = []
    b11 = sys.maxsize
    for v in b6:
        a2 = 0
        for i in range(len(b5.tolist())):
            b12 = b5.tolist()[i]
            b13 = np.vstack((v, b12))
            if norms.pdist(b13, metric)[0] < b11:
                b11 = norms.pdist(b13, metric)[0]
                a2 = i
        b9.append([a2])
        b10.append([b11])
        b11 = sys.maxsize
    return np.matrix(b9), np.matrix(b10)
def fonk3(b6, b5, metric):
    a3 = 1e-7
    a4 = 100
    b14 = b5.shape[1]
    b15 = b5.shape[0]
    b7 = b6.shape[0]
    for i in range(a4):
        codes, b16 = fonk2(b6, b5, metric)
        b17 = np.zeros_like(b5)
        b18 = np.zeros((b15, 1))
        for j in range(b7):
            b17[codes[j, 0], :] += b6[j, :]
            b18[codes[j, 0], 0] += 1.0
        for j in range(b15):
            if b18[j, 0] > 0.0:
                b17[j, :] /= b18[j, 0]
            else:
                b17[j, :] = b6[random.randint(0, b6.shape[0]), :]
        b19 = np.b8(np.square(b5 - b17))
        b5 = b17
        if b19 < a3:
            break
    codes, b16 = fonk2(b6, b5, metric)
    return b5, codes, b16
def fonk4(b24, headers, b15, metric, b20 = True, b4=None):
    try:
        b6 = b24.get_data(headers)
    except AttributeError:
        b6 = b24
    if b20:
        b21 = vq.b20(b6)
    else:
        b21 = b6
    b22 = fonk1(b21, b15, b4)
    b22, codes, b16 = fonk3(b21, b22, metric)
    return b22, codes, b16
if b23 = = '__main__':
    b24 = data.Data("clusterdata.csv")
    b5 = fonk1(b24, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2])
    print(fonk2(b24, b5))