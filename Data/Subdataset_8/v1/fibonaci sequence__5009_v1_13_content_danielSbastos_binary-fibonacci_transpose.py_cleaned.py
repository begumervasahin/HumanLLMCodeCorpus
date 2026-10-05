import numpy as np
import matplotlib.pyplot as plt
def fibonacci_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
def format_binary(number):
    return format(number, '080b')
n = 100
fibonacci_list = [fibonacci_iterative(i) for i in range(n + 1)]
binary_list = [format_binary(num) for num in fibonacci_list]
binary_array = np.array([[int(bit) for bit in binary] for binary in binary_list])
transposed_binary_array = np.transpose(binary_array)
plt.imshow(transposed_binary_array, interpolation='nearest')
plt.show()