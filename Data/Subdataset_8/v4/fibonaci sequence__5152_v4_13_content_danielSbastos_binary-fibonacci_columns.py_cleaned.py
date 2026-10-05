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
binary_array = np.array([[int(bit) for bit in binary_num] for binary_num in binary_list])
def extract_column(binary_array, column_number):
    total_columns = binary_array.shape[1] - 1
    column = binary_array[:, total_columns - column_number]
    return np.trim_zeros(column, 'f')
def extract_first_digits_from_column(binary_array, column_number):
    column = extract_column(binary_array, column_number)
    column_bin_number = 2 ** column_number
    total_patterns_to_get = 3 * column_bin_number
    return column[:total_patterns_to_get]
line_patterns = extract_first_digits_from_column(binary_array, 4)
x_values = np.arange(len(line_patterns))
y_values = line_patterns
plt.bar(x_values, y_values, width=0.6)
plt.show()