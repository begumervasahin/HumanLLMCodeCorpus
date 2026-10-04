import random
import sys
import time
from multiprocessing import Process, Queue
import math
a1 = 4
def fonk1(size):
    return [[0 if b1 = = j else random.randint(2, 30) for j in range(size)] for b1 in range(size)]
def fonk2(b16, size):
    b2 = []
    for b1 in range(size):
        b3 = []
        for j in range(size):
            if b1 = = j or b16[b1][j] == sys.maxsize:
                b3.append(None)
            elif b16[b1][j] < sys.maxsize:
                b3.append(b1)
            else:
                b3.append(-1)
        b2.append(b3)
    return b2
def fonk3(b16, size):
    b4 = [[[(0 if b1 == j else sys.maxsize) for j in range(size)] for b1 in range(size)] for _ in range(size)]
    b4[0] = list(b16)
    return b4
def fonk4(b16, size):
    b2 = [[[(None if b1 == j else 0) for j in range(size)] for b1 in range(size)] for _ in range(size)]
    b2[0] = list(fonk2(b16, size))
    return b2
def fonk5(b16, size):
    b4 = fonk3(b16, size)
    b2 = fonk4(b16, size)
    for k in range(1, size):
        for b1 in range(size):
            for j in range(size):
                b5 = b4[k - 1][b1][k] + b4[k - 1][k][j]
                if b5 < b4[k - 1][b1][j]:
                    b4[k][b1][j] = b5
                    b2[k][b1][j] = b2[k - 1][k][j]
                else:
                    b4[k][b1][j] = b4[k - 1][b1][j]
                    b2[k][b1][j] = b2[k - 1][b1][j]
    return b4, b2
def fonk6(dist, pi, k, b12, size, b9):
    b6 = []
    b7 = []
    for b1 in b12:
        b6.append([min(dist[b1][j], dist[b1][k] + dist[k][j]) for j in range(size)])
        b7.append([pi[b1][j] if dist[b1][j] <= dist[b1][k] + dist[k][j] else pi[k][j] for j in range(size)])
    b9.put((b12, b6, b7))
def fonk7(b16, size):
    b4 = fonk3(b16, size)
    b2 = fonk4(b16, size)
    for k in range(1, size):
        b8 = []
        b9 = Queue()
        for proc in range(a1):
            b10 = math.floor(proc * (size / a1))
            b11 = math.floor((proc + 1) * (size / a1))
            b12 = range(b10, b11)
            b13 = Process(target=min_p_parallel, args=(b4[k - 1], b2[k - 1], k, b12, size, b9), daemon=True)
            b13.start()
            b8.append(b13)
        for b13 in b8:
            b13.join()
        for _ in range(a1):
            veci, vecd, b14 = b9.get()
            for idx, b1 in enumerate(veci):
                b4[k][b1] = vecd[idx]
                b2[k][b1] = b14[idx]
    return b4, b2
if b15 = = "__main__":
    with open('serial.txt', 'a') as fis, open('parallel.txt', 'a') as fip:
        for n in range(24, 460, 24):
            b16 = fonk1(n)
            b17 = time.process_time()
            ds, b18 = fonk5(b16, n)
            b19 = time.process_time()
            fis.write(f'For {n}: Elapsed time: {b19 - b17}s\n')
            print(f'S: For {n}: Elapsed time: {b19 - b17}s')
            for num_threads in [1, 2, 3, 4, 6, 8]:
                global a1
                a1 = num_threads
                b17 = time.process_time()
                b21, b20 = fonk7(b16, n)
                b19 = time.process_time()
                fip.write(f'For {n} with {num_threads} threads: Elapsed time: {b19 - b17}s\n')
                print(f'P: For {n} with {num_threads} threads: Elapsed time: {b19 - b17}s')
                print(f'Same dist matrix: {b21 = = ds}')
                print(f'Same pi matrix: {b20 = = b18}')