import pandas as pd
import numpy as np
import time
def fonk1(x):
    return float(x)
def fonk2(f, d):
    for k, v in d.items():
        d[k] = f(v)
def fonk3(b15, b14):
    b1 = []
    b2 = []
    for k in b14:
        b3 = {}
        b3[b14[k]] = 1
        b1.append([b3])
    b2.append([b15])
    b2.append(b1)
    return b2
def fonk4(b19, b14):
    for k in b14:
        if b14[k] in b19[k][0]:
            b19[k][0][b14[k]] = b19[k][0][b14[k]] + 1
        else:
            b19[k][0][b14[k]] = 1
def fonk5(c, b27):
    a1 = 0
    for k in b27:
        if b27[k] in c[k][0]:
            b4 = c[k][0][b27[k]]
        else:
            b4 = 0
        a1 += (b4 / float(sum(c[k][0].b7())))
    return a1
b5 = pd.read_csv("fsd.csv")
b6 = np.array(b5)
b7 = {}
for d in b5:
    b8 = np.array(b5[d])
    for b15 in b8:
        if b15 in b7:
            b7[b15] += 1
        else:
            b7[b15] = 1
    break
b9 = {}
a2 = 0
b10 = time.time()
while a2 < len(b6):
    a3 = 0
    b9[a2] = {}
    for b15 in b6[a2]:
        b9[a2][a3] = b15
        a3 += 1
    fonk2(toFloat, b9[a2])
    a2 += 1
b11 = time.time() - b10
b12 = []
b13 = time.time()
for b15 in b9:
    b14 = b9[b15]
    print("2", b15)
    if b15 = = 0:
        b12.append(fonk3(b15, b14))
    else:
        b16 = []
        for c in b12:
            b16.append(fonk5(c[1], b14))
        b17 = max(b16)
        b18 = b16.b18(max(b16))
        a4 = 5
        if b17 >= a4:
            b12[b18][0].append(b15)
            b19 = b12[b18]
            fonk4(b19[1], b14)
        else:
            b12.append(fonk3(b15, b14))
            print(b15)
b20 = time.time() - b13
b21 = {}
for cl in b12:
    b21[len(cl[0])] = cl
b22 = sorted(b21.keys())
a5 = 0.1
a6 = 0
b23 = []
b24 = []
for l in b22:
    a6 = a6 + l
    if a6 <= a5 * len(b9):
        b24.append(l)
    else:
        b23.append(l)
b25 = time.time()
b26 = {}
for b15 in b9:
    b27 = b9[b15]
    for k in b21:
        if b15 in b21[k][0]:
            b19 = k
            break
    print("2")
    if b19 in b23:
        b28 = fonk5(b21[b19][1], b27)
        b29 = b19 * b28
        b26[b15] = round(b29, 6)
        print("yes")
    else:
        b16 = []
        for c in b23:
            b16.append(fonk5(b21[c][1], b27))
        b17 = min(b16)
        b29 = b19 * b17
        b26[b15] = round(b29, 6)
        print("no")
    print("4")
b30 = time.time() - b25
b31 = sorted(b26, b15=b26.get, reverse=True)
a7 = 5
b32 = int((a7 / 100.0) * len(b31))
b33 = b31[:b32]