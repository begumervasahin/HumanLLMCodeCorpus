import numpy as np
import ascent as asc
from math import ceil
from random import random as rd
from random import randint as ri
asc.b1 = 'DB24-glass/TRAIN.TXT'
asc.b2 = 'DB24-glass/TEST.TXT'
asc.b3 = False
asc.a1 = 1e-6
a2 = 1.0
a3 = 0.05
a4 = 100
a5 = 100
a6 = 5
a7 = 9
a8 = 3
b4 = a6 * a7 * ceil(np.log2(a8))
b5 = round(b4 * a5 * a3)
def fonk1():
    global b4
    global b5
    b4 = a6 * a7 * ceil(np.log2(a8))
    b5 = round(b4 * a5 * a3)
def fonk2():
    b6 = np.random.choice([0, 1], size=a5 * b4, b19=[0.5, 0.5])
    return b6.reshape(a5, b4)
def fonk3(individual):
    b7 = []
    b8 = ceil(np.log2(a8))
    b9 = a7 * b8
    for t in range(a6):
        b10 = []
        b11 = t * b9
        b12 = ''.join(map(str, individual[b11:b11 + b9]))
        for v in range(a7):
            b13 = v * b8
            b14 = int(b12[b13:b13 + b8], 2)
            b10.append(b14)
        b7.append(b10)
    return np.array(b7)
def fonk4(b23):
    b15 = []
    for ind in b23:
        b16 = fonk3(ind)
        asc.b17 = b16
        asc.set()
        C, trn_rms, b18 = asc.fonk7()
        b15.append(b18)
    return np.array(b15)
def fonk5(b23):
    for i in range(a5
        if rd() <= a2:
            b19 = ri(1, b4
            b20 = b23[i, b19:].copy()
            b23[i, b19:] = b23[a5 - i - 1, b19:]
            b23[a5 - i - 1, b19:] = b20
    return b23
def fonk6(b23):
    for _ in range(b5):
        b21 = ri(0, b4 - 1)
        b22 = ri(0, a5 - 1)
        b23[b22, b21] = 1 - b23[b22, b21]
    return b23
def fonk7():
    asc.set()
    b23 = fonk2()
    b15 = fonk4(b23)
    for g in range(a4):
        b23 = np.tile(b23[:a5], (2, 1))
        b15 = np.tile(b15[:a5], 2)
        b23 = fonk5(b23)
        b23 = fonk6(b23)
        b15[:a5] = fonk4(b23[:a5])
        b24 = np.argsort(b15)
        b15 = b15[b24]
        b23 = b23[b24]
        print(f"gen[{g + 1}] best b15 = {b15[0]:.6f}\t worst b15 = {b15[a5 - 1]:.6f}")
    return fonk3(b23[0]), b15[0]
b16, b25 = fonk7()
asc.b17 = b16
asc.set()
C, trn_rms, b18 = asc.fonk7()
print("b16")
print(b16)
print("coefficients")
print(C)
print("train b26 = ")
print(trn_rms)
print("test b26 = ")
print(b18)