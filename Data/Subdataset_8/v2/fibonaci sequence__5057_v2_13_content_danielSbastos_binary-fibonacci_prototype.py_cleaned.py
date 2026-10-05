import numpy as np
import matplotlib.pyplot as plt
def calculate_fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def convert_to_binary_string(number, length=80):
    return format(number, f'0{length}b')
def create_fibonacci_sequence(up_to_n):
    return [calculate_fibonacci_number(i) for i in range(up_to_n + 1)]
def binary_representation_of_sequence(sequence):
    return [convert_to_binary_string(number) for number in sequence]
def binary_string_to_integer_list(binary_sequence):
    return [[int(bit) for bit in binary_string] for binary_string in binary_sequence]
def display_binary_matrix(matrix):
    plt.figure(figsize=(10, 10))
    plt.imshow(matrix, interpolation='nearest', cmap='gray')
    plt.title("Binary Matrix of Fibonacci Sequence")
    plt.xlabel("Bit Index")
    plt.ylabel("Sequence Index")
    plt.show()
def plot_bit_distribution(matrix):
    ones_count = [sum(row) for row in matrix]
    zeros_count = [len(matrix[0]) - sum(row) for row in matrix]
    indices = range(len(ones_count))
    plt.bar(indices, ones_count, 0.6, label='1s', color='r')
    plt.bar(indices, zeros_count, 0.6, label='0s', color='y', bottom=ones_count)
    plt.title("Distribution of 1s and 0s in Fibonacci Binary Matrix")
    plt.xlabel("Sequence Index")
    plt.ylabel("Bit Count")
    plt.legend()
    plt.show()
if __name__ == "__main__":
    n = 100
    fibonacci_sequence = create_fibonacci_sequence(n)
    binary_sequence = binary_representation_of_sequence(fibonacci_sequence)
    binary_matrix = binary_string_to_integer_list(binary_sequence)
    binary_matrix_np = np.array(binary_matrix)
    display_binary_matrix(binary_matrix_np)
    plot_bit_distribution(binary_matrix_np)