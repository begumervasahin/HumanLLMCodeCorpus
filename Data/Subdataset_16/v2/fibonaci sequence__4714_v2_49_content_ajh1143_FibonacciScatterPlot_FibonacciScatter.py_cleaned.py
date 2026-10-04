import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
class class1:
    def fonk1(self, a1):
        b1 = [0, 1]
        while len(b1) < a1:
            b1.append(b1[-1] + b1[-2])
        return b1[:a1]
    def fonk2(self, seq):
        b2 = np.arange(len(seq))
        b3 = np.array(seq)
        plt.scatter(b2, b3, b4 = 'b', label='Fibonacci Numbers')
        plt.title("Fibonacci Sequence Scatter Plot")
        plt.xlabel("Position")
        plt.ylabel("Fibonacci Number")
        plt.legend()
        plt.show()
if b5 = = "__main__":
    b6 = class1()
    a1 = 10
    b7 = b6.fonk1(a1)
    b6.fonk2(b7)