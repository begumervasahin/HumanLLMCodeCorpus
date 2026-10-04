import random as rd
import numpy as np
import time
from Graph import Graph
def fonk1(b8, b6):
    a1 = 0
    for i in range(len(b8) - 1):
        a1 += b6.costs[b8[i], b8[i + 1]]
    return a1
def fonk2(sol1, sol2, b6):
    return fonk1(sol1, b6) - fonk1(sol2, b6)
def fonk3(b8, b6, a4):
    b1 = fonk4(b8)
    b2 = fonk2(b1, b8, b6)
    if b2 < 0:
        return b1
    else:
        b3 = np.exp(-b2 / a4)
        if rd.random() < b3:
            return b1
        else:
            return b8
def fonk4(b8):
    b1 = b8.copy()
    b4 = list(range(1, len(b8) - 2))
    i, b5 = rd.sample(b4, 2)
    b1[i], b1[b5] = b1[b5], b1[i]
    return b1
def fonk5():
    a2 = 17
    b6 = Graph("N17.data")
    a1 = 0
    a3 = 0
    for _ in range(10):
        b7 = [i for i in range(1, a2)]
        rd.shuffle(b7)
        b8 = [0] + b7 + [0]
        a4 = 1000
        b9 = time.time()
        while a4 > 5:
            for _ in range(a2 ** 2):
                b8 = fonk3(b8, b6, a4)
            a4 *= 0.98
        b10 = time.time() - b9
        print(b8)
        a1 += fonk1(b8, b6)
        a3 += b10
    print(f"Average cost: {a1 / 10}")
    print(f"Average time: {a3 / 10:.2f} seconds")
if b11 = = '__main__':
    fonk5()