import random
import string
import time
from heapq import heappush, heappop, heapify
from collections import defaultdict
def encode(values):
    count = 0
    heap = []
    for sym, wt in values.items():
        count += 1
        heap.append([wt, [sym, ""]])
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
def random_string(string_length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(string_length))
def main():
    iterations = 10
    op_matrix = {f'Iteration{i + 1}': [] for i in range(iterations)}
    time_matrix = {f'Iteration{i + 1}': [] for i in range(iterations)}
    for itr in range(iterations):
        iteration_key = f'Iteration{itr + 1}'
        n = 10
        while n <= 100000:
            txt = random_string(n)
            huffman = defaultdict(int)
            first_count = 0
            for ch in txt:
                first_count += 1
                huffman[ch] += 1
            start_time = time.time()
            encoded_values, encode_operations = encode(huffman)
            end_time = time.time()
            total_time = (end_time - start_time) * 1e9
            total_operations = encode_operations + first_count
            op_matrix[iteration_key].append(total_operations)
            time_matrix[iteration_key].append(total_time)
            n *= 10
    calculate_averages(op_matrix)
    calculate_averages(time_matrix)
    print_results(op_matrix, 'operation')
    print_results(time_matrix, 'time')
def calculate_averages(matrix):
    average = []
    num_iterations = len(matrix)
    for i in range(len(matrix['Iteration1'])):
        avg_value = sum(matrix[key][i] for key in matrix) / num_iterations
        average.append(avg_value)
    matrix['Average'] = average
def print_results(matrix, label):
    print(f'\n\n------------This is for the {label} measurement------------\n\n')
    for key in matrix:
        print(f'{key}: {matrix[key]}')
if __name__ == "__main__":
    main()