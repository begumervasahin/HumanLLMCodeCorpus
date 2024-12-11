import numpy as np
import pandas as pd
from random import random, seed
def fonk1(b22, Ypred):
    b1 = np.sqrt(sum((b22 - Ypred) ** 2) / len(b22))
    return b1
def fonk2(b22, b17):
    b2 = np.mean(b22)
    b3 = sum((b22 - b2) ** 2)
    b4 = sum((b22 - b17) ** 2)
    b5 = 1 - (b4 / b3)
    return b5
def fonk3(b21, b22, b14):
    b6 = len(b22)
    b7 = np.sum((b21.dot(b14) - b22) ** 2) / (2 * b6)
    return b7
def fonk4(b21, b22, b14, a2, b8 = 10000):
    b6 = len(b22)
    b9 = []
    b10 = []
    a1 = 0
    while a1 < b8:
        b11 = b21.dot(b14)
        b12 = b11 - b22
        b13 = b21.T.dot(b12) / b6
        b14 = b14 - a2 * b13
        b15 = fonk3(b21, b22, b14)
        b9.append(b15)
        a1 += 1
        b10.append(b14)
    return b14, b9, b10
def fonk5(b21, b22, b14, newW, b9, b8, b10):
    b16 = fonk3(b21, b22, b14)
    b17 = b21.dot(newW)
    b18 = '=' * 80
    print(b18)
    print("MULTI LINEAR REGRESSION USING GRADIENT DESCENT TERMINATION RESULTS")
    print(b18)
    print(f"Initial Weights were:    {b14[0]:>12.1f}, {b14[1]:>2.1f}, {b14[2]:>2.1f}.")
    print(f"   With initial b15:    {b16:>12,.1f}.")
    print()
    print(f"       Final weights:    w0:{newW[0]:>+0.2f}, w1:{newW[1]:>+3.2f}, w2:{newW[2]:>+3.3f}.")
    print(f"          Final b15:    {b9[-1]:>+12.1f}.")
    print(f"                RMSE:    {fonk1(b22, b17):>+12.1f}, R-Squared: {fonk2(b22, b17):>+12.1f}")
    print(b18)
def fonk6(b28, a2, b8):
    b19 = b28.shape[1] - 1
    b14 = (b19 + 1) * [0]
    b20 = np.ones(b28.shape[0])
    b21 = np.column_stack((b20, b28.iloc[:, 1:(b19 + 1)].values))
    b22 = np.array(b28.iloc[:, 0])
    newW, b9, b10 = fonk4(b21, b22, b14, a2, b8)
    fonk5(b21, b22, b14, newW, b9, b8, b10)
def fonk7():
    a2 = 0.0001
    b8 = 2500000
    np.random.seed(1234)
    a3 = 500
    b23 = [70, 70]
    b24 = [9, 9]
    a4 = 0.8
    b25 = [[b24[0] ** 2, b24[0] * b24[1] * a4], [b24[0] * b24[1] * a4, b24[1] ** 2]]
    b26 = np.random.multivariate_normal(b23, b25, a3).T
    b27 = (b26[0] + b26[1]) / 2.5 + np.random.normal(loc=25, scale=4, size=a3)
    b28 = np.vstack((b27, b26)).T
    b28 = pd.DataFrame({"JobPotential": b28[:, 0], "AI": b28[:, 1], "MachineLearning": b28[:, 2]})
    fonk6(b28, a2, b8)
    print("Finished")
if b29 = = '__main__':
    fonk7()