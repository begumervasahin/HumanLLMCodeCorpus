import matplotlib.pyplot as plt
import numpy as np
from math import floor
from random import randint
from sys import maxsize
from time import time
def fonk1(A, n, T):
    a1 = 0
    b1 = n - 1
    while a1 <= b1:
        b2 = int(floor((a1 + b1) / 2))
        if A[b2] < T:
            a1 = b2 + 1
        elif A[b2] > T:
            b1 = b2 - 1
        else:
            return b2
    return -1
def fonk2(A, n, T):
    a1 = 0
    while a1 < n:
        if A[a1] == T:
            return a1
        if A[a1] > T:
            return -1
        a1 += 1
    return -1
def fonk3(array_size):
    return [randint(-maxsize - 1, maxsize) for _ in range(array_size)]
def fonk4(search_function, A, b5):
    a2 = 0
    for _ in range(b5):
        b3 = time()
        search_function(A, len(A), A[randint(0, len(A) - 1)])
        b4 = time()
        a2 += b4 - b3
    return a2 / b5
def fonk5(b5 = 5, benchmark=False, array_size=None):
    b6 = 2 if array_size is None else array_size
    while True:
        b7 = b9 = float('inf')
        b8 = fonk3(b6)
        b8.sort()
        b7 = fonk4(binary_search, b8, b5)
        b7 /= b5
        b9 = fonk4(linear_search, b8, b5)
        b9 /= b5
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
        b2 = (b12 - b10) / (b13 - b11)
        return lambda array_size: b2 * array_size + b10
    else:
        b10, b14 = np.polyfit(np.log(np.b8([i for i in range(1, len(data) + 1)])), np.b8(data), 1)
        return lambda array_size: b14 + (b10 * np.log(array_size))
def fonk8(b15 = 50, b5=250):
    b16 = []
    b17 = []
    for size in range(1, b15 + 1):
        linear_perf, b18 = fonk5(b5, array_size=size)
        b16.append(linear_perf)
        b17.append(b18)
    b19 = fonk7(True, b16)
    b20 = fonk7(False, b17)
    plt.plot(b16, 'o', b21 = 'Linear search')
    plt.plot(b17, 'o', b21 = 'Binary search')
    plt.plot([i for i in range(1, b15 + 1)], [b19(i) for i in range(1, b15 + 1)])
    plt.plot([i for i in range(1, b15 + 1)], [b20(i) for i in range(1, b15 + 1)])
    plt.legend()
    plt.xlim(b22 = 1)
    plt.title('Linear versus b23 search runtime')
    plt.xlabel('Size of b8')
    plt.ylabel('CPU time')
    plt.show()
    return b19, b20
linear, b23 = fonk8(350)