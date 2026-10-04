import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('CMP3751M_ML_Assignment 1_Task1 - dataset - pol_regression.csv')
b2 = b1['b2'].values
b3 = b1['b3'].values
def fonk1(b2, b15):
    b4 = np.vander(b2, b15 + 1, increasing=True)
    return b4
def fonk2(features_train, y_train, b15):
    b4 = fonk1(features_train, b15)
    b5 = b4.T @ b4
    b6 = np.linalg.solve(b5, b4.T @ y_train)
    return b6
def fonk3(b4, Y, train_split):
    b7 = int(len(b4) * train_split)
    return b4[:b7], b4[b7:], Y[:b7], Y[b7:]
def fonk4(b2, b3, b15):
    X_train, X_test, Y_train, b8 = fonk3(b2, b3, 0.7)
    b9 = np.zeros(b15)
    b10 = np.zeros(b15)
    for i in range(1, b15 + 1):
        b11 = fonk1(np.asarray(X_train), i)
        b12 = fonk1(np.asarray(X_test), i)
        b13 = fonk2(np.asarray(X_train), np.asarray(Y_train), i)
        b9[i - 1] = np.sqrt(np.mean((b11 @ b13 - np.asarray(Y_train)) ** 2))
        b10[i - 1] = np.sqrt(np.mean((b12 @ b13 - np.asarray(b8)) ** 2))
    plt.figure()
    plt.title(f'{b15} Degree Polynomial Regression')
    plt.semilogy(range(1, b15 + 1), b9, b14 = 'Training RMSE')
    plt.semilogy(range(1, b15 + 1), b10, b14 = 'Test RMSE')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('RMSE')
    plt.legend()
    plt.show()
    return b9, b10
def fonk5(b2, b19, b3, b15, b18):
    if b15 = = 0:
        b16 = np.mean(b3)
    else:
        b17 = fonk2(b2, b3, b15)
        b12 = fonk1(b19, b15)
        b16 = b12 @ b17
    plt.figure()
    plt.plot(b2, b3, 'bo', b14 = 'Data Points')
    plt.plot(b19, b16, b18 = b18, b14=f'{b15} Degree Polynomial')
    plt.title(f'{b15} Degrees')
    plt.xlabel('b2')
    plt.ylabel('b3')
    plt.legend()
    plt.show()
def fonk6(b2, b3, b15):
    b9, b10 = fonk4(b2, b3, b15)
    plt.figure()
    plt.semilogy(range(1, b15 + 1), b9, b14 = 'Training RMSE')
    plt.semilogy(range(1, b15 + 1), b10, b14 = 'Test RMSE')
    plt.title(f'{b15} Degree Polynomial Regression Evaluation')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('RMSE')
    plt.legend()
    plt.show()
b19 = np.linspace(-5, 5, len(b2))
for i in range(0, 5):
    fonk5(b2, b19, b3, i, 'r')
fonk5(b2, b19, b3, 5, 'r')
fonk5(b2, b19, b3, 10, 'r')
for i in range(0, 5):
    fonk4(b2, b3, i)
fonk4(b2, b3, 5)
fonk4(b2, b3, 10)