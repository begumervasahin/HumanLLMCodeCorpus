import matplotlib.pyplot as plt
import numpy as np
class class1:
    def fonk1(self, length):
        b1 = [0, 1]
        while len(b1) < length:
            b2 = b1[-1] + b1[-2]
            b1.append(b2)
        return b1[:length]
    def fonk2(self, seq):
        b3 = list(range(len(seq)))
        b4 = seq
        plt.scatter(b3, b4)
        plt.show()
if b5 = = "__main__":
    b6 = class1()
    b7 = b6.fonk1(10)
    b6.fonk2(b7)