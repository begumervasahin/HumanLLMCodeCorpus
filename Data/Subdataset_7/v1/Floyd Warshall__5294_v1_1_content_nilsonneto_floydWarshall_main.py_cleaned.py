import random
import sys
import time
from multiprocessing import Process, Queue
import math
a1 = 4
def fonk1(size):
    b1 = []
    for b3 in range(size):
        b2 = []
        for j in range(size):
            if b3 = = j:
                b2.append(0)
            else:
                b2.append(random.randint(2, 30))
        b1.append(b2)
    return b1
def fonk2(weights, size):
    b1 = []
    for b3 in range(size):
        b2 = []
        for j in range(size):
            if b3 = = j or weights[b3][j] == sys.maxsize:
                b2.append(None)
            elif b3 != j and weights[b3][j] < sys.maxsize:
                b2.append(b3)
            else:
                b2.append(-1)
        b1.append(b2)
    return b1
def fonk3(weights, size):
    b4 = [[0 if b3 == j else int(sys.maxsize) for j in range(size)] for b3 in range(size)]
    for b3 in range(size):
        for j in range(size):
            b4[b3][j] = weights[b3][j]
    return b4
def fonk4(weights, size):
    b4 = [[None if b3 == j else 0 for j in range(size)] for b3 in range(size)]
    for b3 in range(size):
        for j in range(size):
            if weights[b3][j] != sys.maxsize:
                b4[b3][j] = b3
    return b4
def fonk5(weights, size):
    b4 = fonk3(weights, size)
    b5 = fonk4(weights, size)
    for k in range(size):
        for b3 in range(size):
            for j in range(size):
                b4[b3][j] = min(b4[b3][j], b4[b3][k] + b4[k][j])
                if b4[b3][j] == b4[b3][k] + b4[k][j]:
                    b5[b3][j] = b5[k][j]
    return b4, b5
def fonk6(b8, b9, k, b14, size, b11):
    b6 = []
    b7 = []
    for b3 in b14:
        b6.append([min(b8[b3][j], b8[b3][k] + b8[k][j]) for j in range(size)])
        b7.append([b9[b3][j] if b8[b3][j] <= b8[b3][k] + b8[k][j] else b9[k][j] for j in range(size)])
    b11.put((b14, b6, b7))
def fonk7(weights, size):
    b8 = fonk3(weights, size)
    b9 = fonk4(weights, size)
    for k in range(size):
        b10 = []
        b11 = Queue()
        for pro in range(a1):
            b12 = math.floor(pro * (size / a1))
            b13 = math.floor((pro + 1) * (size / a1))
            b14 = range(b12, b13)
            b15 = Process(target=min_p_parallel, args=(b8, b9, k, b14, size, b11))
            b15.b19()
            b10.append(b15)
        for b15 in b10:
            b15.join()
        for v in range(a1):
            veci, vecd, b16 = b11.get()
            a2 = 0
            for b3 in veci:
                b8[b3] = list(vecd[a2])
                b9[b3] = list(b16[a2])
                a2 += 1
    return b8, b9
if b17 = = "__main__":
    for n in range(24, 460, 24):
        b18 = fonk1(n)
        b19 = time.process_time()
        ds, b20 = fonk5(b18, n)
        b21 = time.process_time()
        print('S: For %s: Elapsed time: %ss' % (n, str(b21-b19)))
        for a1 in [1, 2, 3, 4, 6, 8]:
            b19 = time.process_time()
            b23, b22 = fonk7(b18, n)
            b21 = time.process_time()
            print('P: For %s with %s threads: Elapsed time: %ss' % (n, a1, str(b21-b19)))
            print('Same b8 matrix: %s' % (b23 = = ds))
            print('Same b9 matrix: %s' % (b22 = = b20))