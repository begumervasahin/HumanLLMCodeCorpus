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
num_fibonacci = 100
fibonacci_sequence = [fibonacci_iterative(i) for i in range(num_fibonacci + 1)]
binary_sequence = [format_binary(num) for num in fibonacci_sequence]
binary_sequence_split = [[int(bit) for bit in binary_num] for binary_num in binary_sequence]
binary_array = np.array(binary_sequence_split)
def get_column(binary_table, column_number):
    total_columns = binary_table.shape[1] - 1
    column = binary_table[:, total_columns - column_number]
    return np.trim_zeros(column, 'f')
def get_first_digits_from_column(binary_table, column_number):
    column = get_column(binary_table, column_number)
    column_binary_number = 2 ** column_number
    total_patterns = 3 * column_binary_number
    return column[:total_patterns]
first_digits = get_first_digits_from_column(binary_array, 4)
x_values = np.arange(len(first_digits))
y_values = first_digits
plt.bar(x_values, y_values, width=0.6)
plt.show()