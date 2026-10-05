import numpy as np
import pandas as pd
from random import seed, normalvariate
def fonk1(b20, Y_pred):
    return np.sqrt(np.mean((b20 - Y_pred) ** 2))
def fonk2(b20, Y_pred):
    b1 = np.mean(b20)
    b2 = np.sum((b20 - b1) ** 2)
    b3 = np.sum((b20 - Y_pred) ** 2)
    b4 = 1 - (b3 / b2)
    return b4
def fonk3(b19, b20, b13):
    b5 = len(b20)
    b6 = np.sum((b19.dot(b13) - b20) ** 2) / (2 * b5)
    return b6
def fonk4(b19, b20, b13, alpha, b7 = 10000):
    b5 = len(b20)
    b8 = []
    b9 = []
    a1 = 0
    while a1 < b7:
        b10 = b19.dot(b13)
        b11 = b10 - b20
        b12 = b19.T.dot(b11) / b5
        b13 = b13 - alpha * b12
        b6 = fonk3(b19, b20, b13)
        b8.append(b6)
        b9.append(b13)
        a1 += 1
    return b13, b8, b9
def fonk5(b19, b20, b17, final_weights, b8, b7):
    b14 = fonk3(b19, b20, b17)
    b10 = b19.dot(final_weights)
    b15 = '=' * 80
    print(b15)
    print("MULTI LINEAR REGRESSION USING GRADIENT DESCENT TERMINATION RESULTS")
    print(b15)
    print(f"Initial Weights:    {b17[0]:>12.1f}, {b17[1]:>2.1f}, {b17[2]:>2.1f}.")
    print(f"Initial Cost:        {b14:>12,.1f}")
    print()
    print(f"Final Weights:       w0:{final_weights[0]:>+0.2f}, w1:{final_weights[1]:>+3.2f}, w2:{final_weights[2]:>+3.3f}")
    print(f"Final Cost:         {b8[-1]:>+12.1f}")
    print(f"RMSE:              {fonk1(b20, b10):>+12.1f}, R-Squared: {fonk2(b20, b10):>+12.1f}")
    print(b15)
def fonk6(b26, a2, b7):
    b16 = b26.shape[1] - 1
    b17 = np.zeros(b16 + 1)
    b18 = np.ones(b26.shape[0])
    b19 = np.column_stack((b18, b26.iloc[:, 1:(b16 + 1)].values))
    b20 = np.array(b26.iloc[:, 0])
    final_weights, b8, b9 = fonk4(b19, b20, b17, a2, b7)
    fonk5(b19, b20, b17, final_weights, b8, b7)
def fonk7():
    a2 = 0.0001
    b7 = 2500000
    np.random.seed(1234)
    a3 = 500
    b21 = [70, 70]
    b22 = [9, 9]
    a4 = 0.8
    b23 = [[b22[0] ** 2, b22[0] * b22[1] * a4], [b22[0] * b22[1] * a4, b22[1] ** 2]]
    b24 = np.random.multivariate_normal(b21, b23, a3).T
    b25 = (b24[0] + b24[1]) / 2.5 + normalvariate(25, 4)
    b26 = np.vstack((b25, b24)).T
    b26 = pd.DataFrame({"JobPotential": b26[:, 0], "AI": b26[:, 1], "MachineLearning": b26[:, 2]})
    fonk6(b26, a2, b7)
    print("Finished")
if b27 = = '__main__':
    fonk7()