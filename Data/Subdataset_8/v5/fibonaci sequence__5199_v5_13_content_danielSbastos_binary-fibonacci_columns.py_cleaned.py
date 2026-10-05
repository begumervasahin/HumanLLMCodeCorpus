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
fibonacci_numbers = [fibonacci_iterative(i) for i in range(num_fibonacci + 1)]
binary_numbers = [format_binary(num) for num in fibonacci_numbers]
binary_array = np.array([[int(bit) for bit in binary] for binary in binary_numbers])
def extract_column(binary_array, column_number):
    column_index = binary_array.shape[1] - column_number - 1
    column = binary_array[:, column_index]
    return np.trim_zeros(column, 'f')
def extract_first_digits_from_column(binary_array, column_number):
    column = extract_column(binary_array, column_number)
    num_patterns = 3 * (2 ** column_number)
    return column[:num_patterns]
first_digits = extract_first_digits_from_column(binary_array, 4)
x_values = np.arange(len(first_digits))
y_values = first_digits
plt.bar(x_values, y_values, width=0.6)
plt.show()