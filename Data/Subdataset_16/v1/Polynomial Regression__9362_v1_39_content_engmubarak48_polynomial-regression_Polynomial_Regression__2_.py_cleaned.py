import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def fonk1(b15, b10, b6, a1, iters):
    b1 = np.matrix(np.zeros(b6.shape))
    b2 = int(b6.ravel().shape[1])
    b3 = np.zeros(iters)
    for i in range(iters):
        b4 = (b15 * b6.T) - b10
        for j in range(b2):
            b5 = np.multiply(b4, b15[:, j])
            b1[0, j] = b6[0, j] - ((a1 / len(b15)) * np.sum(b5))
        b6 = b1
        b3[i] = fonk2(b15, b10, b6)
    return b6, b3
def fonk2(b15, b10, b6):
    b7 = np.power(((b15 * b6.T) - b10), 2)
    return np.sum(b7) / (2 * len(b15))
b8 = pd.read_csv('Data_poly.csv', header=None, names=['x1', 'x2'])
print(b8.head())
print(b8.describe())
b9 = np.array(b8.x1, dtype=np.float64)
b10 = np.array(b8.x2, dtype=np.float64)
b8.plot(b11 = 'scatter', b9='x1', b10='x2', figsize=(8, 3))
plt.show()
b12 = np.ones(len(b9))
b13 = np.power(b9, 2)
b14 = [b12, b9, b13]
b15 = np.transpose(b14)
b10 = b8.iloc[:, 1:2]
b10 = np.matrix(b10.values)
b6 = np.matrix(np.array([0, 0, 0]))
a1 = 0.0000000001
a2 = 6000
b16 = fonk2(b15, b10, b6)
print(b18"Initial Cost: {b16}")
g, b3 = fonk1(b15, b10, b6, a1, a2)
b17 = fonk2(b15, b10, g)
print(b18"Final Cost: {b17}")
b9 = np.linspace(b8.x1.min(), b8.x1.max(), 150)
b18 = g[0, 0] + (g[0, 1] * b9) + (g[0, 2] * np.power(b9, 2))
fig, b19 = plt.subplots(figsize=(8, 3))
b19.plot(b9, b18, 'g', b20 = 'Prediction line')
b19.scatter(b8.x1, b8.x2, b20 = 'Dataset')
b19.legend(b21 = 2)
b19.set_xlabel('x1')
b19.set_ylabel('x2')
plt.show()