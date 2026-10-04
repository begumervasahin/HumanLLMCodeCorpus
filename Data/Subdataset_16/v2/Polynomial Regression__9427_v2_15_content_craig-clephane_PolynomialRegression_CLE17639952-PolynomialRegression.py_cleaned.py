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
def fonk1(b5, degree):
    b7 = np.ones(b5.shape)
    for i in range(1, degree + 1):
        b7 = np.column_stack((b7, b5 ** i))
    return b7
def fonk2(b5, b6, degree):
    b7 = fonk1(b5, degree)
    b8 = b7.T.dot(b7)
    b9 = np.linalg.solve(b8, b7.T.dot(b6))
    return b9
def fonk3(parameters, b7, b6):
    b10 = b7.dot(parameters)
    b11 = np.sqrt(((b10 - b6) ** 2).mean())
    return b11
def fonk4():
    x_train, x_test, y_train, b12 = train_test_split(b5, b6, test_size=0.30, shuffle=True)
    for b17 in b2[1:]:
        b13 = fonk1(x_train, b17)
        b14 = fonk1(x_test, b17)
        b9 = fonk2(x_train, y_train, b17)
        b3.append(fonk3(b9, b13, y_train))
        b4.append(fonk3(b9, b14, b12))
    plt.figure()
    plt.semilogy(b2[1:], b3, b15 = 'Train')
    plt.semilogy(b2[1:], b4, b15 = 'Test')
    plt.xlabel('Degree of Polynomial')
    plt.ylabel('RMSE')
    plt.title('RMSE for Training and Testing Data')
    plt.legend(b16 = 'upper left')
    plt.show()
def fonk5():
    plt.figure()
    for b17 in b2:
        if b17 = = 0:
            plt.plot([-5, 5], [b6.mean(), b6.mean()], b15 = 'Mean')
        else:
            b9 = fonk2(b5, b6, b17)
            b18 = fonk1(b5, b17)
            b19 = b18.dot(b9)
            print(f'Degree {b17}: {b9}')
            plt.plot(b5, b19, b15 = f'Degree {b17}')
    plt.xlim((-6, 6))
    plt.xlabel('b7')
    plt.ylabel('Y')
    plt.title('Polynomial Regression Fits')
    plt.legend(b16 = 'lower right')
    plt.show()
    fonk4()
if b20 = = '__main__':
    fonk5()