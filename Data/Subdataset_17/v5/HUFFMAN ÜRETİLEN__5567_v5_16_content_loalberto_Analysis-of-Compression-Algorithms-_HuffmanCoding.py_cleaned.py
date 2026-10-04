import random
import string
import time
from collections import defaultdict
from heapq import heappush, heappop, heapify
def huffman_encode(symbols_weights):
    heap = []
    operation_count = 0
    for symbol, weight in symbols_weights.items():
        operation_count += 1
        heap.append([weight, [symbol, ""]])
    heapify(heap)
    while len(heap) > 1:
        operation_count += 1
        low = heappop(heap)
        high = heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    huffman_tree = sorted(heappop(heap)[1:], key=lambda pair: (len(pair[1]), pair[0]))
    return huffman_tree, operation_count
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
def measure_huffman_performance(iterations=10):
    op_matrix = {f'Iteration {i + 1}': [] for i in range(iterations)}
    time_matrix = {f'Iteration {i + 1}': [] for i in range(iterations)}
    for iteration in range(1, iterations + 1):
        string_length = 10
        while string_length <= 100000:
            random_string = generate_random_string(string_length)
            frequency = defaultdict(int)
            for ch in random_string:
                frequency[ch] += 1
            start_time = time.time()
            _, encoding_operations = huffman_encode(frequency)
            end_time = time.time()
            total_time_ns = (end_time - start_time) * 1e9
            total_operations = encoding_operations + len(random_string)
            op_matrix[f'Iteration {iteration}'].append(total_operations)
            time_matrix[f'Iteration {iteration}'].append(total_time_ns)
            string_length *= 10
    op_matrix['Average'] = calculate_averages(op_matrix)
    time_matrix['Average'] = calculate_averages(time_matrix)
    return op_matrix, time_matrix
def calculate_averages(matrix):
    averages = []
    num_iterations = len(matrix) - 1
    for i in range(len(matrix['Iteration 1'])):
        avg = sum(matrix[f'Iteration {j + 1}'][i] for j in range(num_iterations)) / num_iterations
        averages.append(avg)
    return averages
def main():
    op_matrix, time_matrix = measure_huffman_performance()
    print('\n\n------------ Operation Measurement ------------\n\n')
    for key, values in op_matrix.items():
        print(f'{key}: {values}')
    print('\n\n------------ Time Measurement (ns) ------------\n\n')
    for key, values in time_matrix.items():
        print(f'{key}: {values}')
if __name__ == "__main__":
    main()