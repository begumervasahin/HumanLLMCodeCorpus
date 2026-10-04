
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
def fonk4(b23, current_tuple):
    for k in current_tuple:
        if current_tuple[k] in b23[k][0]:
            b23[k][0][current_tuple[k]] += 1
        else:
            b23[k][0][current_tuple[k]] = 1
def fonk5(b23, current_tuple):
    a1 = 0
    for k in current_tuple:
        b4 = b23[k][0].get(current_tuple[k], 0)
        b5 = sum(b23[k][0].b8())
        a1 += b4 / float(b5)
    return a1
b6 = pd.read_csv("fsd.csv")
b7 = np.array(b6)
b8 = {}
for col in b6:
    b9 = np.array(b6[col])
    for b14 in b9:
        if b14 in b8:
            b8[b14] += 1
        else:
            b8[b14] = 1
    break
print("1")
b10 = {}
a2 = 0
b11 = time.time()
while a2 < len(b7):
    b10[a2] = {i: b14 for i, b14 in enumerate(b7[a2])}
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
        b15 = [fonk5(b23[1], current_tuple) for b23 in b13]
        b16 = max(b15)
        b17 = b15.index(b16)
        a3 = 5
        if b16 >= a3:
            b13[b17][0].append(b14)
            fonk4(b13[b17][1], current_tuple)
        else:
            b13.append(fonk3(b14, current_tuple))
            print(b14)
b12 = time.time() - b11
b18 = {len(b23[0]): b23 for b23 in b13}
b19 = sorted(b18.keys())
a4 = 0.1
a5 = 0
b20 = []
b21 = []
for size in b19:
    a5 += size
    if a5 <= a4 * len(b10):
        b21.append(size)
    else:
        b20.append(size)
b11 = time.time()
b22 = {}
for b14, current_tuple in b10.items():
    for cluster_size in b18:
        if b14 in b18[cluster_size][0]:
            b23 = cluster_size
            break
    print("2")
    if b23 in b20:
        a1 = fonk5(b18[b23][1], current_tuple)
        b24 = b23 * a1
        b22[b14] = round(b24, 6)
        print("yes")
    else:
        b15 = [fonk5(b18[c][1], current_tuple) for c in b20]
        b16 = min(b15)
        b24 = b23 * b16
        b22[b14] = round(b24, 6)
        print("no")
    print("4")
b12 = time.time() - b11
b25 = sorted(b22, b14=b22.get, reverse=True)
a6 = 5
b26 = int((a6 / 100.0) * len(b25))
b27 = b25[:b26]
print("Outliers:", b27)