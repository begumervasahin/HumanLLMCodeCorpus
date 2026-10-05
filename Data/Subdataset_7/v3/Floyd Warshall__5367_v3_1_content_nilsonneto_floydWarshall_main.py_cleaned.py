import random
import sys
import time
from multiprocessing import Process, Queue
import math
a1 = 4
def fonk1(size):
    b1 = []
    for i in range(size):
        b2 = [0 if i == j else random.randint(2, 30) for j in range(size)]
        b1.append(b2)
    return b1
def fonk2(b1, size):
    b3 = []
    for i in range(size):
        b2 = [None if i == j or b1[i][j] == sys.maxsize else i if b1[i][j] < sys.maxsize else -1 for j in range(size)]
        b3.append(b2)
    return b3
def fonk3(b1, size):
    b4 = [[0 if i == j else b1[i][j] for j in range(size)] for i in range(size)]
    return b4
def fonk4(b1, size):
    b5 = [[None if i == j else i if b1[i][j] != sys.maxsize else 0 for j in range(size)] for i in range(size)]
    return b5
def fonk5(b1, size):
    b4 = fonk3(b1, size)
    b5 = fonk4(b1, size)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                b6 = b4[i][k] + b4[k][j]
                if b6 < b4[i][j]:
                    b4[i][j] = b6
                    b5[i][j] = b5[k][j]
    return b4, b5
def fonk6(b4, b5, k, b13, size, b10):
    b7 = []
    b8 = []
    for i in b13:
        b7.append([min(b4[i][j], b4[i][k] + b4[k][j]) for j in range(size)])
        b8.append([b5[i][j] if b4[i][j] <= b4[i][k] + b4[k][j] else b5[k][j] for j in range(size)])
    b10.put((b13, b7, b8))
def fonk7(b1, size):
    b4 = fonk3(b1, size)
    b5 = fonk4(b1, size)
    for k in range(size):
        b9 = []
        b10 = Queue()
        for proc in range(a1):
            b11 = math.floor(proc * (size / a1))
            b12 = math.floor((proc + 1) * (size / a1))
            b13 = range(b11, b12)
            b14 = Process(target=min_p_parallel, args=(b4, b5, k, b13, size, b10))
            b14.start()
            b9.append(b14)
        for b14 in b9:
            b14.join()
        for _ in range(a1):
            indices, b7, b8 = b10.get()
            for i in indices:
                b4[i] = list(b7[i - indices[0]])
                b5[i] = list(b8[i - indices[0]])
    return b4, b5
if b15 = = "__main__":
    for size in range(24, 460, 24):
        b1 = fonk1(size)
        b16 = time.process_time()
        serial_distance, b17 = fonk5(b1, size)
        b18 = time.process_time()
        print('Serial: For size %s: Elapsed time: %ss' % (size, b18 - b16))
        for num_threads in [1, 2, 3, 4, 6, 8]:
            a1 = num_threads
            b16 = time.process_time()
            b20, b19 = fonk7(b1, size)
            b18 = time.process_time()
            print('Parallel: For size %s with %s threads: Elapsed time: %ss' % (size, num_threads, b18 - b16))
            print('Same b4 matrix: %s' % (b20 = = serial_distance))
            print('Same previous vertex matrix: %s' % (b19 = = b17))