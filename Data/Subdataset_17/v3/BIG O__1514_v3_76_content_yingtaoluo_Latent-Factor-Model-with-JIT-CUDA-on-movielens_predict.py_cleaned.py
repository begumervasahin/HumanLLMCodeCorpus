import numpy as np
from numba import cuda, float64
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
def load_matrix(file_path):
    return np.load(file_path)
def save_predictions(predictions, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for item in predictions:
            writer.writerow(item)
def get_top_predictions(predictions, data, top_n=100):
    top_predictions_indices = heapq.nlargest(top_n, range(len(predictions)), predictions.take)
    return [data[idx] for idx in top_predictions_indices]
def main():
    m_, n_, k = 640, 9760, 128
    hid = (k - 1)
    Q = load_matrix("Q.npy")
    P = load_matrix("P.npy")
    multiple = np.zeros((m_, n_))
    blockdim = (TPB, TPB)
    griddim1 = ((m_ - 1)
    start_time = time.time()
    Movie_predict = np.dot(Q, P)
    print(f"np.dot elapsed time: {time.time() - start_time:.2f}s")
    start_time = time.time()
    fast_matmul[griddim1, blockdim](Q, P, multiple, hid)
    print(f"CUDA elapsed time: {time.time() - start_time:.2f}s")
    with open("movies.csv", encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        movie_data = [row for idx, row in enumerate(reader) if idx != 0]
    top_predictions = get_top_predictions(Movie_predict[1, :], movie_data, top_n=100)
    save_predictions(top_predictions, 'top_100_movie_predictions.csv')
    print("Top 100 movie predictions saved to 'top_100_movie_predictions.csv'")
    print(top_predictions)
if __name__ == "__main__":
    main()