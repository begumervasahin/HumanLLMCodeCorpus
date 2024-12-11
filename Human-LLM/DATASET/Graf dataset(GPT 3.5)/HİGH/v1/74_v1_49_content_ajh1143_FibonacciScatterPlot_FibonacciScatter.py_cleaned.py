import matplotlib.pyplot as plt
import numpy as np
class class1:
    def fonk1(self, length):
        p1, b1 = 0, 1
        b2 = []
        for _ in range(length):
            b2.append(p1)
            p1, b1 = b1, p1 + b1
        return b2
    def fonk2(self, seq):
        b3 = list(range(len(seq)))
        b4 = seq
        plt.scatter(b3, b4)
        b5 = np.polyfit(b3, b4, 1)
        b6 = np.poly1d(b5)
        plt.plot(b3, b6(b3), "r--")
        plt.xlabel('Index')
        plt.ylabel('Fibonacci Value')
        plt.title('Fibonacci Sequence Scatter Plot with Trendline')
        plt.show()
if b7 = = "__main__":
    b8 = class1()
    b9 = b8.fonk1(10)
    b8.fonk2(b9)