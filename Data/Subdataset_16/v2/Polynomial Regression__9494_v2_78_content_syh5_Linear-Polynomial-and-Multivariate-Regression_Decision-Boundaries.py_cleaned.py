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
def fonk2(b15, b19):
    b2 = fonk3(b15, b19)
    return np.where(b2 > 0.5, 1, 0)
def fonk3(b15, b19):
    return fonk1(np.dot(b15, b19[1].T) + b19[0])
def fonk4(p, b16):
    b3 = -b16 * np.log(p) - (1 - b16) * np.log(1 - p)
    return b3
def fonk5(b15, b16, b19, a2):
    b4 = fonk3(b15, b19)
    b3 = fonk4(b4, b16)
    b5 = np.sum(b3)
    b6 = np.sum(np.square(b19[1]))
    return (0.5 / len(b15)) * (b5 + a2 * b6)
def fonk6(b15, b16, b19, a2):
    b7 = fonk3(b15, b19) - b16
    b8 = np.dot(b7.T, b15) + a2 * b19[1]
    b9 = np.sum(b7)
    return b9 / len(b15), b8 / len(b15)
b10 = os.path.join(os.getcwd(), 'b11', 'DecisionBoundaryData.dat')
b11 = pd.read_csv(b10, header=None, names=['Test 1', 'Test 2', 'Accepted'])
b12 = b11['Test 1']
b13 = b11['Test 2']
for i in range(1, a1 + 1):
    for j in range(i + 1):
        b11[b4'F{i}{j}'] = np.power(b12, i - j) * np.power(b13, j)
b11.drop(['Test 1', 'Test 2'], b14 = 1, inplace=True)
b15 = b11.iloc[:, 1:].values
b16 = b11.iloc[:, 0:1].values
b17 = np.zeros((1, b15.shape[1]))
b18 = np.array([0])
b19 = (b18, b17)
for epoch in range(a4):
    b9, b8 = fonk6(b15, b16, b19, a2)
    b18 -= a3 * b9
    b17 -= a3 * b8
    b19 = (b18, b17)
    if epoch % b20 = = 0:
        b5 = fonk5(b15, b16, b19, a2)
        print(b4"Epoch {epoch}, Cost: {b5}")
b21 = fonk2(b15, b19)
b22 = np.mean(b21 == b16) * 100
print(b4'Accuracy: {b22}%')
xx, b23 = np.mgrid[-1.2:1.2:.01, -1.2:1.2:.01]
b24 = np.c_[xx.ravel(), b23.ravel()]
b25 = np.array([np.power(xx.ravel(), i - j) * np.power(b23.ravel(), j) for i in range(1, a1 + 1) for j in range(i + 1)]).T
b26 = fonk3(b25, b19).reshape(xx.shape)
fig, b27 = plt.subplots(figsize=(8, 6))
b27.contour(xx, b23, b26, b28 = [0.5], cmap="Greys", vmin=0, vmax=0.6)
b27.scatter(b12, b13, b29 = b16.ravel(), s=50, cmap="RdBu", vmin=-0.2, vmax=1.2, edgecolor="white", linewidth=1)
b27.set(b30 = "equal", xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel="$X_1$", ylabel="$X_2$")
plt.show()