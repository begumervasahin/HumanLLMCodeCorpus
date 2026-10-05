import matplotlib.pyplot as plt
import numpy as np
class FibonacciScatter:
    def fibonacci_sequence(self, length):
        p1, p2 = 0, 1
        fib_list = []
        for _ in range(length):
            fib_list.append(p1)
            p1, p2 = p2, p1 + p2
        return fib_list
    def scatter_sequence(self, seq):
        x = []
        y = []
        for position, value in enumerate(seq):
            x.append(position)
            y.append(value)
        plt.scatter(x, y)
        plt.show()
if __name__ == "__main__":
    fibonacci_obj = FibonacciScatter()
    fib_data = fibonacci_obj.fibonacci_sequence(10)
    fibonacci_obj.scatter_sequence(fib_data)