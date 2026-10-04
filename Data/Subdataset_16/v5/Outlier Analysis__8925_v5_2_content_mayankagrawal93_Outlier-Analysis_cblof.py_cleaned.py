
import pandas as pd
import time
import numpy as np
def fonk1(x):
    return float(x)
def fonk2(f, d):
    for k, v in d.items():
        d[k] = f(v)
def fonk3(b11, current_tuple):
    b1 = [{current_tuple[k]: 1} for k in current_tuple]
    return [[b11], b1]
def fonk4(cluster, current_tuple):
    for k in current_tuple:
        b2 = cluster[k][0]
        if current_tuple[k] in b2:
            b2[current_tuple[k]] += 1
        else:
            b2[current_tuple[k]] = 1
def fonk5(cluster_summary, current_tuple):
    a1 = 0
    for k in current_tuple:
        b3 = cluster_summary[k][0].get(current_tuple[k], 0)
        b4 = sum(cluster_summary[k][0].values())
        a1 += b3 / float(b4)
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
    print("Value frequency count completed")
    b9 = {i: {j: fonk1(val) for j, val in enumerate(row)} for i, row in enumerate(b6)}
    print("Data processing completed")
    b10 = []
    a2 = 5
    for b11, current_tuple in b9.items():
        if b11 = = 0:
            b10.append(fonk3(b11, current_tuple))
        else:
            b12 = [fonk5(c[1], current_tuple) for c in b10]
            b13 = max(b12)
            b14 = b12.index(b13)
            if b13 >= a2:
                b10[b14][0].append(b11)
                fonk4(b10[b14][1], current_tuple)
            else:
                b10.append(fonk3(b11, current_tuple))
                print(f"New cluster created for b11 {b11}")
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
        b20 = next(size for size, cluster in b15.items() if b11 in cluster[0])
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
    print("Outliers:", b24)
if b25 = = "__main__":
    fonk6()