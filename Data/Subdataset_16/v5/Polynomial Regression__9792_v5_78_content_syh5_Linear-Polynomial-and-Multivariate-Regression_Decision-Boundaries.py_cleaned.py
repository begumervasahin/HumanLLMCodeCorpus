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
def fonk2(b19, b32):
    b2 = fonk1(b32[0] + np.dot(b19, b32[1].T))
    return (b2 > 0.5).astype(int)
def fonk3(b19, b32):
    return fonk1(b32[0] + np.dot(b19, b32[1].T))
def fonk4(p, b20):
    b3 = np.log(p)
    b4 = np.log(1 - p)
    b5 = -b20 * b3
    b6 = -(1 - b20) * b4
    return b5 + b6
def fonk5(b19, b20, b32, a2):
    b7 = fonk3(b19, b32)
    b8 = fonk4(b7, b20)
    b9 = np.sum(b8)
    b10 = np.sum(np.square(b32[1]))
    return (0.5 / len(b19)) * (b9 + a2 * b10)
def fonk6(b19, b20, b32, a2):
    b11 = fonk3(b19, b32) - b20
    b12 = np.sum(b11 * b19, b18=0)
    b13 = np.sum(b11)
    b14 = (b13 / len(b19), (b12 + a2 * b32[1]) / len(b19))
    return b14
def fonk7(b29, a1):
    b15 = pd.read_csv(b29, header=None, names=['Test 1', 'Test 2', 'Accepted'])
    b16 = b15['Test 1']
    b17 = b15['Test 2']
    for i in range(1, a1 + 1):
        for j in range(i + 1):
            b15[b7'F{i}{j}'] = np.power(b16, i - j) * np.power(b17, j)
    b15.drop(['Test 1', 'Test 2'], b18 = 1, inplace=True)
    b19 = b15.iloc[:, 1:].values
    b20 = b15.iloc[:, 0].values.reshape(-1, 1)
    return b19, b20
def fonk8(b16, b17, b20, a1, b32):
    xx, b21 = np.mgrid[-1.2:1.2:.01, -1.2:1.2:.01]
    b22 = np.c_[xx.ravel(), b21.ravel()]
    b23 = np.empty((b22.shape[0], 0))
    for i in range(1, a1 + 1):
        for j in range(i + 1):
            b23 = np.c_[b23, np.power(b22[:, 0], i - j) * np.power(b22[:, 1], j)]
    b24 = fonk3(b23, b32).reshape(xx.shape)
    b7, b25 = plt.subplots(figsize=(8, 6))
    b25.contour(xx, b21, b24, b26 = [.5], cmap="Greys", vmin=0, vmax=.6)
    b25.scatter(b16, b17, b27 = b20, s=50, cmap="RdBu", vmin=-.2, vmax=1.2, edgecolor="white", linewidth=1)
    b25.set(b28 = "equal", xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel="$X_1$", ylabel="$X_2$")
    plt.show()
def fonk9():
    b29 = os.b29.join(os.getcwd(), 'b15/DecisionBoundaryData.dat')
    b19, b20 = fonk7(b29, a1)
    b30 = np.zeros((1, b19.shape[1]))
    b31 = np.array([0])
    b32 = (b31, b30)
    b33 = fonk5(b19, b20, b32, a2)
    print(b7"Initial b9: {b33}")
    for epoch in range(a4):
        b13, b12 = fonk6(b19, b20, b32, a2)
        b31 -= a3 * b13
        b30 -= a3 * b12
        b32 = (b31, b30)
        b9 = fonk5(b19, b20, b32, a2)
        print(b7"Epoch {epoch}: b34 = {b9}")
    print(b7"Final weights: {b30}")
    print(b7"Final bias: {b31}")
    b35 = fonk2(b19, b32)
    b36 = np.mean(b35 == b20) * 100
    b37 = 100 - b36
    print(b7'b38 = {b37}%')
    fonk8(b15['Test 1'], b15['Test 2'], b20, a1, b32)
if b39 = = "__main__":
    fonk9()