import random
import sys
import time
from multiprocessing import Process, Array, Queue
from threading import Lock, Thread
import math
b1 = 'Nilson'
a1 = 4
def fonk1(size):
    b2 = []
    for b4 in range(size):
        b3 = []
        for j in range(size):
            if b4 = = j:
                b3.append(0)
            else:
                b3.append(random.randint(2, 30))
        b2.append(b3)
    return b2
def fonk2(weights, size):
    b2 = []
    for b4 in range(size):
        b3 = []
        for j in range(size):
            if b4 = = j or weights[b4][j] == sys.maxsize:
                b3.append(None)
            elif b4 != j and weights[b4][j] < sys.maxsize:
                b3.append(b4)
            else:
                b3.append(-1)
        b2.append(b3)
    return b2
def fonk3(weights, size):
    b5 = [[[(0 if __ == ___ else int(sys.maxsize)) for __ in range(size)] for __ in range(size)] for ___ in range(size)]
    b5[0] = list(weights)
    return b5
def fonk4(weights, size):
    b5 = [[[(None if __ == ___ else 0) for __ in range(size)] for __ in range(size)] for ___ in range(size)]
    b5[0] = list(fonk2(weights, size))
    return b5
def fonk5(weights, size):
    b5 = fonk3(weights, size)
    b6 = fonk4(weights, size)
    for k in range(1, size):
        for b4 in range(size):
            for j in range(size):
                b5[k][b4][j] = min(b5[k - 1][b4][j], b5[k - 1][b4][k] + b5[k - 1][k][j])
                if b5[k - 1][b4][j] <= b5[k - 1][b4][k] + b5[k - 1][k][j]:
                    b6[k][b4][j] = b6[k - 1][b4][j]
                else:
                    b6[k][b4][j] = b6[k - 1][k][j]
    return b5, b6
def fonk6(b9, b10, k, b15, size, b12):
    b7 = []
    b8 = []
    for b4 in b15:
        b7.append([(min(b9[b4][j], b9[b4][k] + b9[k][j])) for j in range(size)])
        b8.append([(b10[b4][j] if b9[b4][j] <= b9[b4][k] + b9[k][j] else b10[k][j]) for j in range(size)])
    b12.put((b15, b7, b8))
def fonk7(weights, size):
    b9 = fonk3(weights, size)
    b10 = fonk4(weights, size)
    for k in range(1, size):
        b11 = []
        b12 = Queue()
        for pro in range(a1):
            b13 = math.floor(pro * (size / a1))
            b14 = math.floor((pro + 1) * (size / a1))
            b15 = range(b13, b14)
            b16 = Process(target=min_p_parallel, args=(b9[k - 1], b10[k - 1], k, b15, size, b12), daemon=True).b22()
            b11.append(b16)
        for b16 in b11:
            try:
                b16.join()
            except AttributeError:
                pass
        for v in range(a1):
            veci, vecd, b17 = b12.get()
            a2 = 0
            for b4 in veci:
                b9[k][b4] = list(vecd[a2])
                b10[k][b4] = list(b17[a2])
                a2 += 1
    return b9, b10
if b18 = = "__main__":
    b19 = open('serial.txt', 'a')
    b20 = open('parallel.txt', 'a')
    global a1
    for n in range(24, 460, 24):
        b21 = fonk1(n)
        b22 = time.process_time()
        ds, b23 = fonk5(b21, n)
        b24 = time.process_time()
        b19.write('For %s: Elapsed time: %ss\n' % (n, str(b24-b22)))
        print('S: For %s: Elapsed time: %ss' % (n, str(b24-b22)))
        for a1 in [1, 2, 3, 4, 6, 8]:
            b22 = time.process_time()
            b26, b25 = fonk7(b21, n)
            b24 = time.process_time()
            b20.write('For %s with %s threads: Elapsed time: %ss\n' % (n, a1, str(b24-b22)))
            print('P: For %s with %s threads: Elapsed time: %ss' % (n, a1, str(b24-b22)))
            print('Same b9 matrix: %s' % (b26 = = ds))
            print('Same b10 matrix: %s' % (b25 = = b23))