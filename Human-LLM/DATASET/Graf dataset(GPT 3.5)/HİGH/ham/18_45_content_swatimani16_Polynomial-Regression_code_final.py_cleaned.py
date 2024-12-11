import numpy as np
import matplotlib.pyplot as plt
a1 = 1000
a2 = 10
b1 = np.linspace(0,1,a2)
b2 = np.random.normal(0,0.3,a2)
b3 = np.sin(2*np.pi*b1)+b2
b4 = np.linspace(0,1,a1)
b5 = np.sin(2*np.pi*b4)
def fonk1(b1, b9, a3):
    b6 = np.array([b9[i] * (b1 ** i) for i in range(a3 + 1)])
    return b6.sum()
def fonk2(b1, b3, a3):
    b7 = np.zeros((a3 + 1, a3 + 1))
    for i in range(a3 + 1):
        for j in range(a3 + 1):
            b7[i, j] = (b1 ** (i + j)).sum()
    b8 = np.array([((b1 ** i) * b3).sum() for i in range(a3 + 1)])
    return np.linalg.solve(b7, b8)
for a3 in [0, 1, 3, 9]:
    b9 = fonk2(b1,b3,a3)
    print(b9)
    b10 = [fonk1(i, b9, a3) for i in b1]
    plt.plot(b1, b10, 'r-')
    plt.plot(b4, b5, 'g-')
    plt.plot(b1, b3, 'bo')
    plt.show()
def fonk3(b1, a3):
    return b1[:,None] ** np.arange(a3 + 1)
a3 = 9
a4 = 1
b11 = fonk3(b1, a3)
b12 = b11.b8.dot(b11) + a4 * np.eye(a3+1)
b13 = b3.dot(b11)
b14 = np.linalg.solve(b12, b13)[::-1]
b15 = np.poly1d(b14)
b16 = np.linspace(0, 1, a1)
fig, b17 = plt.subplots()
b17.plot(b1, b3, 'bo')
b17.plot(b16, np.sin(2 * np.pi * b16), 'g-')
b17.plot(b16, b15(b16), 'r-')
plt.show()