import numpy as np
import matplotlib.pyplot as plt
a1 = 1000
a2 = 10
b1 = np.linspace(0, 1, a2)
b2 = np.random.normal(0, 0.3, a2)
b3 = np.sin(2 * np.pi * b1) + b2
def fonk1(x, b7, a3):
    b4 = np.array([b7[i] * (x ** i) for i in range(a3 + 1)])
    return np.sum(b4)
def fonk2(x, t, a3):
    b5 = np.zeros((a3 + 1, a3 + 1))
    for i in range(a3 + 1):
        for j in range(a3 + 1):
            b5[i, j] = (x ** (i + j)).sum()
    b6 = np.array([((x ** i) * t).sum() for i in range(a3 + 1)])
    return np.linalg.solve(b5, b6)
def fonk3(x, a3):
    return x[:, None] ** np.arange(a3 + 1)
for a3 in [0, 1, 3, 9]:
    b7 = fonk2(b1, b3, a3)
    b8 = [fonk1(i, b7, a3) for i in b1]
    plt.plot(b1, b8, 'r-', b9 = f'Degree {a3}')
    plt.plot(b1, b3, 'bo', b9 = 'Sample Points')
    plt.plot(b1, np.sin(2 * np.pi * b1), 'g-', b9 = 'True Sine Curve')
    plt.legend()
    plt.show()
a3 = 9
a4 = 1
b10 = fonk3(b1, a3)
b11 = b10.b6.dot(b10) + a4 * np.eye(a3 + 1)
b12 = b3.dot(b10)
b13 = np.linalg.solve(b11, b12)[::-1]
b14 = np.poly1d(b13)
b15 = np.linspace(0, 1, a1)
plt.plot(b1, b3, 'bo', b9 = 'Sample Points')
plt.plot(b15, np.sin(2 * np.pi * b15), 'g-', b9 = 'True Sine Curve')
plt.plot(b15, b14(b15), 'r-', b9 = 'Fitted Polynomial')
plt.legend()
plt.show()