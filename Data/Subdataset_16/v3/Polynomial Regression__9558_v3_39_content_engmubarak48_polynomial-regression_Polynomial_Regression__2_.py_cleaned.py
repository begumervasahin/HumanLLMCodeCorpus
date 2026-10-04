import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def fonk1(b12, b13, b6, a1, a2):
    b1 = np.matrix(np.zeros(b6.shape))
    b2 = b6.shape[1]
    b3 = np.zeros(a2)
    for i in range(a2):
        b4 = (b12 * b6.T) - b13
        for j in range(b2):
            b5 = np.multiply(b4, b12[:, j])
            b1[0, j] = b6[0, j] - ((a1 / len(b12)) * np.sum(b5))
        b6 = b1
        b3[i] = fonk2(b12, b13, b6)
    return b6, b3
def fonk2(b12, b13, b6):
    b7 = np.power(((b12 * b6.T) - b13), 2)
    return np.sum(b7) / (2 * len(b12))
def fonk3(b19):
    b19.plot(b8 = 'scatter', b9='x1', b13='x2', figsize=(8, 3))
    plt.show()
def fonk4(b19):
    b9 = b19['x1'].values
    b10 = np.ones(len(b9))
    b11 = np.power(b9, 2)
    b12 = np.vstack([b10, b9, b11]).T
    b13 = b19['x2'].values.reshape(-1, 1)
    return np.matrix(b12), np.matrix(b13)
def fonk5(b19, b6):
    b14 = np.linspace(b19['x1'].min(), b19['x1'].max(), 150)
    b15 = b6[0, 0] + (b6[0, 1] * b14) + (b6[0, 2] * np.power(b14, 2))
    fig, b16 = plt.subplots(figsize=(8, 3))
    b16.plot(b14, b15, 'g', b17 = 'Prediction line')
    b16.scatter(b19['x1'], b19['x2'], b17 = 'Dataset')
    b16.legend(b18 = 2)
    b16.set_xlabel('x1')
    b16.set_ylabel('x2')
    plt.show()
b19 = pd.read_csv('Data_poly.csv', header=None, names=['x1', 'x2'])
print(b19.head())
print(b19.describe())
fonk3(b19)
b12, b13 = fonk4(b19)
a1 = 1e-10
a2 = 6000
b20 = np.matrix(np.array([0, 0, 0]))
b21 = fonk2(b12, b13, b20)
print(b15"Initial Cost: {b21}")
b6, b3 = fonk1(b12, b13, b20, a1, a2)
b22 = fonk2(b12, b13, b6)
print(b15"Final Cost: {b22}")
fonk5(b19, b6)