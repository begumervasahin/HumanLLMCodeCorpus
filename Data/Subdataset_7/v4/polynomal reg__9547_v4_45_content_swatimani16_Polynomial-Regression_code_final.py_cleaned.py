import numpy as np
import matplotlib.pyplot as plt
a1 = 1000
a2 = 10
b1 = np.linspace(0, 1, a2)
b2 = np.random.normal(0, 0.3, a2)
b3 = np.sin(2 * np.pi * b1) + b2
def fonk1(b1, b7, a3):
    b4 = np.array([b7[i] * (b1 ** i) for i in range(a3 + 1)])
    return b4.sum()
def fonk2(b1, b3, a3):
    b5 = np.zeros((a3 + 1, a3 + 1))
    for i in range(a3 + 1):
        for j in range(a3 + 1):
            b5[i, j] = (b1 ** (i + j)).sum()
    b6 = np.array([((b1 ** i) * b3).sum() for i in range(a3 + 1)])
    return np.linalg.solve(b5, b6)
for a3 in [0, 1, 3, 9]:
    b7 = fonk2(b1, b3, a3)
    b8 = [fonk1(i, b7, a3) for i in b1]
    plt.plot(b1, b8, 'r-')
    plt.plot(b1, b3, 'bo')
    plt.plot(b1, np.sin(2 * np.pi * b1), 'g-')
    plt.show()
def fonk3(b1, a3):
    return b1[:, None] ** np.arange(a3 + 1)
a3 = 9
a4 = 1
b9 = fonk3(b1, a3)
b10 = b9.b6.dot(b9) + a4 * np.eye(a3 + 1)
b11 = b3.dot(b9)
b12 = np.linalg.solve(b10, b11)[::-1]
b13 = np.poly1d(b12)
b14 = np.linspace(0, 1, a1)
fig, b15 = plt.subplots()
b15.plot(b1, b3, 'bo')
b15.plot(b14, np.sin(2 * np.pi * b14), 'g-')
b15.plot(b14, b13(b14), 'r-')
plt.show()