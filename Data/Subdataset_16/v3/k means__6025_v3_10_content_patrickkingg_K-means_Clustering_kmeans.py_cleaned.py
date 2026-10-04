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
    b10, b6 = fonk5(b5, b2)
    b7 = fonk10(b5, b10, b6)
    print(f"SSE is {b7:.2f}")
    fonk11(b3, b10, b7)
def fonk2(file_path):
    with open(file_path, 'r') as file:
        b8 = reader(file)
        b4 = [row for row in b8 if row]
    return np.array(b4)
def fonk3(b4):
    b5 = b4[:, :-1].astype(np.float64)
    return fonk4(b5)
def fonk4(b5):
    return np.apply_along_axis(lambda col: (col - col.min()) / (col.max() - col.min()), 0, b5)
def fonk5(b5, b2):
    b6 = fonk6(b5, b2)
    b9 = np.zeros(b6.shape)
    b10 = np.zeros(len(b5))
    while not fonk7(b6, b9):
        b10 = fonk8(b5, b6)
        b9 = deepcopy(b6)
        b6 = fonk9(b5, b10, b2)
    return b10, b6
def fonk6(b5, b2):
    b11 = np.random.choice(len(b5), b2, replace=False)
    return b5[b11]
def fonk7(b6, b9):
    return np.allclose(b6, b9)
def fonk8(b5, b6):
    b10 = np.zeros(len(b5))
    for i, x in enumerate(b5):
        b12 = np.linalg.norm(x - b6, b15=1)
        b10[i] = np.argmin(b12)
    return b10
def fonk9(b5, b10, b2):
    b13 = np.zeros((b2, b5.shape[1]))
    for i in range(b2):
        b14 = b5[b10 == i]
        if len(b14) > 0:
            b13[i] = b14.mean(b15 = 0)
    return b13
def fonk10(b5, b10, b6):
    b7 = 0
    for i, centroid in enumerate(b6):
        b14 = b5[b10 == i]
        b7 += np.sum(np.linalg.norm(b14 - centroid, b15 = 1) ** 2)
    return b7
def fonk11(b3, b10, b7):
    with open(b3, 'w') as f:
        for cluster in b10:
            f.write(f"{int(cluster)}\n")
        f.write(f"SSE is {b7:.2f}")
if b16 = = '__main__':
    fonk1()