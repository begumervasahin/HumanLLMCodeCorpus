import pandas as pd
import numpy as np
import time
def fonk1(x):
    return float(x)
def fonk2(func, dictionary):
    for b12, value in dictionary.items():
        dictionary[b12] = func(value)
def fonk3(b12, b11):
    b1 = []
    b2 = [[b12], b1]
    for k, v in b11.items():
        b1.append([{v: 1}])
    return b2
def fonk4(b21, b11):
    for k, v in b11.items():
        if v in b21[k][0]:
            b21[k][0][v] += 1
        else:
            b21[k][0][v] = 1
def fonk5(b21, current):
    a1 = 0
    for k, v in current.items():
        if v in b21[k][0]:
            b3 = b21[k][0][v]
        else:
            b3 = 0
        a1 += (b3 / float(sum(b21[k][0].values())))
    return a1
b4 = pd.read_csv("fsd.csv")
b5 = np.array(b4)
b6 = {}
for column in b4:
    b7 = np.array(b4[column])
    for value in b7:
        if value in b6:
            b6[value] += 1
        else:
            b6[value] = 1
    break
b8 = {}
for index, row in enumerate(b5):
    b9 = {}
    for i, value in enumerate(row):
        b9[i] = fonk1(value)
    b8[index] = b9
b10 = []
for b12 in b8:
    b11 = b8[b12]
    print("Processing tuple", b12)
    if b12 = = 0:
        b10.append(fonk3(b12, b11))
    else:
        b13 = []
        for b21 in b10:
            b13.append(fonk5(b21[1], b11))
        b14 = max(b13)
        b15 = b13.index(b14)
        a2 = 5
        if b14 >= a2:
            b10[b15][0].append(b12)
            fonk4(b10[b15][1], b11)
        else:
            b10.append(fonk3(b12, b11))
            print("New b21 created for tuple", b12)
b16 = {}
for b21 in b10:
    b16[len(b21[0])] = b21
b17 = sorted(b16.keys())
a3 = 0.1
a4 = 0
b18 = []
b19 = []
for size in b17:
    a4 += size
    if a4 <= a3 * len(b8):
        b19.append(size)
    else:
        b18.append(size)
b20 = {}
for b12 in b8:
    b11 = b8[b12]
    for cluster_size in b16:
        if b12 in b16[cluster_size][0]:
            b21 = cluster_size
            break
    print("Processing tuple", b12)
    if b21 in b18:
        a1 = fonk5(b16[b21][1], b11)
        b22 = b21 * a1
        b20[b12] = round(b22, 6)
        print("Tuple", b12, "processed: in large b21")
    else:
        b13 = []
        for cluster_size in b18:
            b13.append(fonk5(b16[cluster_size][1], b11))
        b23 = min(b13)
        b22 = b21 * b23
        b20[b12] = round(b22, 6)
        print("Tuple", b12, "processed: in small b21")
b24 = sorted(b20, b12=b20.get, reverse=True)
a5 = 5
b25 = int((a5 / 100.0) * len(b24))
b26 = b24[:b25]