import numpy as np
import matplotlib.pyplot as plt
def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
def format_bin(number):
    return format(number, '080b')
def generate_fibonacci_sequence(n):
    return [fib_iterative(i) for i in range(n + 1)]
def convert_to_binary_list(fib_list):
    return np.array([[int(bit) for bit in format_bin(num)] for num in fib_list])
def plot_binary_table(binary_table):
    plt.imshow(binary_table, interpolation='nearest')
    plt.title("Binary Representation of Fibonacci Numbers")
    plt.show()
def plot_histogram(binary_table):
    hist_one = [sum(row) for row in binary_table]
    hist_zero = [binary_table.shape[1] - sum(row) for row in binary_table]
    indices = list(range(len(hist_one)))
    plt.bar(indices, hist_one, width=0.6, color='r', label='Ones')
    plt.bar(indices, hist_zero, width=0.6, color='y', bottom=hist_one, label='Zeros')
    plt.xlabel("Fibonacci Sequence Index")
    plt.ylabel("Count")
    plt.title("Histogram of Ones and Zeros in Binary Representation")
    plt.legend()
    plt.show()
def main():
    n = 100
    fib_list = generate_fibonacci_sequence(n)
    binary_table = convert_to_binary_list(fib_list)
    plot_binary_table(binary_table)
    plot_histogram(binary_table)
if __name__ == '__main__':
    main()