import numpy as np
import matplotlib.pyplot as plt
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def format_bin(number):
    return format(number, '080b')
def generate_fibonacci_sequence(n):
    return [fib_iterative(i) for i in range(n + 1)]
def convert_to_binary_list(fib_list):
    return np.array([[int(bit) for bit in format_bin(num)] for num in fib_list])
def get_column(binary_table, column_num):
    total_columns = binary_table.shape[1] - 1
    column = binary_table[:, total_columns - column_num]
    return np.trim_zeros(column, 'f')
def get_first_digits_from_column(binary_table, column_num):
    column = get_column(binary_table, column_num)
    column_bin_number = 2 ** column_num
    total_patterns_to_get = 3 * column_bin_number
    return column[:total_patterns_to_get]
def plot_bar_chart(data):
    x = np.arange(len(data))
    plt.bar(x, data, width=0.6)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("First Digits from the Specified Column of the Binary Table")
    plt.show()
def main():
    n = 100
    fib_list = generate_fibonacci_sequence(n)
    splited_binary_table = convert_to_binary_list(fib_list)
    line_patterns = get_first_digits_from_column(splited_binary_table, 4)
    plot_bar_chart(line_patterns)
if __name__ == '__main__':
    main()