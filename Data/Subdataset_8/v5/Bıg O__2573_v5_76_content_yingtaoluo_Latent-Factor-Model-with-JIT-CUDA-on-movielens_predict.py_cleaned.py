import numpy as np
from numba import cuda, float64
import time
import heapq
import csv
THREADS_PER_BLOCK = 32
@cuda.jit
def cuda_matmul(a, b, c):
    shared_a = cuda.shared.array(shape=(THREADS_PER_BLOCK, THREADS_PER_BLOCK), dtype=float64)
    shared_b = cuda.shared.array(shape=(THREADS_PER_BLOCK, THREADS_PER_BLOCK), dtype=float64)
    x, y = cuda.grid(2)
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    if x >= c.shape[0] and y >= c.shape[1]:
        return
    tmp = 0
    for i in range(blocks_per_row):
        shared_a[tx, ty] = a[x, ty + i * THREADS_PER_BLOCK]
        shared_b[tx, ty] = b[tx + i * THREADS_PER_BLOCK, y]
        cuda.syncthreads()
        for j in range(THREADS_PER_BLOCK):
            tmp += shared_a[tx, j] * shared_b[j, ty]
        cuda.syncthreads()
    c[x, y] = tmp
def load_matrices(Q_file, P_file):
    Q = np.load(Q_file)
    P = np.load(P_file)
    return Q, P
def perform_matrix_multiplication_numpy(Q, P):
    start_time = time.time()
    Movie_predict = np.dot(Q, P)
    end_time = time.time()
    print("Time taken for np.dot: %ss" % (end_time - start_time))
    return Movie_predict
def perform_matrix_multiplication_cuda(Q, P, m, n, k):
    multiple = np.zeros([m, n])
    blocks_per_row = int((k - 1) / THREADS_PER_BLOCK) + 1
    block_dim = (THREADS_PER_BLOCK, THREADS_PER_BLOCK)
    grid_dim = (m
    start_time = time.time()
    cuda_matmul[grid_dim, block_dim](Q, P, multiple)
    end_time = time.time()
    print("Time taken for CUDA: %ss" % (end_time - start_time))
    return multiple
def read_movie_data(csv_file):
    with open(csv_file, encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [item for index, item in enumerate(reader) if index != 0]
    return data
def get_top_predictions(Movie_predict, data, num_predictions=100):
    scores = list(Movie_predict[1, :])
    top_scores_indices = heapq.nlargest(num_predictions, scores)
    top_movies_indices = list(map(scores.index, top_scores_indices))
    top_movies = [data[index] for index in top_movies_indices]
    return top_movies, top_scores_indices
def write_predictions_to_csv(predictions, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(predictions)
def main():
    Q, P = load_matrices("Q.npy", "P.npy")
    Movie_predict_np = perform_matrix_multiplication_numpy(Q, P)
    Movie_predict_cuda = perform_matrix_multiplication_cuda(Q, P, m_, n_, k)
    data = read_movie_data("movies.csv")
    top_predictions, top_scores = get_top_predictions(Movie_predict_np, data)
    write_predictions_to_csv(top_predictions, '2.csv')
    print(top_predictions)
    print(top_scores)
if __name__ == "__main__":
    main()