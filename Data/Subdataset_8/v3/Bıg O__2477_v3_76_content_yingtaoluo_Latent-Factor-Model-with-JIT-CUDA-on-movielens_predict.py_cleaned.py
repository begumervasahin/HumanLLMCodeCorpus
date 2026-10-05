import numpy as np
from numba import cuda, float64
import time
import heapq
import csv
THREADS_PER_BLOCK = 32
@cuda.jit
def fast_matrix_multiply(a, b, c):
    shared_a = cuda.shared.array(shape=(THREADS_PER_BLOCK, THREADS_PER_BLOCK), dtype=float64)
    shared_b = cuda.shared.array(shape=(THREADS_PER_BLOCK, THREADS_PER_BLOCK), dtype=float64)
    x, y = cuda.grid(2)
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    if x >= c.shape[0] and y >= c.shape[1]:
        return
    tmp = 0
    for i in range(HID):
        shared_a[tx, ty] = a[x, ty + i * THREADS_PER_BLOCK]
        shared_b[tx, ty] = b[tx + i * THREADS_PER_BLOCK, y]
        cuda.syncthreads()
        for j in range(THREADS_PER_BLOCK):
            tmp += shared_a[tx, j] * shared_b[j, ty]
        cuda.syncthreads()
    c[x, y] = tmp
M = 640
N = 9760
K = 128
multiple = np.zeros([M, N])
HID = int((K - 1) / THREADS_PER_BLOCK) + 1
BLOCK_DIM = (THREADS_PER_BLOCK, THREADS_PER_BLOCK)
GRID_DIM = (20, 305)
Q = np.load("Q.npy")
P = np.load("P.npy")
start_time = time.time()
movie_predict_np = np.dot(Q, P)
end_time = time.time()
print("np.dot elapsed time: %ss" % (end_time - start_time))
start_time = time.time()
fast_matrix_multiply[GRID_DIM, BLOCK_DIM](Q, P, multiple)
end_time = time.time()
print("CUDA elapsed time: %ss" % (end_time - start_time))
with open("movies.csv", encoding='utf-8') as csv_movie:
    reader = csv.reader(csv_movie)
    data = [item for index, item in enumerate(reader) if index != 0]
movie_ratings = list(movie_predict_np[1, :])
top_ratings = heapq.nlargest(100, movie_ratings)
top_indices = [movie_ratings.index(val) for val in top_ratings]
top_movies = [data[val] for val in top_indices]
with open('top_movies.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for item in top_movies:
        writer.writerow(item)
print(top_movies)
print(top_ratings)