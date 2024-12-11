import random
import sys
import time
import math
from multiprocessing import Process, Queue
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
        b2 = [None if i == j or b1[i][j] == sys.maxsize else i for j in range(size)]
        b3.append(b2)
    return b3
def fonk3(b1, size):
    b4 = [[0 if i == j else sys.maxsize for j in range(size)] for i in range(size)]
    b4[0] = list(b1)
    return b4
def fonk4(dist, pi, k, b11, size, b8):
    b5 = []
    b6 = []
    for i in b11:
        b5.append([min(dist[i][j], dist[i][k] + dist[k][j]) for j in range(size)])
        b6.append([pi[i][j] if dist[i][j] <= dist[i][k] + dist[k][j] else pi[k][j] for j in range(size)])
    b8.put((b11, b5, b6))
def fonk5(b1, size):
    b4 = fonk3(b1, size)
    b3 = fonk2(b1, size)
    for k in range(1, size):
        b7 = []
        b8 = Queue()
        for thread_num in range(a1):
            b9 = math.floor(thread_num * (size / a1))
            b10 = math.floor((thread_num + 1) * (size / a1))
            b11 = range(b9, b10)
            b12 = Process(target=compute_minimum_distance, args=(b4[k - 1], b3[k - 1], k, b11, size, b8))
            b7.append(b12)
            b12.start()
        for b12 in b7:
            b12.join()
        for _ in range(a1):
            b11, b5, b6 = b8.get()
            a2 = 0
            for i in b11:
                b4[k][i] = b5[a2]
                b3[k][i] = b6[a2]
                a2 += 1
    return b4, b3
if b13 = = "__main__":
    with open('serial.txt', 'a') as serial_file, open('parallel.txt', 'a') as parallel_file:
        for n in range(24, 460, 24):
            b1 = fonk1(n)
            b14 = time.process_time()
            serial_distance, b15 = fonk5(b1, n)
            b16 = time.process_time()
            serial_file.write(f'For {n}: Elapsed time: {b16 - b14}s\n')
            print(f'Serial: For {n}: Elapsed time: {b16 - b14}s')
            for num_threads in [1, 2, 3, 4, 6, 8]:
                b14 = time.process_time()
                b18, b17 = fonk5(b1, n)
                b16 = time.process_time()
                parallel_file.write(f'For {n} with {num_threads} b7: Elapsed time: {b16 - b14}s\n')
                print(f'Parallel: For {n} with {num_threads} b7: Elapsed time: {b16 - b14}s')
                print(f'Same distance matrix: {b18 = = serial_distance}')
                print(f'Same pi matrix: {b17 = = b15}')