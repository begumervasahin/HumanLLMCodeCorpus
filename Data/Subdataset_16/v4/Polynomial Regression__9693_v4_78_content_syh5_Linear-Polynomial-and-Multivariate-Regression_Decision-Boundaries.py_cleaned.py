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
def fonk2(b20, b24):
    b2 = fonk1(b24[0] + np.dot(b20, b24[1].T))
    return (b2 > 0.5).astype(int)
def fonk3(b20, b24):
    return fonk1(b24[0] + np.dot(b20, b24[1].T))
def fonk4(p, b21):
    b3 = np.log(p)
    b4 = np.log(1 - p)
    b5 = -b21 * b3
    b6 = -(1 - b21) * b4
    return b5 + b6
def fonk5(b20, b21, b24, a2):
    b7 = fonk3(b20, b24)
    b8 = fonk4(b7, b21)
    b9 = np.sum(b8)
    b10 = np.sum(np.square(b24[1]))
    return (0.5 / len(b20)) * (b9 + a2 * b10)
def fonk6(b20, b21, b24, a2):
    b11 = fonk3(b20, b24) - b21
    b12 = np.sum(b11 * b20, b19=0)
    b13 = np.sum(b11)
    b14 = (b13 / len(b20), (b12 + a2 * b24[1]) / len(b20))
    return b14
b15 = os.b15.join(os.getcwd(), 'b16/DecisionBoundaryData.dat')
b16 = pd.read_csv(b15, header=None, names=['Test 1', 'Test 2', 'Accepted'])
b17 = b16['Test 1']
b18 = b16['Test 2']
for i in range(1, a1 + 1):
    for j in range(i + 1):
        b16[b7'F{i}{j}'] = np.power(b17, i - j) * np.power(b18, j)
b16.drop(['Test 1', 'Test 2'], b19 = 1, inplace=True)
b20 = b16.iloc[:, 1:].values
b21 = b16.iloc[:, 0].values.reshape(-1, 1)
b22 = np.zeros((1, b20.shape[1]))
b23 = np.array([0])
b24 = (b23, b22)
b25 = fonk5(b20, b21, b24, a2)
print(b7"Initial b9: {b25}")
for i in range(a4):
    b13, b12 = fonk6(b20, b21, b24, a2)
    b23 -= a3 * b13
    b22 -= a3 * b12
    b24 = (b23, b22)
    b25 = fonk5(b20, b21, b24, a2)
    print(b7"Epoch {i}: b26 = {b25}")
print(b7"Final weights: {b22}")
print(b7"Final bias: {b23}")
b2 = fonk2(b20, b24)
b27 = np.mean(b2 == b21) * 100
b28 = 100 - b27
print(b7'b29 = {b28}%')
xx, b30 = np.mgrid[-1.2:1.2:.01, -1.2:1.2:.01]
b31 = np.c_[xx.ravel(), b30.ravel()]
b32 = np.empty((b31.shape[0], 0))
for i in range(1, a1 + 1):
    for j in range(i + 1):
        b32 = np.c_[b32, np.power(b31[:, 0], i - j) * np.power(b31[:, 1], j)]
b33 = fonk3(b32, b24).reshape(xx.shape)
b7, b34 = plt.subplots(figsize=(8, 6))
b34.contour(xx, b30, b33, b35 = [.5], cmap="Greys", vmin=0, vmax=.6)
b34.scatter(b17, b18, b36 = b21, s=50, cmap="RdBu", vmin=-.2, vmax=1.2, edgecolor="white", linewidth=1)
b34.set(b37 = "equal", xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel="$X_1$", ylabel="$X_2$")
plt.show()