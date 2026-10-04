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
    if x >= c.shape[0] or y >= c.shape[1]:
        return
    tmp = 0
    for i in range(hid):
        if tx + i * TPB < a.shape[1]:
            sa[tx, ty] = a[x, tx + i * TPB]
        else:
            sa[tx, ty] = 0
        if ty + i * TPB < b.shape[0]:
            sb[tx, ty] = b[tx + i * TPB, y]
        else:
            sb[tx, ty] = 0
        cuda.syncthreads()
        for j in range(TPB):
            tmp += sa[tx, j] * sb[j, ty]
        cuda.syncthreads()
    c[x, y] = tmp
def main():
    m_ = 640
    n_ = 9760
    k = 128
    multiple = np.zeros([m_, n_])
    global hid
    hid = (k - 1)
    blockdim = (TPB, TPB)
    griddim1 = (20, 305)
    Q = np.load("Q.npy")
    P = np.load("P.npy")
    start_time = time.time()
    Movie_predict = np.dot(Q, P)
    end_time = time.time()
    print("Numpy dot product time: %ss" % (end_time - start_time))
    start_time = time.time()
    fast_matmul[griddim1, blockdim](Q, P, multiple)
    end_time = time.time()
    print("CUDA matrix multiplication time: %ss" % (end_time - start_time))
    with open("movies.csv", encoding='utf-8') as csvMovie:
        reader = csv.reader(csvMovie)
        data = [item for index, item in enumerate(reader) if index != 0]
        print(np.shape(data))
        user_predictions = Movie_predict[1, :]
        top_100_scores = heapq.nlargest(100, user_predictions)
        top_100_indices = list(map(user_predictions.tolist().index, top_100_scores))
        predictions = [data[idx] for idx in top_100_indices]
        with open('predicted_movies.csv', 'w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(predictions)
        print(predictions)
        print(top_100_scores)
if __name__ == "__main__":
    main()