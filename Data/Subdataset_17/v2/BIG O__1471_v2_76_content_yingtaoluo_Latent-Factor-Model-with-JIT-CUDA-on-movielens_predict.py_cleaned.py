import numpy as np
from numba import cuda, float64
from scipy import sparse
import time
import heapq
import csv
TPB = 32
@cuda.jit
def fast_matmul(a, b, c, hid):
    sa = cuda.shared.array(shape=(TPB, TPB), dtype=float64)
    sb = cuda.shared.array(shape=(TPB, TPB), dtype=float64)
    x, y = cuda.grid(2)
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    if x >= c.shape[0] or y >= c.shape[1]:
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
def main():
    m_ = 640
    n_ = 9760
    k = 128
    hid = (k - 1)
    Q = np.load("Q.npy")
    P = np.load("P.npy")
    multiple = np.zeros((m_, n_))
    blockdim = (TPB, TPB)
    griddim1 = ((m_ - 1)
    time_start = time.time()
    Movie_predict = np.dot(Q, P)
    time_end = time.time()
    print("np.dot elapsed time: {}s".format(time_end - time_start))
    time_start = time.time()
    fast_matmul[griddim1, blockdim](Q, P, multiple, hid)
    time_end = time.time()
    print("CUDA elapsed time: {}s".format(time_end - time_start))
    with open("movies.csv", encoding='utf-8') as csvMovie:
        reader = csv.reader(csvMovie)
        data = [item for index, item in enumerate(reader) if index != 0]
    print("Shape of movie data:", np.shape(data))
    a = list(Movie_predict[1, :])
    re2 = heapq.nlargest(100, a)
    re1 = list(map(a.index, re2))
    predict = [data[re1[i]] for i in range(100)]
    with open('2.csv', 'w', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        for item in predict:
            writer.writerow(item)
    print("Top 100 movie predictions saved to '2.csv'")
    print(predict)
    print(re2)
if __name__ == "__main__":
    main()