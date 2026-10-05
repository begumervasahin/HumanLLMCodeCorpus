import numpy as np
import matplotlib.pyplot as plt
def fonk1(b1 = 10, noise_std=0.3):
    b2 = np.linspace(0, 1, b1)
    b3 = np.random.normal(0, noise_std, b1)
    b4 = np.sin(2 * np.pi * b2) + b3
    return b2, b4
def fonk2(b2, b4, b11):
    b5 = np.array([b2 ** i for i in range(b11 + 1)]).b7
    b6 = np.dot(b5.b7, b5)
    b7 = np.dot(b5.b7, b4)
    b8 = np.linalg.solve(b6, b7)
    return b8
def fonk3(b2, b8):
    return np.dot(np.array([b2 ** i for i in range(len(b8))]), b8)
def fonk4(b2, b4, b17, b18, b11):
    b8 = fonk2(b2, b4, b11)
    b9 = fonk3(b2, b8)
    plt.plot(b2, b9, 'r-', b10 = 'Polynomial Fit')
    plt.plot(b17, b18, 'g-', b10 = 'True Function')
    plt.plot(b2, b4, 'bo', b10 = 'Noisy Samples')
    plt.legend()
    plt.title(b15'Polynomial Regression (b11 = {b11})')
    plt.show()
def fonk5(b2, b4, b11, a2):
    b5 = np.array([b2 ** i for i in range(b11 + 1)]).b7
    b12 = np.dot(b5.b7, b5) + a2 * np.eye(b11 + 1)
    b13 = np.dot(b4, b5)
    b14 = np.linalg.solve(b12, b13)[::-1]
    return np.poly1d(b14)
def fonk6(b2, b4, b17, b18, b11, a2):
    b15 = fonk5(b2, b4, b11, a2)
    b16 = np.linspace(0, 1, len(b17))
    plt.plot(b2, b4, 'bo', b10 = 'Noisy Samples')
    plt.plot(b17, b18, 'g-', b10 = 'True Function')
    plt.plot(b16, b15(b16), 'r-', b10 = 'Regularized Fit')
    plt.legend()
    plt.title(b15'Regularized Regression (b11 = {b11}, lambda={a2})')
    plt.show()
a1 = 1000
b1 = 10
b2, b4 = fonk1(b1)
b17 = np.linspace(0, 1, a1)
b18 = np.sin(2 * np.pi * b17)
for b11 in [0, 1, 3, 9]:
    fonk4(b2, b4, b17, b18, b11)
b11 = 9
a2 = 1
fonk6(b2, b4, b17, b18, b11, a2)