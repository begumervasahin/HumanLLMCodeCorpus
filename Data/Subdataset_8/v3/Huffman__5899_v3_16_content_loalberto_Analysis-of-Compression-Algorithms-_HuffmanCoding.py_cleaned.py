from heapq import heappush, heappop, heapify
from collections import defaultdict
import string
import random
import time
def huffman_encode(values):
    count = 0
    heap = []
    for symbol, weight in values.items():
        count += 1
        heap.append([weight, [symbol, ""]])
    heapify(heap)
    while len(heap) > 1:
        count += 1
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda val: (len(val[-1]), val)), count
def generate_random_string(string_length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(string_length))
def measure_huffman_iterations(iterations):
    operation_matrix = {f'Iteration{i}': [] for i in range(1, iterations + 1)}
    time_matrix = {f'Iteration{i}': [] for i in range(1, iterations + 1)}
    for i in range(1, iterations + 1):
        for n in range(1, 6):
            n = 10 ** n
            text = generate_random_string(n)
            huffman_dict = defaultdict(int)
            first_count = 0
            for char in text:
                first_count += 1
                huffman_dict[char] += 1
            start_time = time.time()
            vals, operations_count = huffman_encode(huffman_dict)
            end_time = time.time()
            total_time = (end_time - start_time) * 1000000000
            total_operations = operations_count + first_count
            operation_matrix[f'Iteration{i}'].append(total_operations)
            time_matrix[f'Iteration{i}'].append(total_time)
    operation_result = {i: 0 for i in range(len(operation_matrix['Iteration1']))}
    for key in operation_matrix:
        for idx, val in enumerate(operation_matrix[key]):
            operation_result[idx] += val
    operation_matrix['Average'] = [val / iterations for val in operation_result.values()]
    time_result = {i: 0 for i in range(len(time_matrix['Iteration1']))}
    for key in time_matrix:
        for idx, val in enumerate(time_matrix[key]):
            time_result[idx] += val
    time_matrix['Average'] = [val / iterations for val in time_result.values()]
    return operation_matrix, time_matrix
if __name__ == "__main__":
    iterations = 10
    operation_matrix, time_matrix = measure_huffman_iterations(iterations)
    print('\n\n------------Operation Measurement------------\n\n')
    for key, value in operation_matrix.items():
        print(f"{key}: {value}")
    print('\n\n------------Time Measurement------------\n\n')
    for key, value in time_matrix.items():
        print(f"{key}: {value}")