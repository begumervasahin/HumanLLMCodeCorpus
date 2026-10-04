import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
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
        plt.title("Fibonacci Sequence Scatter Plot")
        plt.xlabel("Position")
        plt.ylabel("Fibonacci Number")
        plt.show()
if b5 = = "__main__":
    b6 = class1()
    b7 = b6.fonk1(10)
    b6.fonk2(b7)