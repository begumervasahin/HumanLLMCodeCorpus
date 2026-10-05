import pandas as pd
import numpy as np
import time
def fonk1(x):
    return float(x)
def fonk2(f, d):
    for k, v in d.items():
        d[k] = f(v)
def fonk3(b14, b13):
    b1 = []
    b2 = []
    for k in b13:
        b3 = {}
        b3[b13[k]] = 1
        b1.append([b3])
    b2.append([b14])
    b2.append(b1)
    return b2
def fonk4(cluster, b13):
    for k in b13:
        if b13[k] in cluster[k][0]:
            cluster[k][0][b13[k]] += 1
        else:
            cluster[k][0][b13[k]] = 1
def fonk5(c, current):
    a1 = 0
    for k in current:
        if current[k] in c[k][0]:
            b4 = c[k][0][current[k]]
        else:
            b4 = 0
        a1 += (b4 / float(sum(c[k][0].values())))
    return a1
b5 = pd.read_csv("fsd.csv")
b6 = np.array(b5)
b7 = {}
for column in b5:
    b8 = np.array(b5[column])
    for b14 in b8:
        if b14 in b7:
            b7[b14] += 1
        else:
            b7[b14] = 1
    break
b9 = {}
a2 = 0
b10 = time.time()
while a2 < len(b6):
    a3 = 0
    b9[a2] = {}
    for b14 in b6[a2]:
        b9[a2][a3] = b14
        a3 += 1
    fonk2(to_float, b9[a2])
    a2 += 1
b11 = time.time() - b10
b12 = []
b10 = time.time()
for b14 in b9:
    b13 = b9[b14]
    print("Processing tuple", b14)
    if b14 = = 0:
        b12.append(fonk3(b14, b13))
    else:
        b15 = []
        for cluster in b12:
            b15.append(fonk5(cluster[1], b13))
        b16 = max(b15)
        b17 = b15.index(b16)
        a4 = 5
        if b16 >= a4:
            b12[b17][0].append(b14)
            fonk4(b12[b17][1], b13)
        else:
            b12.append(fonk3(b14, b13))
            print("New cluster created for tuple", b14)
b18 = time.time() - b10
b19 = {}
for cluster in b12:
    b19[len(cluster[0])] = cluster
b20 = sorted(b19.keys())
a5 = 0.1
a6 = 0
b21 = []
b22 = []
for size in b20:
    a6 += size
    if a6 <= a5 * len(b9):
        b22.append(size)
    else:
        b21.append(size)
b10 = time.time()
b23 = {}
for b14 in b9:
    b24 = b9[b14]
    for cluster_size in b19:
        if b14 in b19[cluster_size][0]:
            b25 = cluster_size
            break
    if b25 in b21:
        a1 = fonk5(b19[b25][1], b24)
        b26 = b25 * a1
        b23[b14] = round(b26, 6)
    else:
        b15 = []
        for lc in b21:
            b15.append(fonk5(b19[lc][1], b24))
        b16 = min(b15)
        b26 = b25 * b16
        b23[b14] = round(b26, 6)
b27 = time.time() - b10
b28 = sorted(b23, b14=b23.get, reverse=True)
a7 = 5
b29 = int((a7 / 100.0) * len(b28))
b30 = b28[:b29]