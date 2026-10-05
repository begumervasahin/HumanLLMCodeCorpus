import matplotlib.pyplot as plt
import numpy as np
class FibonacciScatter:
    def fibonacci_sequence(self, length):
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[:length]
    def scatter_sequence(self, sequence):
        x_values = list(range(len(sequence)))
        y_values = sequence
        plt.scatter(x_values, y_values)
        trendline_coefficients = np.polyfit(x_values, y_values, 1)
        trendline_polynomial = np.poly1d(trendline_coefficients)
        plt.plot(x_values, trendline_polynomial(x_values), "r--")
        plt.xlabel('Index')
        plt.ylabel('Fibonacci Value')
        plt.title('Fibonacci Sequence Scatter Plot with Trendline')
        plt.show()
if __name__ == "__main__":
    fibonacci_scatter = FibonacciScatter()
    fib_length = int(input("Enter the number of Fibonacci sequence points to generate: "))
    fib_sequence = fibonacci_scatter.fibonacci_sequence(fib_length)
    fibonacci_scatter.scatter_sequence(fib_sequence)