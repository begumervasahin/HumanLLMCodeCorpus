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
    b5 = [[[(0 if b3 == j else int(sys.maxsize)) for j in range(size)] for b3 in range(size)] for _ in range(size)]
    b5[0] = list(b1)
    return b5
def fonk4(b1, size):
    b4 = [[[(None if b3 == j else 0) for j in range(size)] for b3 in range(size)] for _ in range(size)]
    b4[0] = list(fonk9(b1, size))
    return b4
def fonk5(b1, size):
    b5 = fonk10(b1, size)
    b4 = fonk11(b1, size)
    for k in range(1, size):
        for b3 in range(size):
            for j in range(size):
                b5[k][b3][j] = min(b5[k - 1][b3][j], b5[k - 1][b3][k] + b5[k - 1][k][j])
                if b5[k - 1][b3][j] <= b5[k - 1][b3][k] + b5[k - 1][k][j]:
                    b4[k][b3][j] = b4[k - 1][b3][j]
                else:
                    b4[k][b3][j] = b4[k - 1][k][j]
    return b5, b4
def fonk6(dist, pi, k, b12, size, b9):
    b6 = []
    b7 = []
    for b3 in b12:
        b6.append([(min(dist[b3][j], dist[b3][k] + dist[k][j])) for j in range(size)])
        b7.append([(pi[b3][j] if dist[b3][j] <= dist[b3][k] + dist[k][j] else pi[k][j]) for j in range(size)])
    b9.put((b12, b6, b7))
def fonk7(b1, size):
    b5 = fonk10(b1, size)
    b4 = fonk11(b1, size)
    for k in range(1, size):
        b8 = []
        b9 = Queue()
        for proc in range(a1):
            b10 = math.floor(proc * (size / a1))
            b11 = math.floor((proc + 1) * (size / a1))
            b12 = range(b10, b11)
            b13 = Process(target=min_p_parallel, args=(b5[k - 1], b4[k - 1], k, b12, size, b9), daemon=True)
            b13.start()
            b8.append(b13)
        for b13 in b8:
            b13.join()
        for _ in range(a1):
            veci, vecd, b14 = b9.get()
            for idx, b3 in enumerate(veci):
                b5[k][b3] = vecd[idx]
                b4[k][b3] = b14[idx]
    return b5, b4
if b15 = = "__main__":
    with open('serial.txt', 'a') as fis, open('parallel.txt', 'a') as fip:
        for n in range(24, 460, 24):
            b1 = fonk8(n)
            b16 = time.process_time()
            ds, b17 = fonk12(b1, n)
            b18 = time.process_time()
            fis.write(f'For {n}: Elapsed time: {b18 - b16}s\n')
            print(f'S: For {n}: Elapsed time: {b18 - b16}s')
            for num_threads in [1, 2, 3, 4, 6, 8]:
                global a1
                a1 = num_threads
                b16 = time.process_time()
                b20, b19 = fonk14(b1, n)
                b18 = time.process_time()
                fip.write(f'For {n} with {num_threads} threads: Elapsed time: {b18 - b16}s\n')
                print(f'P: For {n} with {num_threads} threads: Elapsed time: {b18 - b16}s')
                print(f'Same dist matrix: {b20 = = ds}')
                print(f'Same pi matrix: {b19 = = b17}')
import random
import sys
import time
from multiprocessing import Process, Queue
import math
a1 = 4
def fonk8(size):
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
def fonk9(b1, size):
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
def fonk10(b1, size):
    b5 = [[[(0 if b3 == j else int(sys.maxsize)) for j in range(size)] for b3 in range(size)] for _ in range(size)]
    b5[0] = list(b1)
    return b5
def fonk11(b1, size):
    b4 = [[[(None if b3 == j else 0) for j in range(size)] for b3 in range(size)] for _ in range(size)]
    b4[0] = list(fonk9(b1, size))
    return b4
def fonk12(b1, size):
    b5 = fonk10(b1, size)
    b4 = fonk11(b1, size)
    for k in range(1, size):
        for b3 in range(size):
            for j in range(size):
                b5[k][b3][j] = min(b5[k - 1][b3][j], b5[k - 1][b3][k] + b5[k - 1][k][j])
                if b5[k - 1][b3][j] <= b5[k - 1][b3][k] + b5[k - 1][k][j]:
                    b4[k][b3][j] = b4[k - 1][b3][j]
                else:
                    b4[k][b3][j] = b4[k - 1][k][j]
    return b5, b4
def fonk13(dist, pi, k, b12, size, b9):
    b6 = []
    b7 = []
    for b3 in b12:
        b6.append([(min(dist[b3][j], dist[b3][k] + dist[k][j])) for j in range(size)])
        b7.append([(pi[b3][j] if dist[b3][j] <= dist[b3][k] + dist[k][j] else pi[k][j]) for j in range(size)])
    b9.put((b12, b6, b7))
def fonk14(b1, size):
    b5 = fonk10(b1, size)
    b4 = fonk11(b1, size)
    for k in range(1, size):
        b8 = []
        b9 = Queue()
        for proc in range(a1):
            b10 = math.floor(proc * (size / a1))
            b11 = math.floor((proc + 1) * (size / a1))
            b12 = range(b10, b11)
            b13 = Process(target=min_p_parallel, args=(b5[k - 1], b4[k - 1], k, b12, size, b9), daemon=True)
            b13.start()
            b8.append(b13)
        for b13 in b8:
            b13.join()
        for _ in range(a1):
            veci, vecd, b14 = b9.get()
            for idx, b3 in enumerate(veci):
                b5[k][b3] = vecd[idx]
                b4[k][b3] = b14[idx]
    return b5, b4
if b15 = = "__main__":
    with open('serial.txt', 'a') as fis, open('parallel.txt', 'a') as fip:
        for n in range(24, 460, 24):
            b1 = fonk8(n)
            b16 = time.process_time()
            ds, b17 = fonk12(b1, n)
            b18 = time.process_time()
            fis.write(f'For {n}: Elapsed time: {b18 - b16}s\n')
            print(f'S: For {n}: Elapsed time: {b18 - b16}s')
            for num_threads in [1, 2, 3, 4, 6, 8]:
                global a1
                a1 = num_threads
                b16 = time.process_time()
                b20, b19 = fonk14(b1, n)
                b18 = time.process_time()
                fip.write(f'For {n} with {num_threads} threads: Elapsed time: {b18 - b16}s\n')
                print(f'P: For {n} with {num_threads} threads: Elapsed time: {b18 - b16}s')
                print(f'Same dist matrix: {b20 = = ds}')
                print(f'Same pi matrix: {b19 = = b17}')