import random
import numpy as np
import time
from Graph import Graph
def fonk1(b8, b12):
    return sum(b12.costs[b8[i], b8[i + 1]] for i in range(len(b8) - 1))
def fonk2(sol1, sol2, b12):
    return fonk1(sol1, b12) - fonk1(sol2, b12)
def fonk3(b8, b12, b9):
    b1 = fonk4(b8)
    b2 = fonk2(b1, b8, b12)
    if b2 < 0:
        return b1
    b3 = np.exp(-b2 / b9)
    return b1 if random.random() < b3 else b8
def fonk4(b8):
    b1 = b8.copy()
    b4 = range(1, len(b8) - 2)
    i, b5 = random.sample(b4, 2)
    b1[i], b1[b5] = b1[b5], b1[i]
    return b1
def fonk5(b12, a1, b6 = 1000, cooling_rate=0.98, min_temperature=5):
    b7 = list(range(1, a1))
    random.shuffle(b7)
    b8 = [0] + b7 + [0]
    b9 = b6
    b10 = time.time()
    while b9 > min_temperature:
        for _ in range(a1 ** 2):
            b8 = fonk3(b8, b12, b9)
        b9 *= cooling_rate
    b11 = time.time() - b10
    return b8, fonk1(b8, b12), b11
def fonk6():
    a1 = 17
    b12 = Graph("N17.data")
    a2 = 0
    a3 = 0
    for _ in range(10):
        b8, cost, b11 = fonk5(b12, a1)
        print(f"Solution: {b8}")
        a2 += cost
        a3 += b11
    print(f"Average cost: {a2 / 10}")
    print(f"Average time: {a3 / 10:.2f} seconds")
if b13 = = '__main__':
    fonk6()