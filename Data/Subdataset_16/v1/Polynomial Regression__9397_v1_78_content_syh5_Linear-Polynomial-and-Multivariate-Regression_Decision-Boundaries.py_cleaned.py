import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = 'p6_reg0'
a1 = 6
a2 = 1
a3 = 0.01
a4 = 10000
a5 = 0.0
def fonk1(z):
    return 1 / (1 + np.exp(-z))
def fonk2(X, b27):
    b2 = np.zeros([X.shape[0], 1])
    b3 = fonk3(X, b27)
    for i in range(len(b3)):
        b2[i] = 1 if b3[i] > 0.5 else 0
    return b2
def fonk3(X, b27):
    return fonk1(b27[0] + np.dot(X, np.transpose(b27[1])))
def fonk4(p, y):
    b4 = np.log(p)
    b5 = np.log(1 - p)
    b6 = np.multiply(-y, b4)
    b7 = np.multiply(-(np.ones(y.shape) - y), b5)
    return b6 + b7
def fonk5(X, y, b27, a2):
    b8 = fonk3(X, b27)
    b9 = fonk4(b8, y)
    b10 = np.sum(b9)
    b11 = np.sum(np.square(b27[1]))
    return (0.5 / len(X)) * (b10 + a2 * b11)
def fonk6(X, y, b27, a2):
    b12 = fonk3(X, b27) - y
    b13 = np.multiply(b12, X)
    b14 = np.sum(b13, b21=0)
    b15 = np.sum(b12)
    b16 = ((b15) / len(X), (b14 + a2 * b27[1]) / len(X))
    return b16
b17 = os.b17.join(os.getcwd(), 'data', 'DecisionBoundaryData.dat')
b18 = pd.read_csv(b17, header=None, names=['Test 1', 'Test 2', 'Accepted'])
b19 = b18['Test 1']
b20 = b18['Test 2']
for i in range(1, a1 + 1):
    for j in range(0, i + 1):
        b18[b8'F{i}{j}'] = np.power(b19, i - j) * np.power(b20, j)
b18.drop(['Test 1', 'Test 2'], b21 = 1, inplace=True)
b22 = b18.shape[1]
b23 = b18.iloc[:, 1:b22].values
b24 = b18.iloc[:, 0:1].values
b25 = np.zeros((1, b23.shape[1]))
b26 = np.array([0])
b27 = (b26, b25)
for i in range(a4):
    b15, b14 = fonk6(b23, b24, b27, a2)
    b26 = b27[0] - a3 * b15
    b25 = b27[1] - a3 * b14
    b28 = fonk5(b23, b24, b27, a2)
    b27 = (b26, b25)
    if i % b29 = = 0:
        print(b8"Epoch {i}, Cost: {b28}")
b30 = fonk2(b23, b27)
b31 = np.mean(b30 == b24) * 100
print(b8'Accuracy: {b31}%')
xx, b32 = np.mgrid[-1.2:1.2:.01, -1.2:1.2:.01]
b33 = np.c_[xx.ravel(), b32.ravel()]
b34 = np.array([np.power(xx.ravel(), i - j) * np.power(b32.ravel(), j) for i in range(1, a1 + 1) for j in range(0, i + 1)]).T
b35 = fonk3(b34, b27).reshape(xx.shape)
b8, b36 = plt.subplots(figsize=(8, 6))
b36.contour(xx, b32, b35, b37 = [0.5], cmap="Greys", vmin=0, vmax=0.6)
b36.scatter(b18['F10'], b18['F01'], b38 = b24, s=50, cmap="RdBu", vmin=-0.2, vmax=1.2, edgecolor="white", linewidth=1)
b36.set(b39 = "equal", xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel="$X_1$", ylabel="$X_2$")
plt.show()