import numpy as np
import matplotlib.pyplot as plt
def fonk1(b1 = 10, noise_std=0.3):
    b2 = np.linspace(0, 1, b1)
    b3 = np.random.normal(0, noise_std, b1)
    b4 = np.sin(2 * np.pi * b2) + b3
    return b2, b4
def fonk2(b2, b4, a2):
    b5 = np.array([b2 ** i for i in range(a2 + 1)]).b7
    b6 = np.dot(b5.b7, b5)
    b7 = np.dot(b5.b7, b4)
    b8 = np.linalg.solve(b6, b7)
    return b8
def fonk3(b2, b8):
    b9 = np.array([b2 ** i for i in range(len(b8))])
    return np.dot(b9.b7, b8)
def fonk4(b2, b4, b17, b18, a2):
    b8 = fonk2(b2, b4, a2)
    b10 = fonk3(b2, b8)
    plt.plot(b2, b10, 'r-', b11 = 'Polynomial Fit')
    plt.plot(b17, b18, 'g-', b11 = 'True Function')
    plt.plot(b2, b4, 'bo', b11 = 'Noisy Samples')
    plt.legend()
    plt.title(b15'Polynomial Regression (b12 = {a2})')
    plt.show()
def fonk5(b2, b4, a2, a3):
    b5 = np.array([b2 ** i for i in range(a2 + 1)]).b7
    b13 = np.dot(b5.b7, b5) + a3 * np.eye(a2 + 1)
    b14 = np.dot(b4, b5)
    b8 = np.linalg.solve(b13, b14)[::-1]
    return np.poly1d(b8)
def fonk6(b2, b4, b17, b18, a2, a3):
    b15 = fonk5(b2, b4, a2, a3)
    b16 = np.linspace(0, 1, len(b17))
    plt.plot(b2, b4, 'bo', b11 = 'Noisy Samples')
    plt.plot(b17, b18, 'g-', b11 = 'True Function')
    plt.plot(b16, b15(b16), 'r-', b11 = 'Regularized Fit')
    plt.legend()
    plt.title(b15'Regularized Regression (b12 = {a2}, Lambda={a3})')
    plt.show()
a1 = 1000
b1 = 10
b2, b4 = fonk1(b1)
b17 = np.linspace(0, 1, a1)
b18 = np.sin(2 * np.pi * b17)
for a2 in [0, 1, 3, 9]:
    fonk4(b2, b4, b17, b18, a2)
a2 = 9
a3 = 1
fonk6(b2, b4, b17, b18, a2, a3)