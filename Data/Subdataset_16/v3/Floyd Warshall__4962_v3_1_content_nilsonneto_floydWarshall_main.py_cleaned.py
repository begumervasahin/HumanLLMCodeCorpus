import random
import sys
import time
from multiprocessing import Process, Queue
import math
a1 = 4
def fonk1(size):
    b1 = []
    for b4 in range(size):
        b2 = [0 if b4 == j else random.randint(2, 30) for j in range(size)]
        b1.append(b2)
    return b1
def fonk2(b1, size):
    b3 = []
    for b4 in range(size):
        b2 = []
        for j in range(size):
            if b4 = = j or b1[b4][j] == sys.maxsize:
                b2.append(None)
            elif b1[b4][j] < sys.maxsize:
                b2.append(b4)
            else:
                b2.append(-1)
        b3.append(b2)
    return b3
def fonk3(b1, size):
    b5 = [[[(0 if b4 == j else sys.maxsize) for j in range(size)] for b4 in range(size)] for _ in range(size)]
    b5[0] = list(b1)
    return b5
def fonk4(b1, size):
    b3 = [[[(None if b4 == j else 0) for j in range(size)] for b4 in range(size)] for _ in range(size)]
    b3[0] = list(fonk2(b1, size))
    return b3
def fonk5(b1, size):
    b5 = fonk3(b1, size)
    b3 = fonk4(b1, size)
    for k in range(1, size):
        for b4 in range(size):
            for j in range(size):
                b6 = b5[k - 1][b4][k] + b5[k - 1][k][j]
                if b6 < b5[k - 1][b4][j]:
                    b5[k][b4][j] = b6
                    b3[k][b4][j] = b3[k - 1][k][j]
                else:
                    b5[k][b4][j] = b5[k - 1][b4][j]
                    b3[k][b4][j] = b3[k - 1][b4][j]
    return b5, b3
def fonk6(dist, pi, k, b13, size, b10):
    b7 = []
    b8 = []
    for b4 in b13:
        b7.append([(min(dist[b4][j], dist[b4][k] + dist[k][j])) for j in range(size)])
        b8.append([(pi[b4][j] if dist[b4][j] <= dist[b4][k] + dist[k][j] else pi[k][j]) for j in range(size)])
    b10.put((b13, b7, b8))
def fonk7(b1, size):
    b5 = fonk3(b1, size)
    b3 = fonk4(b1, size)
    for k in range(1, size):
        b9 = []
        b10 = Queue()
        for proc in range(a1):
            b11 = math.floor(proc * (size / a1))
            b12 = math.floor((proc + 1) * (size / a1))
            b13 = range(b11, b12)
            b14 = Process(target=min_p_parallel, args=(b5[k - 1], b3[k - 1], k, b13, size, b10), daemon=True)
            b14.start()
            b9.append(b14)
        for b14 in b9:
            b14.join()
        for _ in range(a1):
            veci, vecd, b15 = b10.get()
            for idx, b4 in enumerate(veci):
                b5[k][b4] = vecd[idx]
                b3[k][b4] = b15[idx]
    return b5, b3
if b16 = = "__main__":
    with open('serial.txt', 'a') as fis, open('parallel.txt', 'a') as fip:
        for n in range(24, 460, 24):
            b1 = fonk1(n)
            b17 = time.process_time()
            ds, b18 = fonk5(b1, n)
            b19 = time.process_time()
            fis.write(f'For {n}: Elapsed time: {b19 - b17}s\n')
            print(f'S: For {n}: Elapsed time: {b19 - b17}s')
            for num_threads in [1, 2, 3, 4, 6, 8]:
                global a1
                a1 = num_threads
                b17 = time.process_time()
                b21, b20 = fonk7(b1, n)
                b19 = time.process_time()
                fip.write(f'For {n} with {num_threads} threads: Elapsed time: {b19 - b17}s\n')
                print(f'P: For {n} with {num_threads} threads: Elapsed time: {b19 - b17}s')
                print(f'Same dist matrix: {b21 = = ds}')
                print(f'Same pi matrix: {b20 = = b18}')