import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, a2, a3, b6, b1 = 1, b4=1):
    b2 = np.linspace(a1, a2, a3)
    b3 = np.zeros_like(b2)
    for i, b6 in enumerate(b6):
        b3 += b6 * b2 ** i
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
a1 = 0
a2 = 10
a3 = 100
b6 = [1, 2, 3]
b1 = 1
b2, b3 = fonk1(a1, a2, a3, b6, b1, b4=1)