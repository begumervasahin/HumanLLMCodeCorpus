import random
import sys
import time
import math
from multiprocessing import Process, Queue
NUM_THREADS = 4
def generate_weights(size):
    weights = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(0)
            else:
                row.append(random.randint(2, 30))
        weights.append(row)
    return weights
def initialize_pi_serial(weights, size):
    pi_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j or weights[i][j] == sys.maxsize:
                row.append(None)
            elif i != j and weights[i][j] < sys.maxsize:
                row.append(i)
            else:
                row.append(-1)
        pi_matrix.append(row)
    return pi_matrix
def initialize_distance_serial(weights, size):
    distance_matrix = [[(0 if i == j else int(sys.maxsize)) for j in range(size)] for i in range(size)]
    distance_matrix[0] = list(weights)
    return distance_matrix
def initialize_pi_parallel(weights, size):
    pi_matrix = [[[(None if i == j else 0) for j in range(size)] for i in range(size)] for _ in range(size)]
    pi_matrix[0] = list(initialize_pi_serial(weights, size))
    return pi_matrix
def floyd_warshall_serial(weights, size):
    distance_matrix = initialize_distance_serial(weights, size)
    pi_matrix = initialize_pi_parallel(weights, size)
    for k in range(1, size):
        for i in range(size):
            for j in range(size):
                distance_matrix[k][i][j] = min(distance_matrix[k - 1][i][j], distance_matrix[k - 1][i][k] + distance_matrix[k - 1][k][j])
                if distance_matrix[k - 1][i][j] <= distance_matrix[k - 1][i][k] + distance_matrix[k - 1][k][j]:
                    pi_matrix[k][i][j] = pi_matrix[k - 1][i][j]
                else:
                    pi_matrix[k][i][j] = pi_matrix[k - 1][k][j]
    return distance_matrix, pi_matrix
def compute_minimum_distance_parallel(dist, pi, k, indices, size, queue):
    distance_array = []
    pi_array = []
    for i in indices:
        distance_array.append([(min(dist[i][j], dist[i][k] + dist[k][j])) for j in range(size)])
        pi_array.append([(pi[i][j] if dist[i][j] <= dist[i][k] + dist[k][j] else pi[k][j]) for j in range(size)])
    queue.put((indices, distance_array, pi_array))
def floyd_warshall_parallel(weights, size):
    distance_matrix = initialize_distance_serial(weights, size)
    pi_matrix = initialize_pi_parallel(weights, size)
    for k in range(1, size):
        threads = []
        queue = Queue()
        for thread_num in range(NUM_THREADS):
            start_index = math.floor(thread_num * (size / NUM_THREADS))
            end_index = math.floor((thread_num + 1) * (size / NUM_THREADS))
            indices = range(start_index, end_index)
            thread = Process(target=compute_minimum_distance_parallel, args=(distance_matrix[k - 1], pi_matrix[k - 1], k, indices, size, queue))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        for _ in range(NUM_THREADS):
            indices, distance_array, pi_array = queue.get()
            count = 0
            for i in indices:
                distance_matrix[k][i] = list(distance_array[count])
                pi_matrix[k][i] = list(pi_array[count])
                count += 1
    return distance_matrix, pi_matrix
if __name__ == "__main__":
    with open('serial.txt', 'a') as serial_file, open('parallel.txt', 'a') as parallel_file:
        for n in range(24, 460, 24):
            weights = generate_weights(n)
            start_time = time.process_time()
            serial_distance, serial_pi = floyd_warshall_serial(weights, n)
            end_time = time.process_time()
            serial_file.write(f'For {n}: Elapsed time: {end_time - start_time}s\n')
            print(f'Serial: For {n}: Elapsed time: {end_time - start_time}s')
            for num_threads in [1, 2, 3, 4, 6, 8]:
                start_time = time.process_time()
                parallel_distance, parallel_pi = floyd_warshall_parallel(weights, n)
                end_time = time.process_time()
                parallel_file.write(f'For {n} with {num_threads} threads: Elapsed time: {end_time - start_time}s\n')
                print(f'Parallel: For {n} with {num_threads} threads: Elapsed time: {end_time - start_time}s')
                print(f'Same distance matrix: {parallel_distance == serial_distance}')
                print(f'Same pi matrix: {parallel_pi == serial_pi}')