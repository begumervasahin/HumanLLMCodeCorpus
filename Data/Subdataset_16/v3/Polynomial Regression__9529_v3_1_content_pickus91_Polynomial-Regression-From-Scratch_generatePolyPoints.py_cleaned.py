import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, a2, a3, b8, b1 = 1, b5=1):
    b2 = np.linspace(a1, a2, a3)
    b3 = np.polyval(b8[::-1], b2)
    if b1 > 0:
        b4 = np.random.normal(0, 10 ** b1, a3)
        b3 += b4
    if b5 = = 1:
        plt.figure()
        plt.scatter(b2, b3, b6 = 'Data points')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Generated Polynomial Points with Noise')
        plt.legend()
        plt.show()
    return b2, b3
if b7 = = "__main__":
    a1 = 0
    a2 = 10
    a3 = 100
    b8 = [1, 2, 3]
    b1 = 1
    b2, b3 = fonk1(a1, a2, a3, b8, b1, b5=1)