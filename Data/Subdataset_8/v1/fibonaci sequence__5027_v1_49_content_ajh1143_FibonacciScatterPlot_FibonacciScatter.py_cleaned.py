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
        x = list(range(len(seq)))
        y = seq
        plt.scatter(x, y)
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x, p(x), "r--")
        plt.xlabel('Index')
        plt.ylabel('Fibonacci Value')
        plt.title('Fibonacci Sequence Scatter Plot with Trendline')
        plt.show()
if __name__ == "__main__":
    fib_obj = FibonacciScatter()
    fib_data = fib_obj.fibonacci_sequence(10)
    fib_obj.scatter_sequence(fib_data)