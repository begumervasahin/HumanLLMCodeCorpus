import matplotlib.pyplot as plt
import numpy as np
from math import floor
from random import randint
from sys import maxsize
from time import time
def fonk1(b8, size, target):
    a1 = 0
    b1 = size - 1
    while a1 <= b1:
        b2 = int(floor((a1 + b1) / 2))
        if b8[b2] < target:
            a1 = b2 + 1
        elif b8[b2] > target:
            b1 = b2 - 1
        else:
            return b2
    return -1
def fonk2(b8, size, target):
    for i in range(size):
        if b8[i] == target:
            return i
        if b8[i] > target:
            return -1
    return -1
def fonk3(size):
    return [randint(-maxsize - 1, maxsize) for _ in range(size)]
def fonk4(search_func, b8, b5):
    a2 = 0
    for _ in range(b5):
        b3 = time()
        search_func(b8, len(b8), b8[randint(0, len(b8) - 1)])
        b4 = time()
        a2 += b4 - b3
    return a2 / b5
def fonk5(b5 = 5, benchmark=False, array_size=None):
    b6 = 2 if array_size is None else array_size
    while True:
        b7 = b9 = float('inf')
        b8 = fonk3(b6)
        b8.sort()
        b7 = fonk4(binary_search, b8, b5) / b5
        b9 = fonk4(linear_search, b8, b5) / b5
        if not benchmark:
            return b9, b7
        if benchmark and b7 < b9:
            return b6
        b6 += 1
def fonk6():
    return sum(fonk5(250, True) for _ in range(100)) / 100
def fonk7(linear, data):
    if linear:
        b10 = min(data)
        b11 = data.index(b10)
        b12 = max(data)
        b13 = data.index(b12)
        b14 = (b12 - b10) / (b13 - b11)
        return lambda array_size: b14 * array_size + b10
    else:
        b10, b15 = np.polyfit(np.log(np.array([i for i in range(1, len(data) + 1)])), np.array(data), 1)
        return lambda array_size: b15 + (b10 * np.log(array_size))
def fonk8(b16 = 50, b5=250):
    b17 = []
    b18 = []
    for size in range(1, b16 + 1):
        linear_perf, b19 = fonk5(b5, array_size=size)
        b17.append(linear_perf)
        b18.append(b19)
    b20 = fonk7(True, b17)
    b21 = fonk7(False, b18)
    plt.plot(b17, 'o', b22 = 'Linear search')
    plt.plot(b18, 'o', b22 = 'Binary search')
    plt.plot([i for i in range(1, b16 + 1)], [b20(i) for i in range(1, b16 + 1)])
    plt.plot([i for i in range(1, b16 + 1)], [b21(i) for i in range(1, b16 + 1)])
    plt.legend()
    plt.xlim(a1 = 1)
    plt.title('Linear versus binary search runtime')
    plt.xlabel('Size of array')
    plt.ylabel('CPU time')
    plt.show()
    return b20, b21
b20, b21 = fonk8(350)