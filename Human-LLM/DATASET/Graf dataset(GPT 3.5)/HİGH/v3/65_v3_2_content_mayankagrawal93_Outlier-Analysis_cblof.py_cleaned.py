import pandas as pd
import numpy as np
import time
def fonk1(x):
    return float(x)
def fonk2(f, d):
    for k, v in d.items():
        d[k] = f(v)
def fonk3(b17, b16):
    b1 = []
    b2 = []
    for k in b16:
        b3 = {b16[k]: 1}
        b1.append([b3])
    b2.append([b17])
    b2.append(b1)
    return b2
def fonk4(cluster, b16):
    for k in b16:
        if b16[k] in cluster[k][0]:
            cluster[k][0][b16[k]] += 1
        else:
            cluster[k][0][b16[k]] = 1
def fonk5(cluster, b16):
    a1 = 0
    for k in b16:
        if b16[k] in cluster[k][0]:
            b4 = cluster[k][0][b16[k]]
        else:
            b4 = 0
        a1 += (b4 / float(sum(cluster[k][0].values())))
    return a1
def fonk6(b11, b13, b15):
    b5 = {}
    for b17 in b13:
        b6 = b13[b17]
        for cluster_size in b15:
            if b17 in b15[cluster_size][0]:
                b7 = cluster_size
                break
        if b7 in b21:
            a1 = fonk5(b15[b7][1], b6)
            b8 = b7 * a1
            b5[b17] = round(b8, 6)
        else:
            b9 = []
            for lc in b21:
                b9.append(fonk5(b15[lc][1], b6))
            b10 = min(b9)
            b8 = b7 * b10
            b5[b17] = round(b8, 6)
    return b5
b11 = pd.read_csv("fsd.csv")
b12 = np.array(b11)
b13 = {}
for column_name in b11:
    b14 = np.array(b11[column_name])
    for index, value in enumerate(b14):
        b13[index] = {i: fonk1(v) for i, v in enumerate(b14)}
    break
b15 = {}
for b17 in b13:
    b16 = b13[b17]
    print("Processing tuple", b17)
    if b17 = = 0:
        b15[b17] = fonk3(b17, b16)
    else:
        b9 = {}
        for cluster_key in b15:
            b9[cluster_key] = fonk5(b15[cluster_key][1], b16)
        b18 = max(b9, b17=b9.get)
        a2 = 5
        if b9[b18] >= a2:
            b15[b18][0].append(b17)
            fonk4(b15[b18][1], b16)
        else:
            b15[b17] = fonk3(b17, b16)
            print("New cluster created for tuple", b17)
b19 = {len(b15[cluster_size][0]): b15[cluster_size] for cluster_size in b15}
b20 = sorted(b19.keys())
a3 = 0.1
a4 = 0
b21 = []
b22 = []
for size in b20:
    a4 += size
    if a4 <= a3 * len(b13):
        b22.append(size)
    else:
        b21.append(size)
b5 = fonk6(b11, b13, b15)
b23 = sorted(b5, b17=b5.get, reverse=True)
a5 = 5
b24 = int((a5 / 100.0) * len(b23))
b25 = b23[:b24]