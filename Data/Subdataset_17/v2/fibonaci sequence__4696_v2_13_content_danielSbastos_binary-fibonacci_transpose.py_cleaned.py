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
    binary_list = [[int(bit) for bit in format_bin(num)] for num in fib_list]
    return np.array(binary_list)
def plot_binary_table(binary_table):
    plt.imshow(binary_table, interpolation='nearest')
    plt.title("Binary Representation of Fibonacci Numbers (Transposed)")
    plt.xlabel("Fibonacci Sequence Index")
    plt.ylabel("Bit Position")
    plt.colorbar(label="Bit Value")
    plt.show()
def main():
    n = 100
    fib_list = generate_fibonacci_sequence(n)
    binary_table = convert_to_binary_list(fib_list)
    transposed_binary_table = np.transpose(binary_table)
    plot_binary_table(transposed_binary_table)
if __name__ == '__main__':
    main()