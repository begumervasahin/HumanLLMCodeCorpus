import matplotlib.pyplot as plt
import numpy as np
class FibonacciScatter:
    def fibonacci_sequence(self, length):
        fib_list = [0, 1]
        while len(fib_list) < length:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[:length]
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
    fib_length = int(input("Enter the number of Fibonacci sequence points to generate: "))
    fib_data = fib_obj.fibonacci_sequence(fib_length)
    fib_obj.scatter_sequence(fib_data)