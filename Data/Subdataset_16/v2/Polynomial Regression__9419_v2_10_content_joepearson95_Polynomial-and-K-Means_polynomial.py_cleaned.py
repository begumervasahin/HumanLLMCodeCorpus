import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('CMP3751M_ML_Assignment 1_Task1 - dataset - pol_regression.csv')
b2 = b1['b2'].values
b3 = b1['b3'].values
def fonk1(b2, b18):
    b4 = np.ones((b2.shape[0], b18 + 1))
    for i in range(1, b18 + 1):
        b4[:, i] = b2 ** i
    return b4
def fonk2(features_train, y_train, b18):
    b4 = fonk1(features_train, b18)
    b5 = np.linalg.solve(b4.T.dot(b4), b4.T.dot(y_train))
    return b5
def fonk3(b4, Y, b6 = 0.7):
    b7 = int(len(b4) * b6)
    X_train, b8 = b4[:b7], b4[b7:]
    Y_train, b9 = Y[:b7], Y[b7:]
    return X_train, b8, Y_train, b9
def fonk4(b2, b3, max_degree):
    X_train, b8, Y_train, b9 = fonk3(b2, b3, 0.7)
    b10 = []
    b11 = []
    for b18 in range(1, max_degree + 1):
        b12 = fonk1(X_train, b18)
        b13 = fonk1(b8, b18)
        b14 = fonk2(X_train, Y_train, b18)
        b15 = b12.dot(b14)
        b16 = b13.dot(b14)
        b10.append(np.sqrt(np.mean((b15 - Y_train) ** 2)))
        b11.append(np.sqrt(np.mean((b16 - b9) ** 2)))
    plt.figure()
    plt.semilogy(range(1, max_degree + 1), b10, b17 = 'RMSE Train')
    plt.semilogy(range(1, max_degree + 1), b11, b17 = 'RMSE Test')
    plt.title(f'{max_degree} Degree')
    plt.xlabel("Degree of Polynomial")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()
    return b10, b11
def fonk5(b2, b21, b3, b18, b20):
    if b18 = = 0:
        b19 = np.mean(b3) * np.ones_like(b21)
    else:
        b14 = fonk2(b2, b3, b18)
        b13 = fonk1(b21, b18)
        b19 = b13.dot(b14)
    plt.figure()
    plt.plot(b2, b3, 'bo', b17 = 'Data Points')
    plt.plot(b21, b19, b20 = b20, b17=f'{b18} Degrees')
    plt.xlabel("Input Feature")
    plt.ylabel("Target Value")
    plt.legend()
    plt.show()
def fonk6(b2, b3, max_degree):
    b10, b11 = fonk4(b2, b3, max_degree)
    plt.figure()
    plt.semilogy(range(1, max_degree + 1), b10, b17 = 'RMSE Train')
    plt.semilogy(range(1, max_degree + 1), b11, b17 = 'RMSE Test')
    plt.title(f'{max_degree} Degrees')
    plt.xlabel("Degree of Polynomial")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()
b21 = np.linspace(min(b2), max(b2), len(b2))
for i in range(4):
    fonk5(b2, b21, b3, i, 'r')
fonk5(b2, b21, b3, 5, 'r')
fonk5(b2, b21, b3, 10, 'r')
for i in range(4):
    fonk4(b2, b3, i)
fonk4(b2, b3, 5)
fonk4(b2, b3, 10)