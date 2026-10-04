import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('CMP3751M_ML_Assignment 1_Task1 - dataset - pol_regression.csv')
b2 = b1['b2'].values
b3 = b1['b3'].values
def fonk1(b2, b14):
    b4 = np.ones(b2.shape)
    for i in range(1, b14 + 1):
        b4 = np.column_stack((b4, b2 ** i))
    return b4
def fonk2(features_train, y_train, b14):
    b4 = fonk1(features_train, b14)
    b5 = b4.transpose().dot(b4)
    b6 = np.linalg.solve(b5, b4.transpose().dot(y_train))
    return b6
def fonk3(b4, Y, train_split):
    X_train, X_test, Y_train, b7 = [], [], [], []
    for position in range(len(b4)):
        if position >= len(b4) * train_split:
            X_test.append(b4[position])
            b7.append(Y[position])
        else:
            X_train.append(b4[position])
            Y_train.append(Y[position])
    return np.array(X_train), np.array(X_test), np.array(Y_train), np.array(b7)
def fonk4(b2, b3, b14):
    X_train, X_test, Y_train, b7 = fonk3(b2, b3, 0.7)
    b8 = np.zeros(b14)
    b9 = np.zeros(b14)
    for i in range(1, b14 + 1):
        b10 = fonk1(X_train, i)
        b11 = fonk1(X_test, i)
        b12 = fonk2(X_train, Y_train, i)
        b8[i - 1] = np.sqrt(((b10.dot(b12) - Y_train) ** 2).mean())
        b9[i - 1] = np.sqrt(((b11.dot(b12) - b7) ** 2).mean())
    plt.figure()
    plt.title(f'{b14} Degree')
    plt.semilogy(range(1, b14 + 1), b8, b13 = 'RMSE Train')
    plt.semilogy(range(1, b14 + 1), b9, b13 = 'RMSE Test')
    plt.legend()
    plt.show()
    return b8, b9
def fonk5(b2, b18, b3, b14, b17):
    if b14 = = 0:
        b15 = np.mean(b3)
    else:
        b15 = fonk2(b2, b3, b14)
    b11 = fonk1(b18, b14)
    b16 = b11.dot(b15)
    plt.figure()
    plt.plot(b2, b3, 'bo', b13 = 'Data Points')
    plt.plot(b18, b16, b17 = b17, b13=f'{b14} Degrees')
    plt.xlabel("Range of Polynomials")
    plt.ylabel("Points of Polynomial")
    plt.legend()
    plt.show()
def fonk6(b2, b3, b14):
    b8, b9 = fonk4(b2, b3, b14)
    plt.figure()
    plt.semilogy(range(1, b14 + 1), b8, b13 = 'RMSE Train')
    plt.semilogy(range(1, b14 + 1), b9, b13 = 'RMSE Test')
    plt.title(f'{b14} Degrees')
    plt.xlabel("Degree of RMSE")
    plt.ylabel("Points of RMSE")
    plt.legend()
    plt.show()
b18 = np.linspace(-5, 5, len(b2))
b19 = np.linspace(-5, 5, len(b2))
for i in range(4):
    fonk5(b2, b18, b3, i, 'r')
fonk5(b2, b18, b3, 5, 'r')
fonk5(b2, b18, b3, 10, 'r')
for i in range(4):
    fonk4(b2, b3, i)
fonk4(b2, b3, 5)
fonk4(b2, b3, 10)