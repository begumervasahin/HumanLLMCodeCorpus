import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
def fonk1(a1, a2, a3, b6, b1 = 1, b7=True):
    b2 = np.linspace(a1, a2, a3)
    b3 = np.polyval(b6[::-1], b2)
    if b1 > 0:
        b4 = np.random.normal(0, 10 ** b1, a3)
        b3 += b4
    if b7:
        plt.figure()
        plt.scatter(b2, b3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Generated Polynomial Points with Noise')
        plt.show()
    return b2, b3
if b5 = = "__main__":
    a1 = 0
    a2 = 10
    a3 = 100
    b6 = [1, -2, 3]
    b1 = 1
    b7 = True
    b2, b3 = fonk1(a1, a2, a3, b6, b1, b7)