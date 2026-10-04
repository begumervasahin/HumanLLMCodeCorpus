import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def fonk1(b16, b9,b6, a1, iters):
    b1 = np.matrix(np.zeros(b6.shape))
    b2 = int(b6.ravel().shape[1])
    b3 = np.zeros(iters)
    for i in range(iters):
        b4 = (b16 * b6.T) - b9
        for j in range(b2):
            b5 = np.multiply(b4, b16[:,j])
            b1[0,j] = b6[0,j] - ((a1 / len(b16)) * np.sum(b5))
        b6 = b1
        b3[i] = fonk2(b16, b9,b6)
    return b6, b3
a1 = 0.0000000001
a2 = 6000
b7 = pd.read_csv('Data_poly.csv', header=None, names=['x1', 'x2'])
b7.head()
b7.describe()
b8 = np.array(b7.x1, dtype = np.float64)
b9 = np.array(b7.x2, dtype = np.float64)
b7.plot(b10 = 'scatter', b8 = 'x1', b9 = 'x2', figsize = (8,3))
def fonk2(b16, b9, b6):
    b11 = np.power(((b16*b6.T) - b9),2)
    return np.sum(b11) / (2 * len(b16))
b12 = np.ones(len(b8))
b13 = np.power(b8,2)
b14 = [b12, b8, b13]
np.shape(b14)
b15 = b7.shape[1]
b16 = np.transpose(b14)
b9 = b7.iloc[:,b15-1:b15]
b9.head()
b9 = np.matrix(b9.values)
b6 = np.matrix(np.array([0,0,0]))
b16.shape,b6.shape, b9.shape
fonk2(b16,b9,b6)
b8 = np.linspace(b7.x1.min(), b7.x1.max(), 150)
g, b3 = fonk1(b16, b9,b6,a1, a2)
fonk2(b16, b9, g)
b17 = g[0, 0] + (g[0, 1] * b8) + (g[0, 2] * np.power(b8,2))
fig, b18 = plt.subplots(figsize=(8,3))
b18.plot(b8, b17, 'g', b19 = 'Prediction line')
b18.scatter(b7.x1, b7.x2, b19 = 'Dataset')
b18.legend(b20 = 2)
b18.set_xlabel('x1')
b18.set_ylabel('x2')