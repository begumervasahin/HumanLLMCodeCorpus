import numpy as np
from csv import reader
from random import randint
from copy import deepcopy
from sys import argv
def fonk1():
    b1 = argv[1]
    b2 = int(argv[2])
    b3 = argv[3]
    b4 = fonk2(b1)
    b6, b5 = b4[:, :-1], b4[:, -1]
    b6 = fonk3(b6)
    b12, b7 = fonk7(b6, b2)
    b8 = fonk8(b6, b12, b7)
    print(f"SSE is {b8:.2f}")
    fonk9(b3, b12, b8)
def fonk2(file_path):
    with open(file_path) as file:
        return np.array([row for row in reader(file) if row])
def fonk3(b6):
    return (b6 - b6.min(b9 = 0)) / (b6.max(b9=0) - b6.min(b9=0))
def fonk4(b6, b2):
    b10 = set()
    b7 = []
    while len(b7) < b2:
        b11 = randint(0, len(b6) - 1)
        if b11 not in b10:
            b7.append(b6[b11])
            b10.add(b11)
    return np.array(b7)
def fonk5(b6, b7):
    b12 = np.zeros(len(b6))
    for i, point in enumerate(b6):
        b13 = np.linalg.norm(point - b7, b9=1)
        b12[i] = np.argmin(b13)
    return b12
def fonk6(b6, b12, b2):
    b14 = np.zeros((b2, b6.shape[1]))
    for i in range(b2):
        b15 = b6[b12 == i]
        if len(b15) > 0:
            b14[i] = b15.mean(b9 = 0)
    return b14
def fonk7(b6, b2):
    b7 = fonk4(b6, b2)
    b16 = np.zeros_like(b7)
    b12 = np.zeros(len(b6))
    while np.linalg.norm(b7 - b16, b9 = 1).sum() != 0:
        b12 = fonk5(b6, b7)
        b16 = deepcopy(b7)
        b7 = fonk6(b6, b12, b2)
    return b12, b7
def fonk8(b6, b12, b7):
    b8 = 0.0
    for i, centroid in enumerate(b7):
        b15 = b6[b12 == i]
        b8 += np.sum((b15 - centroid) ** 2)
    return b8
def fonk9(file_path, b12, b8):
    with open(file_path, 'w') as file:
        for cluster in b12:
            file.write(f"{int(cluster)}\n")
        file.write(f"SSE is {b8:.2f}")
if b17 = = '__main__':
    fonk1()