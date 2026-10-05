import numpy as np
import matplotlib.pyplot as plt
def fibonacci_sequence(n):
    sequence = [0, 1]
    for _ in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
def to_binary_strings(sequence, length=80):
    return [format(number, f'0{length}b') for number in sequence]
def binary_strings_to_matrix(binary_strings):
    return np.array([[int(bit) for bit in string] for string in binary_strings])
def display_fibonacci_matrix(matrix):
    plt.figure(figsize=(10, 10))
    plt.imshow(matrix, cmap='gray', interpolation='nearest')
    plt.title("Fibonacci Sequence in Binary Form")
    plt.xlabel("Bit Position")
    plt.ylabel("Fibonacci Index")
    plt.show()
def plot_bit_distribution(matrix):
    bit_counts = np.sum(matrix, axis=1)
    bit_indices = np.arange(len(bit_counts))
    plt.figure(figsize=(10, 6))
    plt.bar(bit_indices, bit_counts, color='r', label='1s', alpha=0.6)
    plt.bar(bit_indices, matrix.shape[1] - bit_counts, bottom=bit_counts, color='y', label='0s', alpha=0.6)
    plt.title("Bit Distribution in the Fibonacci Binary Matrix")
    plt.xlabel("Fibonacci Index")
    plt.ylabel("Count")
    plt.legend()
    plt.show()
if __name__ == "__main__":
    n = 100
    sequence = fibonacci_sequence(n)
    binary_strings = to_binary_strings(sequence)
    binary_matrix = binary_strings_to_matrix(binary_strings)
    display_fibonacci_matrix(binary_matrix)
    plot_bit_distribution(binary_matrix)