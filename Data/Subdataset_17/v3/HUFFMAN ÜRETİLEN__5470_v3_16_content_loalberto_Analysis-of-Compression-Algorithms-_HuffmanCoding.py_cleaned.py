import random
import string
import time
from heapq import heappush, heappop, heapify
from collections import defaultdict
def huffman_encode(symbol_weights):
    operation_count = 0
    heap = []
    for symbol, weight in symbol_weights.items():
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
    huffman_codes = sorted(heappop(heap)[1:], key=lambda item: (len(item[1]), item[0]))
    return huffman_codes, operation_count
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
def main():
    iterations = 10
    op_matrix = {f'Iteration {i + 1}': [] for i in range(iterations)}
    time_matrix = {f'Iteration {i + 1}': [] for i in range(iterations)}
    for itr in range(iterations):
        iteration_key = f'Iteration {itr + 1}'
        n = 10
        while n <= 100000:
            random_string = generate_random_string(n)
            frequency_dict = defaultdict(int)
            initial_operations = 0
            for char in random_string:
                initial_operations += 1
                frequency_dict[char] += 1
            start_time = time.time()
            encoded_values, encoding_operations = huffman_encode(frequency_dict)
            end_time = time.time()
            total_time_ns = (end_time - start_time) * 1e9
            total_operations = initial_operations + encoding_operations
            op_matrix[iteration_key].append(total_operations)
            time_matrix[iteration_key].append(total_time_ns)
            n *= 10
    calculate_averages(op_matrix)
    calculate_averages(time_matrix)
    print_results(op_matrix, 'Operation Count')
    print_results(time_matrix, 'Time (ns)')
def calculate_averages(matrix):
    num_iterations = len(matrix)
    averages = [
        sum(matrix[key][i] for key in matrix) / num_iterations
        for i in range(len(next(iter(matrix.values()))))
    ]
    matrix['Average'] = averages
def print_results(matrix, label):
    print(f'\n------------ {label} Measurements ------------\n')
    for key, values in matrix.items():
        print(f'{key}: {values}')
if __name__ == "__main__":
    main()