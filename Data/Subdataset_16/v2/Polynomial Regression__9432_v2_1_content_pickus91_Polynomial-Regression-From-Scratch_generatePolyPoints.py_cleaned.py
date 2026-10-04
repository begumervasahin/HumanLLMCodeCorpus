import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, a2, a3, b7, b1 = 1, b4=1):
    b2 = np.linspace(a1, a2, a3)
    b3 = np.zeros_like(b2)
    for i, coef in enumerate(b7):
        b3 += coef * b2 ** i
    if b1 > 0:
        b3 += np.random.normal(0, 10 ** b1, a3)
    if b4 = = 1:
        plt.figure()
        plt.scatter(b2, b3, b5 = 'Data points')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Generated Polynomial Points with Noise')
        plt.legend()
        plt.show()
    return b2, b3
if b6 = = "__main__":
    a1 = 0
    a2 = 10
    a3 = 100
    b7 = [1, 2, 3]
    b1 = 1
    b2, b3 = fonk1(a1, a2, a3, b7, b1, b4=1)