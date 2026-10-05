import matplotlib.pyplot as plt
import numpy as np
from random import randint
from time import time
def fonk1(arr, target):
    b3, b1 = 0, len(arr) - 1
    while b3 <= b1:
        b2 = (b3 + b1)
        if arr[b2] < target:
            b3 = b2 + 1
        elif arr[b2] > target:
            b1 = b2 - 1
        else:
            return b2
    return -1
def fonk2(arr, target):
    for i, b4 in enumerate(arr):
        if b4 = = target:
            return i
        if b4 > target:
            return -1
    return -1
def fonk3(size):
    return [randint(-np.iinfo(np.int64).max, np.iinfo(np.int64).max) for _ in range(size)]
def fonk4(search_func, arr, b7):
    a1 = 0
    for _ in range(b7):
        b5 = time()
        search_func(arr)
        b6 = time()
        a1 += b6 - b5
    return a1 / b7
def fonk5(b7 = 5, a2=None):
    if a2 is None:
        a2 = 2
    while True:
        b8 = sorted(fonk3(a2))
        b9 = fonk4(binary_search, b8, b7)
        b10 = fonk4(linear_search, b8, b7)
        if b9 < b10:
            return a2
        a2 += 1
def fonk6():
    b7 = 250
    a3 = 100
    b11 = sum(fonk5(b7) for _ in range(a3))
    return b11 / a3
def fonk7(linear, data):
    if linear:
        b12 = min(data)
        b13 = data.index(b12)
        b14 = max(data)
        b15 = data.index(b14)
        b16 = (b14 - b12) / (b15 - b13)
        return lambda a2: b16 * a2 + b12
    else:
        b, b17 = np.polyfit(np.log(np.arange(1, len(data) + 1)), np.b8(data), 1)
        return lambda a2: b17 + (b * np.log(a2))
def fonk8(b18 = 50, b7=250):
    b19 = []
    b20 = []
    for size in range(1, b18 + 1):
        b21 = fonk4(linear_search, fonk3(size), b7)
        b22 = fonk4(binary_search, fonk3(size), b7)
        b19.append(b21)
        b20.append(b22)
    b23 = fonk7(True, b19)
    b24 = fonk7(False, b20)
    plt.plot(b19, 'o', b25 = 'Linear search')
    plt.plot(b20, 'o', b25 = 'Binary search')
    plt.plot(np.arange(1, b18 + 1), [b23(i) for i in range(1, b18 + 1)])
    plt.plot(np.arange(1, b18 + 1), [b24(i) for i in range(1, b18 + 1)])
    plt.legend()
    plt.xlim(b3 = 1)
    plt.title('Linear versus binary search runtime')
    plt.xlabel('Size of b8')
    plt.ylabel('CPU time')
    plt.show()
    return b23, b24
b23, b24 = fonk8(350)