import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def fonk1(b14, b10, b7):
    b1 = np.power(((b14 * b7.T) - b10), 2)
    return np.sum(b1) / (2 * len(b14))
def fonk2(b14, b10, b7, a1, a2):
    b2 = np.matrix(np.zeros(b7.shape))
    b3 = int(b7.ravel().shape[1])
    b4 = np.zeros(a2)
    for i in range(a2):
        b5 = (b14 * b7.T) - b10
        for j in range(b3):
            b6 = np.multiply(b5, b14[:, j])
            b2[0, j] = b7[0, j] - ((a1 / len(b14)) * np.sum(b6))
        b7 = b2
        b4[i] = fonk1(b14, b10, b7)
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
b14 = np.column_stack((b12, b9, b13))
b14 = np.matrix(b14)
b10 = np.matrix(b10).T
b7 = np.matrix(np.array([0, 0, 0]))
print(b18"Shape of b14: {b14.shape}")
print(b18"Shape of b7: {b7.shape}")
print(b18"Shape of b10: {b10.shape}")
b15 = fonk1(b14, b10, b7)
print(b18"Initial Cost: {b15}")
b7, b4 = fonk2(b14, b10, b7, a1, a2)
b16 = fonk1(b14, b10, b7)
print(b18"Final Cost: {b16}")
b17 = np.linspace(b8.x1.min(), b8.x1.max(), 150)
b18 = b7[0, 0] + (b7[0, 1] * b17) + (b7[0, 2] * np.power(b17, 2))
fig, b19 = plt.subplots(figsize=(8, 3))
b19.plot(b17, b18, 'g', b20 = 'Prediction Line')
b19.scatter(b8.x1, b8.x2, b20 = 'Dataset')
b19.legend(b21 = 2)
b19.set_xlabel('x1')
b19.set_ylabel('x2')
plt.show()