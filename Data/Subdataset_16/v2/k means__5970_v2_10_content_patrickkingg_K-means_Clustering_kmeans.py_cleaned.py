import numpy as np
from csv import reader
from random import randint
from copy import deepcopy
from sys import argv
def fonk1():
    if len(argv) != 4:
        print("Usage: python script.py <b1> <b2> <b3>")
        return
    b1 = argv[1]
    b2 = int(argv[2])
    b3 = argv[3]
    b4 = fonk2(b1)
    b5 = fonk3(b4)
    b15, b6 = fonk5(b5, b2)
    b7 = fonk10(b5, b15, b6)
    print(f"SSE is {b7:.2f}")
    fonk11(b3, b15, b7)
def fonk2(file_path):
    with open(file_path, 'b8') as file:
        b8 = reader(file)
        return np.array([row for row in b8 if row])
def fonk3(b4):
    b5, b9 = b4[:, :-1], b4[:, -1]
    b5 = b5.astype(np.float64)
    return fonk4(b5)
def fonk4(b5):
    b10 = []
    for col in b5.T:
        b11 = col.min()
        b12 = col.max()
        b13 = (col - b11) / (b12 - b11)
        b10.append(b13)
    return np.array(b10).T
def fonk5(b5, b2):
    b6 = fonk6(b5, b2)
    b14 = np.zeros(b6.shape)
    b15 = np.zeros(len(b5))
    while not fonk7(b6, b14):
        b15 = fonk8(b5, b6)
        b14 = deepcopy(b6)
        b6 = fonk9(b5, b15, b2)
    return b15, b6
def fonk6(b5, b2):
    b6 = []
    b16 = set()
    while len(b16) < b2:
        b17 = randint(0, len(b5) - 1)
        if b17 not in b16:
            b6.append(b5[b17])
            b16.add(b17)
    return np.array(b6)
def fonk7(b6, b14):
    return np.allclose(b6, b14)
def fonk8(b5, b6):
    b15 = np.zeros(len(b5))
    for i, x in enumerate(b5):
        b18 = np.linalg.norm(x - b6, b21=1)
        b15[i] = np.argmin(b18)
    return b15
def fonk9(b5, b15, b2):
    b19 = np.zeros((b2, b5.shape[1]))
    for i in range(b2):
        b20 = b5[b15 == i]
        if len(b20) > 0:
            b19[i] = b20.mean(b21 = 0)
    return b19
def fonk10(b5, b15, b6):
    b7 = 0
    for i, centroid in enumerate(b6):
        b20 = b5[b15 == i]
        b7 += np.sum(np.linalg.norm(b20 - centroid, b21 = 1) ** 2)
    return b7
def fonk11(b3, b15, b7):
    with open(b3, 'w') as f:
        for cluster in b15:
            f.write(f"{int(cluster)}\n")
        f.write(f"SSE is {b7:.2f}")
if b22 = = '__main__':
    fonk1()