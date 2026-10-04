import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
class FibonacciScatter:
    def fibonacci_sequence(self, length):
        if length <= 0:
            return []
        elif length == 1:
            return [0]
        sequence = [0, 1]
        for _ in range(2, length):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
    def scatter_sequence(self, seq):
        x = np.arange(len(seq))
        y = np.array(seq)
        plt.scatter(x, y, color='b', label='Fibonacci Numbers')
        plt.title("Fibonacci Sequence Scatter Plot")
        plt.xlabel("Position")
        plt.ylabel("Fibonacci Number")
        plt.legend()
        plt.show()
if __name__ == "__main__":
    fibonacci_scatter = FibonacciScatter()
    length = 10
    data = fibonacci_scatter.fibonacci_sequence(length)
    fibonacci_scatter.scatter_sequence(data)