import random
import sys
import time
import math
from multiprocessing import Process, Queue
NUM_THREADS = 4
def generate_weights(size):
    weights = []
    for i in range(size):
        row = [0 if i == j else random.randint(2, 30) for j in range(size)]
        weights.append(row)
    return weights
def initialize_pi(weights, size):
    pi_matrix = []
    for i in range(size):
        row = [None if i == j or weights[i][j] == sys.maxsize else i for j in range(size)]
        pi_matrix.append(row)
    return pi_matrix
def initialize_distance(weights, size):
    distance_matrix = [[0 if i == j else sys.maxsize for j in range(size)] for i in range(size)]
    distance_matrix[0] = list(weights)
    return distance_matrix
def compute_minimum_distance(dist, pi, k, indices, size, queue):
    distance_array = []
    pi_array = []
    for i in indices:
        distance_array.append([min(dist[i][j], dist[i][k] + dist[k][j]) for j in range(size)])
        pi_array.append([pi[i][j] if dist[i][j] <= dist[i][k] + dist[k][j] else pi[k][j] for j in range(size)])
    queue.put((indices, distance_array, pi_array))
def floyd_warshall(weights, size):
    distance_matrix = initialize_distance(weights, size)
    pi_matrix = initialize_pi(weights, size)
    for k in range(1, size):
        threads = []
        queue = Queue()
        for thread_num in range(NUM_THREADS):
            start_index = math.floor(thread_num * (size / NUM_THREADS))
            end_index = math.floor((thread_num + 1) * (size / NUM_THREADS))
            indices = range(start_index, end_index)
            thread = Process(target=compute_minimum_distance, args=(distance_matrix[k - 1], pi_matrix[k - 1], k, indices, size, queue))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        for _ in range(NUM_THREADS):
            indices, distance_array, pi_array = queue.get()
            count = 0
            for i in indices:
                distance_matrix[k][i] = distance_array[count]
                pi_matrix[k][i] = pi_array[count]
                count += 1
    return distance_matrix, pi_matrix
if __name__ == "__main__":
    with open('serial.txt', 'a') as serial_file, open('parallel.txt', 'a') as parallel_file:
        for n in range(24, 460, 24):
            weights = generate_weights(n)
            start_time = time.process_time()
            serial_distance, serial_pi = floyd_warshall(weights, n)
            end_time = time.process_time()
            serial_file.write(f'For {n}: Elapsed time: {end_time - start_time}s\n')
            print(f'Serial: For {n}: Elapsed time: {end_time - start_time}s')
            for num_threads in [1, 2, 3, 4, 6, 8]:
                start_time = time.process_time()
                parallel_distance, parallel_pi = floyd_warshall(weights, n)
                end_time = time.process_time()
                parallel_file.write(f'For {n} with {num_threads} threads: Elapsed time: {end_time - start_time}s\n')
                print(f'Parallel: For {n} with {num_threads} threads: Elapsed time: {end_time - start_time}s')
                print(f'Same distance matrix: {parallel_distance == serial_distance}')
                print(f'Same pi matrix: {parallel_pi == serial_pi}')