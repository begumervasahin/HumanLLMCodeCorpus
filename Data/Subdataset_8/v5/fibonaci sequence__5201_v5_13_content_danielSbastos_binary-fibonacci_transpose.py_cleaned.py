import numpy as np
import matplotlib.pyplot as plt
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def format_binary(number):
    return format(number, '080b')
num_fibonacci = 100
fibonacci_sequence = [fibonacci_iterative(i) for i in range(num_fibonacci + 1)]
binary_sequence = [format_binary(num) for num in fibonacci_sequence]
binary_split_sequence = [[int(bit) for bit in binary] for binary in binary_sequence]
binary_array = np.array(binary_split_sequence)
transposed_binary_array = np.transpose(binary_array)
plt.imshow(transposed_binary_array, interpolation='nearest')
plt.show()