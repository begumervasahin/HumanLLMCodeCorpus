import numpy as np
import scipy.spatial.b13 as norms
import scipy.cluster.vq as vq
import sys
import random
import data
b1 = "Yashaswi Mohanty"
b2 = "ymohanty@colby.edu"
b3 = "2/21/2016"
def fonk1(b23, b14, b4 = None):
    b5 = []
    b6 = b23.shape[0]
    if b4 is None:
        for b15 in range(b14):
            b5.append(b23[np.random.randint(0, b6)].tolist()[0])
    else:
        if b14 != max(b4) + 1:
            print("The highest category label and specified clusters should be the same")
            return
        for i in range(b14):
            b7 = np.zeros(b23.shape[1])
            a1 = 0
            for j in range(len(b4)):
                if b4[j] == i:
                    b7 = np.add(b7, b23[j].tolist()[0])
                    a1 += 1
            b8 = 1 / float(a1) * b7
            b5.append(b8)
    return np.matrix(b5)
def fonk2(b23, b5, distance_metric):
    b9 = []
    b10 = []
    b11 = sys.maxsize
    for data_point in b23:
        a2 = 0
        for i, center in enumerate(b5.tolist()):
            b12 = np.vstack((data_point, center))
            b13 = norms.pdist(b12, distance_metric)[0]
            if b13 < b11:
                b11 = b13
                a2 = i
        b9.append([a2])
        b10.append([b11])
        b11 = sys.maxsize
    return np.matrix(b9), np.matrix(b10)
def fonk3(b23, b20, distance_metric):
    a3 = 1e-7
    a4 = 100
    b14 = b20.shape[0]
    b6 = b23.shape[0]
    for b15 in range(a4):
        b9, b15 = fonk2(b23, b20, distance_metric)
        b16 = np.zeros_like(b20)
        b17 = np.zeros((b14, 1))
        for j in range(b6):
            b18 = b9[j, 0]
            b16[b18, :] += b23[j, :]
            b17[b18, 0] += 1.0
        for j in range(b14):
            if b17[j, 0] > 0.0:
                b16[j, :] /= b17[j, 0]
            else:
                b16[j, :] = b23[random.randint(0, b6), :]
        b19 = np.sum(np.square(b20 - b16))
        b20 = b16
        if b19 < a3:
            break
    b9, b21 = fonk2(b23, b20, distance_metric)
    return b20, b9, b21
def fonk4(b25, headers, b14, distance_metric, b22 = True, b4=None):
    try:
        b23 = b25.get_data(headers)
    except AttributeError:
        b23 = b25
    if b22:
        b23 = vq.b22(b23)
    b20 = fonk1(b23, b14, b4)
    b5, b9, b21 = fonk3(b23, b20, distance_metric)
    return b5, b9, b21
if b24 = = '__main__':
    b25 = data.Data("clusterdata.csv")
    b20 = fonk1(b25, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2])
    print(fonk2(b25, b20))