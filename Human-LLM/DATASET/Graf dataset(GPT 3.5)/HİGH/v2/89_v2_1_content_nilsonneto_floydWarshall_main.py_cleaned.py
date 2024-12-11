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
def fonk2(b1, size):
    b4 = []
    for b3 in range(size):
        b2 = []
        for j in range(size):
            if b3 = = j or b1[b3][j] == sys.maxsize:
                b2.append(None)
            elif b3 != j and b1[b3][j] < sys.maxsize:
                b2.append(b3)
            else:
                b2.append(-1)
        b4.append(b2)
    return b4
def fonk3(b1, size):
    b5 = [[0 if b3 == j else int(sys.maxsize) for j in range(size)] for b3 in range(size)]
    for b3 in range(size):
        for j in range(size):
            b5[b3][j] = b1[b3][j]
    return b5
def fonk4(b1, size):
    b6 = [[None if b3 == j else 0 for j in range(size)] for b3 in range(size)]
    for b3 in range(size):
        for j in range(size):
            if b1[b3][j] != sys.maxsize:
                b6[b3][j] = b3
    return b6
def fonk5(b1, size):
    b5 = fonk3(b1, size)
    b6 = fonk4(b1, size)
    for k in range(size):
        for b3 in range(size):
            for j in range(size):
                b5[b3][j] = min(b5[b3][j], b5[b3][k] + b5[k][j])
                if b5[b3][j] == b5[b3][k] + b5[k][j]:
                    b6[b3][j] = b6[k][j]
    return b5, b6
def fonk6(b5, b6, k, b13, size, b10):
    b7 = []
    b8 = []
    for b3 in b13:
        b7.append([min(b5[b3][j], b5[b3][k] + b5[k][j]) for j in range(size)])
        b8.append([b6[b3][j] if b5[b3][j] <= b5[b3][k] + b5[k][j] else b6[k][j] for j in range(size)])
    b10.put((b13, b7, b8))
def fonk7(b1, size):
    b5 = fonk3(b1, size)
    b6 = fonk4(b1, size)
    for k in range(size):
        b9 = []
        b10 = Queue()
        for proc in range(a1):
            b11 = math.floor(proc * (size / a1))
            b12 = math.floor((proc + 1) * (size / a1))
            b13 = range(b11, b12)
            b14 = Process(target=min_p_parallel, args=(b5, b6, k, b13, size, b10))
            b14.start()
            b9.append(b14)
        for b14 in b9:
            b14.join()
        for _ in range(a1):
            indices, b7, b8 = b10.get()
            a2 = 0
            for b3 in indices:
                b5[b3] = list(b7[a2])
                b6[b3] = list(b8[a2])
                a2 += 1
    return b5, b6
if b15 = = "__main__":
    for size in range(24, 460, 24):
        b1 = fonk1(size)
        b16 = time.process_time()
        serial_distance, b17 = fonk5(b1, size)
        b18 = time.process_time()
        print('Serial: For size %s: Elapsed time: %ss' % (size, str(b18 - b16)))
        for num_threads in [1, 2, 3, 4, 6, 8]:
            a1 = num_threads
            b16 = time.process_time()
            b20, b19 = fonk7(b1, size)
            b18 = time.process_time()
            print('Parallel: For size %s with %s threads: Elapsed time: %ss' % (size, num_threads, str(b18 - b16)))
            print('Same b5 matrix: %s' % (b20 = = serial_distance))
            print('Same previous vertex matrix: %s' % (b19 = = b17))