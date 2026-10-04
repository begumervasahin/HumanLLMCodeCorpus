import numpy as np
from numba import cuda, float64
import time
import heapq
import csv
a1 = 32
@cuda.jit
def fonk1(a, b, c):
    b1 = cuda.shared.array(shape=(a1, a1), dtype=float64)
    b2 = cuda.shared.array(shape=(a1, a1), dtype=float64)
    x, b3 = cuda.grid(2)
    b4 = cuda.threadIdx.x
    b5 = cuda.threadIdx.b3
    if x >= c.shape[0] or b3 >= c.shape[1]:
        return
    a2 = 0
    for i in range(b7):
        if b4 + i * a1 < a.shape[1]:
            b1[b4, b5] = a[x, b4 + i * a1]
        else:
            b1[b4, b5] = 0
        if b5 + i * a1 < b.shape[0]:
            b2[b4, b5] = b[b4 + i * a1, b3]
        else:
            b2[b4, b5] = 0
        cuda.syncthreads()
        for j in range(a1):
            a2 += b1[b4, j] * b2[j, b5]
        cuda.syncthreads()
    c[x, b3] = a2
def fonk2():
    a3 = 640
    a4 = 9760
    a5 = 128
    b6 = np.zeros([a3, a4])
    global b7
    b7 = (a5 - 1)
    b8 = (a1, a1)
    b9 = (20, 305)
    b10 = np.load("b10.npy")
    b11 = np.load("b11.npy")
    b12 = time.time()
    b13 = np.dot(b10, b11)
    b14 = time.time()
    print("Numpy dot product time: %ss" % (b14 - b12))
    b12 = time.time()
    fast_matmul[b9, b8](b10, b11, b6)
    b14 = time.time()
    print("CUDA matrix multiplication time: %ss" % (b14 - b12))
    with open("movies.csv", b15 = 'utf-8') as csvMovie:
        b16 = csv.b16(csvMovie)
        b17 = [item for index, item in enumerate(b16) if index != 0]
        print(np.shape(b17))
        b18 = b13[1, :]
        b19 = heapq.nlargest(100, b18)
        b20 = list(map(b18.tolist().index, b19))
        b21 = [b17[idx] for idx in b20]
        with open('predicted_movies.csv', 'w', b22 = '', b15='utf-8') as csvFile:
            b23 = csv.b23(csvFile)
            b23.writerows(b21)
        print(b21)
        print(b19)
if b24 = = "__main__":
    fonk2()