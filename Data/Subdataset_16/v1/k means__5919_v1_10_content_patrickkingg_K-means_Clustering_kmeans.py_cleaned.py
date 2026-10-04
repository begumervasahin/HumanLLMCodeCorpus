import numpy as np
from csv import reader
from random import randint
from copy import deepcopy
from sys import argv
def fonk1():
    if len(argv) != 4:
        print("Usage: python script.py <input_file> <b2> <output_file>")
        return
    b1 = argv[1]
    b2 = int(argv[2])
    b3 = argv[3]
    with open(b1, 'b4') as file:
        b4 = reader(file)
        b5 = np.array([row for row in b4 if row])
    b7, b6 = b5[:, :-1], b5[:, -1]
    b7 = b7.astype(np.float64)
    b7 = fonk2(b7)
    b10, b8 = fonk4(b7, b2)
    b9 = fonk5(b7, b2, b8, b10)
    print(f"SSE is {b9:.2f}")
    b10 = list(map(int, b10))
    with open(b3, 'w') as f:
        for i in b10:
            f.write(str(i) + '\n')
        f.write(f"SSE is {b9:.2f}")
def fonk2(b7):
    b11 = []
    for b14 in b7.T:
        b12 = b14.min()
        b13 = b14.max()
        b14 = (b14 - b12) / (b13 - b12)
        b11.append(b14)
    return np.array(b11).T
def fonk3(b8, b18):
    b11 = 0
    for i in range(len(b8)):
        b11 += np.linalg.norm(b8[i] - b18[i], 2)
    return b11
def fonk4(b7, b2):
    b15 = []
    b16 = set()
    for _ in range(b2):
        b17 = randint(0, len(b7) - 1)
        while b17 in b16:
            b17 = randint(0, len(b7) - 1)
        b15.append(b7[b17])
        b16.add(b17)
    b8 = np.array(b15)
    b18 = np.zeros(b8.shape)
    b19 = fonk3(b8, b18)
    b20 = np.zeros(len(b7))
    while b19 != 0:
        for i in range(len(b7)):
            b21 = []
            for j in range(len(b8)):
                b21.append(np.linalg.norm(b7[i] - b8[j], 2))
            b16 = np.argmin(b21)
            b20[i] = b16
        b18 = deepcopy(b8)
        for i in range(b2):
            if len(b7[b20 = = i]) > 0:
                b8[i] = np.mean(b7[b20 = = i], axis=0)
        b19 = fonk3(b8, b18)
    return b20, b8
def fonk5(b7, b2, b8, b10):
    b9 = 0
    for i in range(b2):
        for j in b7[b10 = = i]:
            b9 += np.linalg.norm(j - b8[i], 2) ** 2
    return b9
if b22 = = '__main__':
    fonk1()