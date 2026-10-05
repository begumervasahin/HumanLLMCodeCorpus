import numpy as np
import matplotlib.pyplot as plt
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def format_binary(number):
    return format(number, '080b')
n = 100
fibonacci_numbers = [fibonacci_iterative(i) for i in range(n + 1)]
binary_fibonacci_numbers = [format_binary(num) for num in fibonacci_numbers]
binary_fibonacci_lists = [[int(bit) for bit in binary] for binary in binary_fibonacci_numbers]
binary_table = np.array(binary_fibonacci_lists)
plt.imshow(binary_table, interpolation='nearest')
plt.show()
histogram_ones = [np.sum(column) for column in binary_table.T]
histogram_zeros = [len(binary_table) - ones for ones in histogram_ones]
indices = list(range(len(histogram_ones)))
plt.bar(indices, histogram_ones, 0.6, color='r')
plt.bar(indices, histogram_zeros, 0.6, color='y', bottom=histogram_ones)
plt.show()