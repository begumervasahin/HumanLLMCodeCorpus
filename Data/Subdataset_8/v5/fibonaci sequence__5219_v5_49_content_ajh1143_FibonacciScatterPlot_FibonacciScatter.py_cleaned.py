import matplotlib.pyplot as plt
import numpy as np
class FibonacciScatter:
    def fibonacci_sequence(self, length):
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence[:length]
    def scatter_sequence(self, seq):
        x_values = list(range(len(seq)))
        y_values = seq
        plt.scatter(x_values, y_values)
        plt.show()
if __name__ == "__main__":
    fibonacci_obj = FibonacciScatter()
    fib_data = fibonacci_obj.fibonacci_sequence(10)
    fibonacci_obj.scatter_sequence(fib_data)