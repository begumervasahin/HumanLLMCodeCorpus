import numpy as np
import matplotlib.pyplot as plt
def fonk1():
    return 0, -10, -50, -10, 50
def fonk2(b8, b9, b12, b13, b14, b15, b0, b1, b2, b3, b11):
    b1 = len(b9)
    b2 = b0 + b1 * b12 + b2 * b13 + b3 * b14 + b11 * b15
    b3 = (-2 / b1) * np.sum(b9 - b2)
    b11 = (-2 / b1) * np.sum(b12 * (b9 - b2))
    b5 = (-2 / b1) * np.sum(b13 * (b9 - b2))
    b6 = (-2 / b1) * np.sum(b14 * (b9 - b2))
    b7 = (-2 / b1) * np.sum(b15 * (b9 - b2))
    return b3, b11, b5, b6, b7
def fonk3(b0, b1, b2, b3, b11, b3, b11, b5, b6, b7, a1):
    b0 -= a1 * b3
    b1 -= a1 * b11
    b2 -= a1 * b5
    b3 -= a1 * b6
    b11 -= a1 * b7
    return b0, b1, b2, b3, b11
def fonk4():
    b8 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    b9 = np.array([4, 5, 6, 8, 11, 15, 20, 30, 50, 100])
    plt.scatter(b8, b9, b10 = 50, b17='red')
    b0, b1, b2, b3, b11 = fonk1()
    a1 = 0.001
    b12 = b8
    b13 = np.array([0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1])
    b14 = np.array([0.001, 0.008, 0.027, 0.064, 0.125, 0.216, 0.343, 0.512, 0.729, 1])
    b15 = np.array([0.00001, 0.0016, 0.0081, 0.0256, 0.0625, 0.1296, 0.2401, 0.4096, 0.6561, 1])
    for _ in range(1000):
        b3, b11, b5, b6, b7 = fonk2(b8, b9, b12, b13, b14, b15, b0, b1, b2, b3, b11)
        b0, b1, b2, b3, b11 = fonk3(b0, b1, b2, b3, b11, b3, b11, b5, b6, b7, a1)
    b16 = b0 + b1 * b12 + b2 * b13 + b3 * b14 + b11 * b15
    plt.plot(b8, b16, b17 = 'blue')
    plt.show()
if b18 = = "__main__":
    fonk4()