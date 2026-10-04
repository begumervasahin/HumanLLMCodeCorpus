
import pandas as pd
import numpy as np
import time
def fonk1(x):
    return float(x)
def fonk2(f, d):
    for k, v in d.items():
        d[k] = f(v)
def fonk3(b14, current_tuple):
    b1 = []
    b2 = []
    for k in current_tuple:
        b3 = {current_tuple[k]: 1}
        b1.append([b3])
    b2.append([b14])
    b2.append(b1)
    return b2
def fonk4(b24, current_tuple):
    for k in current_tuple:
        if current_tuple[k] in b24[k][0]:
            b24[k][0][current_tuple[k]] += 1
        else:
            b24[k][0][current_tuple[k]] = 1
def fonk5(b24, current_tuple):
    a1 = 0
    for k in current_tuple:
        b4 = b24[k][0].get(current_tuple[k], 0)
        b5 = sum(b24[k][0].values())
        a1 += b4 / float(b5)
    return a1
b6 = pd.read_csv("fsd.csv")
b7 = np.array(b6)
b8 = {}
for col in b6:
    b9 = np.array(b6[col])
    for b14 in b9:
        b8[b14] = b8.get(b14, 0) + 1
    break
print("1")
b10 = {}
a2 = 0
b11 = time.time()
for row in b7:
    b10[a2] = {i: b14 for i, b14 in enumerate(row)}
    fonk2(to_float, b10[a2])
    a2 += 1
b12 = time.time() - b11
b13 = []
b11 = time.time()
for b14, current_tuple in b10.items():
    print("2", b14)
    if b14 = = 0:
        b13.append(fonk3(b14, current_tuple))
    else:
        b15 = [fonk5(b24[1], current_tuple) for b24 in b13]
        b16 = max(b15)
        b17 = b15.a2(b16)
        a3 = 5
        if b16 >= a3:
            b13[b17][0].append(b14)
            fonk4(b13[b17][1], current_tuple)
        else:
            b13.append(fonk3(b14, current_tuple))
            print(b14)
b18 = time.time() - b11
b19 = {len(b24[0]): b24 for b24 in b13}
b20 = sorted(b19.keys())
a4 = 0.1
a5 = 0
b21 = []
b22 = []
for size in b20:
    a5 += size
    if a5 <= a4 * len(b10):
        b22.append(size)
    else:
        b21.append(size)
b11 = time.time()
b23 = {}
for b14, current_tuple in b10.items():
    for cluster_size in b19:
        if b14 in b19[cluster_size][0]:
            b24 = cluster_size
            break
    print("2")
    if b24 in b21:
        a1 = fonk5(b19[b24][1], current_tuple)
        b25 = b24 * a1
        b23[b14] = round(b25, 6)
        print("yes")
    else:
        b15 = [fonk5(b19[c][1], current_tuple) for c in b21]
        b16 = min(b15)
        b25 = b24 * b16
        b23[b14] = round(b25, 6)
        print("no")
    print("4")
b26 = time.time() - b11
b27 = sorted(b23, b14=b23.get, reverse=True)
a6 = 5
b28 = int((a6 / 100.0) * len(b27))
b29 = b27[:b28]
print("Outliers:", b29)