import random
import sys
import time
from multiprocessing import Process, Queue
import math
numThreads = 4
def generate_random_weights(size):
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
def initialize_pi(weights, size):
    pi = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j or weights[i][j] == sys.maxsize:
                row.append(None)
            elif i != j and weights[i][j] < sys.maxsize:
                row.append(i)
            else:
                row.append(-1)
        pi.append(row)
    return pi
def initialize_distance(weights, size):
    distance = [[0 if i == j else int(sys.maxsize) for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            distance[i][j] = weights[i][j]
    return distance
def initialize_previous_vertex(weights, size):
    previous_vertex = [[None if i == j else 0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            if weights[i][j] != sys.maxsize:
                previous_vertex[i][j] = i
    return previous_vertex
def floyd_warshall_serial(weights, size):
    distance = initialize_distance(weights, size)
    previous_vertex = initialize_previous_vertex(weights, size)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                if distance[i][j] == distance[i][k] + distance[k][j]:
                    previous_vertex[i][j] = previous_vertex[k][j]
    return distance, previous_vertex
def min_p_parallel(distance, previous_vertex, k, indices_range, size, queue):
    updated_distances = []
    updated_previous_vertex = []
    for i in indices_range:
        updated_distances.append([min(distance[i][j], distance[i][k] + distance[k][j]) for j in range(size)])
        updated_previous_vertex.append([previous_vertex[i][j] if distance[i][j] <= distance[i][k] + distance[k][j] else previous_vertex[k][j] for j in range(size)])
    queue.put((indices_range, updated_distances, updated_previous_vertex))
def floyd_warshall_parallel(weights, size):
    distance = initialize_distance(weights, size)
    previous_vertex = initialize_previous_vertex(weights, size)
    for k in range(size):
        processes = []
        queue = Queue()
        for proc in range(numThreads):
            start_index = math.floor(proc * (size / numThreads))
            end_index = math.floor((proc + 1) * (size / numThreads))
            indices_range = range(start_index, end_index)
            process = Process(target=min_p_parallel, args=(distance, previous_vertex, k, indices_range, size, queue))
            process.start()
            processes.append(process)
        for process in processes:
            process.join()
        for _ in range(numThreads):
            indices, updated_distances, updated_previous_vertex = queue.get()
            count = 0
            for i in indices:
                distance[i] = list(updated_distances[count])
                previous_vertex[i] = list(updated_previous_vertex[count])
                count += 1
    return distance, previous_vertex
if __name__ == "__main__":
    for size in range(24, 460, 24):
        weights = generate_random_weights(size)
        start_time = time.process_time()
        serial_distance, serial_previous_vertex = floyd_warshall_serial(weights, size)
        end_time = time.process_time()
        print('Serial: For size %s: Elapsed time: %ss' % (size, str(end_time - start_time)))
        for num_threads in [1, 2, 3, 4, 6, 8]:
            numThreads = num_threads
            start_time = time.process_time()
            parallel_distance, parallel_previous_vertex = floyd_warshall_parallel(weights, size)
            end_time = time.process_time()
            print('Parallel: For size %s with %s threads: Elapsed time: %ss' % (size, num_threads, str(end_time - start_time)))
            print('Same distance matrix: %s' % (parallel_distance == serial_distance))
            print('Same previous vertex matrix: %s' % (parallel_previous_vertex == serial_previous_vertex))