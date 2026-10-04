import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
class FibonacciScatter:
    def generate_fibonacci_sequence(self, length):
        sequence = [0, 1]
        for _ in range(2, length):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:length]
    def plot_fibonacci_sequence(self, sequence):
        x = np.arange(len(sequence))
        y = np.array(sequence)
        plt.scatter(x, y, color='b', label='Fibonacci Numbers')
        plt.title("Fibonacci Sequence Scatter Plot")
        plt.xlabel("Position")
        plt.ylabel("Fibonacci Number")
        plt.legend()
        plt.show()
if __name__ == "__main__":
    fibonacci_scatter = FibonacciScatter()
    length = 10
    fibonacci_data = fibonacci_scatter.generate_fibonacci_sequence(length)
    fibonacci_scatter.plot_fibonacci_sequence(fibonacci_data)