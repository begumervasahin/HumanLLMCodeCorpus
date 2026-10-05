import numpy as np
from numba import cuda, float64
import time
import heapq
import csv
TPB = 32
@cuda.jit
def fast_matmul(a, b, c):
    sa = cuda.shared.array(shape=(TPB, TPB), dtype=float64)
    sb = cuda.shared.array(shape=(TPB, TPB), dtype=float64)
    x, y = cuda.grid(2)
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    if x >= c.shape[0] and y >= c.shape[1]:
        return
    tmp = 0
    for i in range(hid):
        sa[tx, ty] = a[x, ty + i * TPB]
        sb[tx, ty] = b[tx + i * TPB, y]
        cuda.syncthreads()
        for j in range(TPB):
            tmp += sa[tx, j] * sb[j, ty]
        cuda.syncthreads()
    c[x, y] = tmp
m_ = 640
n_ = 9760
k = 128
multiple = np.zeros([m_, n_])
hid = int((k - 1) / TPB) + 1
blockdim = (TPB, TPB)
griddim1 = (20, 305)
Q = np.load("Q.npy")
P = np.load("P.npy")
time_start = time.time()
Movie_predict = np.dot(Q, P)
time_end = time.time()
print("np.dot elapsed time: %ss" % (time_end - time_start))
time_start = time.time()
fast_matmul[griddim1, blockdim](Q, P, multiple)
time_end = time.time()
print("CUDA elapsed time: %ss" % (time_end - time_start))
with open("movies.csv", encoding='utf-8') as csvMovie:
    reader = csv.reader(csvMovie)
    data = [item for index, item in enumerate(reader) if index != 0]
a = list(Movie_predict[1, :])
re2 = heapq.nlargest(100, a)
re1 = [a.index(val) for val in re2]
predict = [data[val] for val in re1]
with open('2.csv', 'w', newline='', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    for item in predict:
        writer.writerow(item)
print(predict)
print(re2)