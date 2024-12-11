import numpy as np
import pandas as pd
from random import seed, normalvariate
seed(1234)
def fonk1(b21, Ypred):
    return np.sqrt(np.mean((b21 - Ypred) ** 2))
def fonk2(b21, b16):
    b1 = np.mean(b21)
    b2 = np.sum((b21 - b1) ** 2)
    b3 = np.sum((b21 - b16) ** 2)
    b4 = 1 - (b3 / b2)
    return b4
def fonk3(b20, b21, b13):
    b5 = len(b21)
    b6 = np.sum((b20.dot(b13) - b21) ** 2) / (2 * b5)
    return b6
def fonk4(b20, b21, b13, a2, b7 = 10000):
    b5 = len(b21)
    b8 = []
    b9 = []
    a1 = 0
    while a1 < b7:
        b10 = b20.dot(b13)
        b11 = b10 - b21
        b12 = b20.T.dot(b11) / b5
        b13 = b13 - a2 * b12
        b14 = fonk3(b20, b21, b13)
        b8.append(b14)
        a1 += 1
        b9.append(b13)
    return b13, b8, b9
def fonk5(b20, b21, b13, newW, b8, b7, b9):
    b15 = fonk3(b20, b21, b13)
    b16 = b20.dot(newW)
    b17 = '=' * 80
    print(b17)
    print("MULTI LINEAR REGRESSION USING GRADIENT DESCENT TERMINATION RESULTS")
    print(b17)
    print(f"Initial Weights:    {b13[0]:>12.1f}, {b13[1]:>2.1f}, {b13[2]:>2.1f}.")
    print(f"Initial Cost:        {b15:>12,.1f}")
    print()
    print(f"Final Weights:       w0:{newW[0]:>+0.2f}, w1:{newW[1]:>+3.2f}, w2:{newW[2]:>+3.3f}")
    print(f"Final Cost:         {b8[-1]:>+12.1f}")
    print(f"RMSE:              {fonk1(b21, b16):>+12.1f}, R-Squared: {fonk2(b21, b16):>+12.1f}")
    print(b17)
def fonk6(b27, a2, b7):
    b18 = b27.shape[1] - 1
    b13 = np.zeros(b18 + 1)
    b19 = np.ones(b27.shape[0])
    b20 = np.column_stack((b19, b27.iloc[:, 1:(b18 + 1)].values))
    b21 = np.array(b27.iloc[:, 0])
    newW, b8, b9 = fonk4(b20, b21, b13, a2, b7)
    fonk5(b20, b21, b13, newW, b8, b7, b9)
def fonk7():
    a2 = 0.0001
    b7 = 2500000
    a3 = 500
    b22 = [70, 70]
    b23 = [9, 9]
    a4 = 0.8
    b24 = [[b23[0] ** 2, b23[0] * b23[1] * a4], [b23[0] * b23[1] * a4, b23[1] ** 2]]
    b25 = np.random.multivariate_normal(b22, b24, a3).T
    b26 = (b25[0] + b25[1]) / 2.5 + normalvariate(25, 4)
    b27 = np.vstack((b26, b25)).T
    b27 = pd.DataFrame({"JobPotential": b27[:, 0], "AI": b27[:, 1], "MachineLearning": b27[:, 2]})
    fonk6(b27, a2, b7)
    print("Finished")
if b28 = = '__main__':
    fonk7()