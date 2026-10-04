import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
b1 = pd.read_csv('CMP3751M_ML_Assignment 1_Task1_pol_regression.csv')
b2 = [0, 1, 2, 3, 5, 10]
b3 = []
b4 = []
b5 = np.sort(b1['b5'].values)
b6 = np.sort(b1['b6'].values)
plt.figure()
plt.plot(b5, b6, 'bo')
plt.xlabel('b7')
plt.ylabel('Y')
plt.title('Original Data')
plt.show()
def fonk1(b5, degree):
    b7 = np.ones(b5.shape)
    for i in range(1, degree + 1):
        b7 = np.column_stack((b7, b5 ** i))
    return b7
def fonk2(b5, b6, degree):
    b7 = fonk1(b5, degree)
    b8 = np.linalg.solve(b7.T.dot(b7), b7.T.dot(b6))
    return b8
def fonk3(parameters, b7, b6):
    b9 = b7.dot(parameters)
    b10 = np.sqrt(((b9 - b6) ** 2).mean())
    return b10
def fonk4():
    x_train, x_test, y_train, b11 = train_test_split(b5, b6, test_size=0.30, shuffle=True)
    for b16 in b2[1:]:
        b12 = fonk1(x_train, b16)
        b13 = fonk1(x_test, b16)
        b8 = fonk2(x_train, y_train, b16)
        b3.append(fonk3(b8, b12, y_train))
        b4.append(fonk3(b8, b13, b11))
    plt.figure()
    plt.semilogy(b2[1:], b3, b14 = 'Train')
    plt.semilogy(b2[1:], b4, b14 = 'Test')
    plt.xlabel('Degree of Polynomial')
    plt.ylabel('RMSE')
    plt.title('RMSE for Training and Testing Data')
    plt.legend(b15 = 'upper left')
    plt.show()
def fonk5():
    plt.figure()
    for b16 in b2:
        if b16 = = 0:
            plt.plot([-5, 5], [b6.mean(), b6.mean()], b14 = 'Mean')
        else:
            b8 = fonk2(b5, b6, b16)
            b17 = fonk1(b5, b16)
            b18 = b17.dot(b8)
            print(f'Degree {b16}: {b8}')
            plt.plot(b5, b18, b14 = f'Degree {b16}')
    plt.xlim((-6, 6))
    plt.xlabel('b7')
    plt.ylabel('Y')
    plt.title('Polynomial Regression Fits')
    plt.legend(b15 = 'lower right')
    plt.show()
    fonk4()
if b19 = = '__main__':
    fonk5()