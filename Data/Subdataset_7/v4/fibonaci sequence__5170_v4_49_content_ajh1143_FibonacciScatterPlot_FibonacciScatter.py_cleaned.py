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
        b3 = []
        b4 = []
        for position, value in enumerate(seq):
            b3.append(position)
            b4.append(value)
        plt.scatter(b3, b4)
        plt.show()
if b5 = = "__main__":
    b6 = class1()
    b7 = b6.fonk1(10)
    b6.fonk2(b7)