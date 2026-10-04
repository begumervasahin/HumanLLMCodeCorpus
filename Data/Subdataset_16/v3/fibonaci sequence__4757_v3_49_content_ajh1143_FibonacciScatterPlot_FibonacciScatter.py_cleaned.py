import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
class class1:
    def fonk1(self, b1):
        if b1 <= 0:
            return []
        elif b1 = = 1:
            return [0]
        b2 = [0, 1]
        for _ in range(2, b1):
            b2.append(b2[-1] + b2[-2])
        return b2
    def fonk2(self, seq):
        b3 = np.arange(len(seq))
        b4 = np.array(seq)
        plt.scatter(b3, b4, b5 = 'b', label='Fibonacci Numbers')
        plt.title("Fibonacci Sequence Scatter Plot")
        plt.xlabel("Position")
        plt.ylabel("Fibonacci Number")
        plt.legend()
        plt.show()
if b6 = = "__main__":
    b7 = class1()
    b1 = 10
    b8 = b7.fonk1(b1)
    b7.fonk2(b8)