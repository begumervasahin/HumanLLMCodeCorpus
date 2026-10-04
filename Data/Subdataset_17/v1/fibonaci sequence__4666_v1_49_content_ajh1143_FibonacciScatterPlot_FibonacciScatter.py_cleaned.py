import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
class FibonacciScatter:
    def fibonacci_sequence(self, length):
        p1, p2 = 0, 1
        fib_list = []
        for _ in range(length):
            fib_list.append(p1)
            p1, p2 = p2, p1 + p2
        return fib_list
    def scatter_sequence(self, seq):
        x = list(range(len(seq)))
        y = seq
        plt.scatter(x, y)
        plt.title("Fibonacci Sequence Scatter Plot")
        plt.xlabel("Position")
        plt.ylabel("Fibonacci Number")
        plt.show()
if __name__ == "__main__":
    fibonacci_scatter = FibonacciScatter()
    data = fibonacci_scatter.fibonacci_sequence(10)
    fibonacci_scatter.scatter_sequence(data)