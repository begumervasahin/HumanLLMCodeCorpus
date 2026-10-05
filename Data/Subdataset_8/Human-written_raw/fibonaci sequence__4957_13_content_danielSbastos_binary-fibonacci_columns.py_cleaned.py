import numpy as np
def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
def format_bin(number):
  return format(number, '080b')
n = 100
fib_list = [fib_iterative(i) for i in range(n + 1)]
fib_list_bin = [format_bin(i) for i in fib_list]
fib_list_bin_splited = []
for bin_number in fib_list_bin:
    bin_list = []
    for i in bin_number:
        bin_list.append(int(i))
    fib_list_bin_splited.append(bin_list)
splited_binary_table = np.array(fib_list_bin_splited)
def get_column(binary_table, column_num):
    total_columns = binary_table.shape[1] - 1
    column = binary_table[:, total_columns - column_num]
    return np.trim_zeros(column, 'f')
def get_first_digits_from_column(binary_table, column_num):
    column = get_column(binary_table, column_num)
    column_bin_number = 2 ** column_num
    total_patterns_to_get = 3 * column_bin_number
    return column[:total_patterns_to_get]
line_patterns = get_first_digits_from_column(splited_binary_table, 4)
x = np.arange(len(line_patterns))
y = line_patterns
import matplotlib.pyplot as plt
plt.bar(x, y, width=0.6)
plt.show()