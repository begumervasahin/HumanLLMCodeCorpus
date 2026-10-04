
import pandas as pd
import time
import numpy as np
def fonk1(x):
    return float(x)
def fonk2(f, d):
    for k, v in d.items():
        d[k] = f(v)
def fonk3(b11, current_tuple):
    b1 = []
    b2 = []
    for k in current_tuple:
        b3 = {current_tuple[k]: 1}
        b1.append([b3])
    b2.append([b11])
    b2.append(b1)
    return b2
def fonk4(cluster, current_tuple):
    for k in current_tuple:
        if current_tuple[k] in cluster[k][0]:
            cluster[k][0][current_tuple[k]] += 1
        else:
            cluster[k][0][current_tuple[k]] = 1
def fonk5(cluster_summary, current_tuple):
    a1 = 0
    for k in current_tuple:
        if current_tuple[k] in cluster_summary[k][0]:
            b4 = cluster_summary[k][0][current_tuple[k]]
        else:
            b4 = 0
        a1 += b4 / float(sum(cluster_summary[k][0].values()))
    return a1
def fonk6():
    b5 = pd.read_csv("fsd.csv")
    b6 = np.array(b5)
    b7 = {}
    for col in b5:
        b8 = np.array(b5[col])
        for b11 in b8:
            b7[b11] = b7.get(b11, 0) + 1
        break
    print("1")
    b9 = {}
    for i, row in enumerate(b6):
        b9[i] = {j: fonk1(val) for j, val in enumerate(row)}
    print("2")
    b10 = []
    for b11, current_tuple in b9.items():
        if b11 = = 0:
            b10.append(fonk3(b11, current_tuple))
        else:
            b12 = [fonk5(c[1], current_tuple) for c in b10]
            b13 = max(b12)
            b14 = b12.index(b13)
            a2 = 5
            if b13 >= a2:
                b10[b14][0].append(b11)
                fonk4(b10[b14][1], current_tuple)
            else:
                b10.append(fonk3(b11, current_tuple))
                print(b11)
    b15 = {len(c[0]): c for c in b10}
    b16 = sorted(b15.keys())
    a3 = 0.1
    a4 = 0
    b17 = []
    b18 = []
    for size in b16:
        a4 += size
        if a4 <= a3 * len(b9):
            b18.append(size)
        else:
            b17.append(size)
    b19 = {}
    for b11, current_tuple in b9.items():
        b20 = None
        for size, cluster in b15.items():
            if b11 in cluster[0]:
                b20 = size
                break
        if b20 in b17:
            a1 = fonk5(b15[b20][1], current_tuple)
            b21 = b20 * a1
            b19[b11] = round(b21, 6)
        else:
            b12 = [fonk5(b15[size][1], current_tuple) for size in b17]
            b13 = min(b12)
            b21 = b20 * b13
            b19[b11] = round(b21, 6)
    b22 = sorted(b19, b11=b19.get, reverse=True)
    a5 = 5
    b23 = int((a5 / 100.0) * len(b22))
    b24 = b22[:b23]
    print(b24)
if b25 = = "__main__":
    fonk6()