import random
import sys
import time
from multiprocessing import Process, Queue
import math
NUM_THREADS = 4
def generate_weight_matrix(size):
    weights = []
    for i in range(size):
        row = [0 if i == j else random.randint(2, 30) for j in range(size)]
        weights.append(row)
    return weights
def initialize_pi_matrix(weights, size):
    pi_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j or weights[i][j] == sys.maxsize:
                row.append(None)
            elif weights[i][j] < sys.maxsize:
                row.append(i)
            else:
                row.append(-1)
        pi_matrix.append(row)
    return pi_matrix
def initialize_distance_matrix(weights, size):
    dist_matrix = [[[(0 if i == j else sys.maxsize) for j in range(size)] for i in range(size)] for _ in range(size)]
    dist_matrix[0] = list(weights)
    return dist_matrix
def initialize_parallel_pi_matrix(weights, size):
    pi_matrix = [[[(None if i == j else 0) for j in range(size)] for i in range(size)] for _ in range(size)]
    pi_matrix[0] = list(initialize_pi_matrix(weights, size))
    return pi_matrix
def floyd_warshall_serial(weights, size):
    dist_matrix = initialize_distance_matrix(weights, size)
    pi_matrix = initialize_parallel_pi_matrix(weights, size)
    for k in range(1, size):
        for i in range(size):
            for j in range(size):
                new_distance = dist_matrix[k - 1][i][k] + dist_matrix[k - 1][k][j]
                if new_distance < dist_matrix[k - 1][i][j]:
                    dist_matrix[k][i][j] = new_distance
                    pi_matrix[k][i][j] = pi_matrix[k - 1][k][j]
                else:
                    dist_matrix[k][i][j] = dist_matrix[k - 1][i][j]
                    pi_matrix[k][i][j] = pi_matrix[k - 1][i][j]
    return dist_matrix, pi_matrix
def min_p_parallel(dist, pi, k, ir, size, queue):
    dist_arr = []
    pi_arr = []
    for i in ir:
        dist_arr.append([(min(dist[i][j], dist[i][k] + dist[k][j])) for j in range(size)])
        pi_arr.append([(pi[i][j] if dist[i][j] <= dist[i][k] + dist[k][j] else pi[k][j]) for j in range(size)])
    queue.put((ir, dist_arr, pi_arr))
def floyd_warshall_parallel(weights, size):
    dist_matrix = initialize_distance_matrix(weights, size)
    pi_matrix = initialize_parallel_pi_matrix(weights, size)
    for k in range(1, size):
        processes = []
        queue = Queue()
        for proc in range(NUM_THREADS):
            imin = math.floor(proc * (size / NUM_THREADS))
            imax = math.floor((proc + 1) * (size / NUM_THREADS))
            ir = range(imin, imax)
            p = Process(target=min_p_parallel, args=(dist_matrix[k - 1], pi_matrix[k - 1], k, ir, size, queue), daemon=True)
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
        for _ in range(NUM_THREADS):
            veci, vecd, vecp = queue.get()
            for idx, i in enumerate(veci):
                dist_matrix[k][i] = vecd[idx]
                pi_matrix[k][i] = vecp[idx]
    return dist_matrix, pi_matrix
if __name__ == "__main__":
    with open('serial.txt', 'a') as fis, open('parallel.txt', 'a') as fip:
        for n in range(24, 460, 24):
            weights = generate_weight_matrix(n)
            start_time = time.process_time()
            ds, ps = floyd_warshall_serial(weights, n)
            end_time = time.process_time()
            fis.write(f'For {n}: Elapsed time: {end_time - start_time}s\n')
            print(f'S: For {n}: Elapsed time: {end_time - start_time}s')
            for num_threads in [1, 2, 3, 4, 6, 8]:
                global NUM_THREADS
                NUM_THREADS = num_threads
                start_time = time.process_time()
                dp, pp = floyd_warshall_parallel(weights, n)
                end_time = time.process_time()
                fip.write(f'For {n} with {num_threads} threads: Elapsed time: {end_time - start_time}s\n')
                print(f'P: For {n} with {num_threads} threads: Elapsed time: {end_time - start_time}s')
                print(f'Same dist matrix: {dp == ds}')
                print(f'Same pi matrix: {pp == ps}')