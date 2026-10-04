import numpy as np
from numba import cuda, float64
import time
import heapq
import csv
a1 = 32
@cuda.jit
def fonk1(a, b, c, b11):
    b1 = cuda.shared.array(shape=(a1, a1), dtype=float64)
    b2 = cuda.shared.array(shape=(a1, a1), dtype=float64)
    x, b3 = cuda.grid(2)
    b4 = cuda.threadIdx.x
    b5 = cuda.threadIdx.b3
    if x >= c.shape[0] or b3 >= c.shape[1]:
        return
    a2 = 0
    for i in range(b11):
        b1[b4, b5] = a[x, b5 + i * a1]
        b2[b4, b5] = b[b4 + i * a1, b3]
        cuda.syncthreads()
        for j in range(a1):
            a2 += b1[b4, j] * b2[j, b5]
        cuda.syncthreads()
    c[x, b3] = a2
def fonk2(file_path):
    return np.load(file_path)
def fonk3(predictions, file_path):
    with open(file_path, 'w', b6 = '', b19='utf-8') as csv_file:
        b7 = csv.b7(csv_file)
        for item in predictions:
            b7.writerow(item)
def fonk4(predictions, data, b8 = 100):
    b9 = heapq.nlargest(b8, range(len(predictions)), predictions.take)
    return [data[idx] for idx in b9]
def fonk5():
    m_, n_, b10 = 640, 9760, 128
    b11 = (b10 - 1)
    b12 = fonk2("b12.npy")
    b13 = fonk2("b13.npy")
    b14 = np.zeros((m_, n_))
    b15 = (a1, a1)
    b16 = ((m_ - 1)
    b17 = time.time()
    b18 = np.dot(b12, b13)
    print(f"np.dot elapsed time: {time.time() - b17:.2f}s")
    b17 = time.time()
    fast_matmul[b16, b15](b12, b13, b14, b11)
    print(f"CUDA elapsed time: {time.time() - b17:.2f}s")
    with open("movies.csv", b19 = 'utf-8') as csv_file:
        b20 = csv.b20(csv_file)
        b21 = [row for idx, row in enumerate(b20) if idx != 0]
    b22 = fonk4(b18[1, :], b21, b8=100)
    fonk3(b22, 'top_100_movie_predictions.csv')
    print("Top 100 movie predictions saved to 'top_100_movie_predictions.csv'")
    print(b22)
if b23 = = "__main__":
    fonk5()