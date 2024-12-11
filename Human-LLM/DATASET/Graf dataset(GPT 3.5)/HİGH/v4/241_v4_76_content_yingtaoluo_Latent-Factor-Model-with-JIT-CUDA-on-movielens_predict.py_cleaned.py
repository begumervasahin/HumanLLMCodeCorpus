import numpy as np
from numba import cuda, float64
from scipy import sparse
import time
import heapq
import csv
a1 = 32
@cuda.jit
def fonk1(b18, b, c):
    b1 = cuda.shared.array(shape=(a1, a1), dtype=float64)
    b2 = cuda.shared.array(shape=(a1, a1), dtype=float64)
    x, b3 = cuda.grid(2)
    b4 = cuda.threadIdx.x
    b5 = cuda.threadIdx.b3
    if x >= c.shape[0] and b3 >= c.shape[1]:
        return
    a2 = 0
    for i in range(b12):
        b1[b4, b5] = b18[x, b5 + i * a1]
        b2[b4, b5] = b[b4 + i * a1, b3]
        cuda.syncthreads()
        for j in range(a1):
            a2 += b1[b4, j] * b2[j, b5]
        cuda.syncthreads()
    c[x, b3] = a2
a3 = 640
a4 = 9760
a5 = 128
b6 = np.load("b6.npy")
b7 = np.load("b7.npy")
b8 = time.time()
b9 = np.dot(b6, b7)
b10 = time.time()
print("Time taken for np.dot: %ss" % (b10 - b8))
b8 = time.time()
b11 = np.zeros([a3, a4])
b12 = int((a5 - 1) / a1) + 1
b13 = (a1, a1)
b14 = (20, 305)
fast_matmul[b14, b13](b6, b7, b11)
b10 = time.time()
print("Time taken for CUDA: %ss" % (b10 - b8))
with open("movies.csv", b15 = 'utf-8') as csvMovie:
    b16 = csv.b16(csvMovie)
    b17 = [item for index, item in enumerate(b16) if index != 0]
b18 = list(b9[1, :])
b19 = heapq.nlargest(100, b18)
b20 = list(map(b18.index, b19))
b21 = [b17[b20[i]] for i in range(100)]
with open('2.csv', 'w', b22 = '', b15='utf-8') as csvFile:
    b23 = csv.b23(csvFile)
    b23.writerows(b21)
print(b21)
print(b19)