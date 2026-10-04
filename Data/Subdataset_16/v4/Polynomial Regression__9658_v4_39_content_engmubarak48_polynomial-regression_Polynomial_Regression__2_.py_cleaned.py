import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def fonk1(b15, b10, b7):
    b1 = np.power(((b15 * b7.T) - b10), 2)
    return np.sum(b1) / (2 * len(b15))
def fonk2(b15, b10, b7, a1, iters):
    b2 = np.matrix(np.zeros(b7.shape))
    b3 = int(b7.ravel().shape[1])
    b4 = np.zeros(iters)
    for i in range(iters):
        b5 = (b15 * b7.T) - b10
        for j in range(b3):
            b6 = np.multiply(b5, b15[:, j])
            b2[0, j] = b7[0, j] - ((a1 / len(b15)) * np.sum(b6))
        b7 = b2
        b4[i] = fonk1(b15, b10, b7)
    return b7, b4
a1 = 1e-10
a2 = 6000
b8 = pd.read_csv('Data_poly.csv', header=None, names=['x1', 'x2'])
print(b8.head())
print(b8.describe())
b9 = np.array(b8.x1, dtype=np.float64)
b10 = np.array(b8.x2, dtype=np.float64)
b8.plot(b11 = 'scatter', b9='x1', b10='x2', figsize=(8, 3))
b12 = np.ones(len(b9))
b13 = np.power(b9, 2)
b14 = [b12, b9, b13]
b15 = np.transpose(b14)
b10 = b8.iloc[:, -1:]
b10 = np.matrix(b10.values)
b7 = np.matrix(np.array([0, 0, 0]))
print(b15.shape, b7.shape, b10.shape)
b16 = fonk1(b15, b10, b7)
print("Initial Cost:", b16)
g, b4 = fonk2(b15, b10, b7, a1, a2)
b17 = fonk1(b15, b10, g)
print("Final Cost:", b17)
b18 = np.linspace(b8.x1.min(), b8.x1.max(), 150)
b19 = g[0, 0] + (g[0, 1] * b18) + (g[0, 2] * np.power(b18, 2))
fig, b20 = plt.subplots(figsize=(8, 3))
b20.plot(b18, b19, 'g', b21 = 'Prediction Line')
b20.scatter(b8.x1, b8.x2, b21 = 'Dataset')
b20.legend(b22 = 2)
b20.set_xlabel('x1')
b20.set_ylabel('x2')
plt.show()