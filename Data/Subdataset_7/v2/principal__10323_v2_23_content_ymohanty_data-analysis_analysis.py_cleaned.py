import random
import sys
import numpy as np
import scipy.stats
import scipy.cluster.vq as vq
import scipy.spatial.b14 as norms
import data
import math
b1 = "Yashaswi Mohanty"
b2 = "ymohanty@colby.edu"
b3 = "2/21/2016"
def fonk1(b24, b15, b4 = None):
    b5 = []
    b6 = b24.shape[0]
    if b4 is None:
        for b16 in range(b15):
            b5.append(b24[np.random.randint(0, b6)].tolist()[0])
    else:
        if b15 != max(b4) + 1:
            print("The highest category label and specified clusters should be the same")
            return
        for i in range(b15):
            b7 = np.zeros(b24.shape[1])
            a1 = 0
            for j in range(len(b4)):
                if b4[j] == i:
                    b7 = np.add(b7, b24[j].tolist()[0])
                    a1 += 1
            b8 = 1 / float(a1) * b7
            b5.append(b8)
    return np.matrix(b5)
def fonk2(b24, b5, distance_metric):
    b9 = []
    b10 = []
    b11 = sys.maxsize
    for data_point in b24:
        a2 = 0
        for i in range(len(b5.tolist())):
            b12 = b5.tolist()[i]
            b13 = np.vstack((data_point, b12))
            b14 = norms.pdist(b13, distance_metric)[0]
            if b14 < b11:
                b11 = b14
                a2 = i
        b9.append([a2])
        b10.append([b11])
        b11 = sys.maxsize
    return np.matrix(b9), np.matrix(b10)
def fonk3(b24, b21, distance_metric):
    a3 = 1e-7
    a4 = 100
    b15 = b21.shape[0]
    b6 = b24.shape[0]
    for b16 in range(a4):
        b9, b16 = fonk2(b24, b21, distance_metric)
        b17 = np.zeros_like(b21)
        b18 = np.zeros((b15, 1))
        for j in range(b6):
            b19 = b9[j, 0]
            b17[b19, :] += b24[j, :]
            b18[b19, 0] += 1.0
        for j in range(b15):
            if b18[j, 0] > 0.0:
                b17[j, :] /= b18[j, 0]
            else:
                b17[j, :] = b24[random.randint(0, b6), :]
        b20 = np.sum(np.square(b21 - b17))
        b21 = b17
        if b20 < a3:
            break
    b9, b22 = fonk2(b24, b21, distance_metric)
    return b21, b9, b22
def fonk4(b26, headers, b15, distance_metric, b23 = True, b4=None):
    try:
        b24 = b26.get_data(headers)
    except AttributeError:
        b24 = b26
    if b23:
        b24 = vq.b23(b24)
    b21 = fonk1(b24, b15, b4)
    b5, b9, b22 = fonk3(b24, b21, distance_metric)
    return b5, b9, b22
if b25 = = '__main__':
    b26 = data.Data("clusterdata.csv")
    b21 = fonk1(b26, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2])
    print(fonk2(b26, b21))