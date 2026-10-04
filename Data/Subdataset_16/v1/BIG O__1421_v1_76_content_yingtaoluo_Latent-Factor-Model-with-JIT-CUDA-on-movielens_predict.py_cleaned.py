import numpy as np
from numba import cuda, float64
from scipy import sparse
import time
import heapq
import csv
import pandas as pd
a1 = 32
@cuda.jit
def fonk1(b18, b, c, b6):
    b1 = cuda.shared.array(shape=(a1, a1), dtype=float64)
    b2 = cuda.shared.array(shape=(a1, a1), dtype=float64)
    x, b3 = cuda.grid(2)
    b4 = cuda.threadIdx.x
    b5 = cuda.threadIdx.b3
    if x >= c.shape[0] or b3 >= c.shape[1]:
        return
    a2 = 0
    for i in range(b6):
        b1[b4, b5] = b18[x, b5 + i * a1]
        b2[b4, b5] = b[b4 + i * a1, b3]
        cuda.syncthreads()
        for j in range(a1):
            a2 += b1[b4, j] * b2[j, b5]
        cuda.syncthreads()
    c[x, b3] = a2
def fonk2():
    a3 = 640
    a4 = 9760
    a5 = 128
    b6 = (a5 - 1)
    b7 = np.load("b7.npy")
    b8 = np.load("b8.npy")
    b9 = np.zeros((a3, a4))
    b10 = (a1, a1)
    b11 = ((a3 - 1)
    b12 = time.time()
    b13 = np.dot(b7, b8)
    b14 = time.time()
    print("np.dot elapsed time: {}s".format(b14 - b12))
    b12 = time.time()
    fast_matmul[b11, b10](b7, b8, b9, b6)
    b14 = time.time()
    print("CUDA elapsed time: {}s".format(b14 - b12))
    with open("movies.csv", b15 = 'utf-8') as csvMovie:
        b16 = csv.b16(csvMovie)
        b17 = [item for index, item in enumerate(b16) if index != 0]
    print("Shape of movie b17:", np.shape(b17))
    b18 = list(b13[1, :])
    b19 = heapq.nlargest(100, b18)
    b20 = list(map(b18.index, b19))
    b21 = [b17[b20[i]] for i in range(100)]
    with open('2.csv', 'w', b22 = '', b15='utf-8') as csvFile:
        b23 = csv.b23(csvFile)
        for item in b21:
            b23.writerow(item)
    print("Top 100 movie predictions saved to '2.csv'")
    print(b21)
    print(b19)
if b24 = = "__main__":
    fonk2()