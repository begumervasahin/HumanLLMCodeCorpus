import matplotlib.pyplot as plt
import numpy as np
class class1:
    def fonk1(self, length):
        b1 = [0, 1]
        while len(b1) < length:
            b1.append(b1[-1] + b1[-2])
        return b1[:length]
    def fonk2(self, seq):
        b2 = list(range(len(seq)))
        b3 = seq
        plt.scatter(b2, b3)
        b4 = np.polyfit(b2, b3, 1)
        b5 = np.poly1d(b4)
        plt.plot(b2, b5(b2), "r--")
        plt.xlabel('Index')
        plt.ylabel('Fibonacci Value')
        plt.title('Fibonacci Sequence Scatter Plot with Trendline')
        plt.show()
if b6 = = "__main__":
    b7 = class1()
    b8 = int(input("Enter the number of Fibonacci sequence points to generate: "))
    b9 = b7.fonk1(b8)
    b7.fonk2(b9)