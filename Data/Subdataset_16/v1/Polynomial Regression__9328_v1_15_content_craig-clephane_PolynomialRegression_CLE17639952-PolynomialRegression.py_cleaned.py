import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
b1 = pd.read_csv('CMP3751M_ML_Assignment 1_Task1_pol_regression.csv')
b2 = [0, 1, 2, 3, 5, 10]
b3 = []
b4 = []
b5 = np.sort(b1['b5'].values, axis=0)
b6 = np.sort(b1['b6'].values, axis=0)
plt.figure()
plt.plot(b5, b6, 'bo')
plt.xlabel('b7')
plt.ylabel('Y')
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
def fonk3(parameters, b5, b6):
    b10 = np.sqrt(((b5.dot(parameters) - b6) ** 2).mean())
    return b10
def fonk4():
    a1 = 0
    xtrain, xtest, ytrain, b11 = train_test_split(b5, b6, test_size=0.30, shuffle=True)
    for b15 in b2[1:]:
        b12 = fonk1(xtrain, b15)
        b13 = fonk1(xtest, b15)
        b9 = fonk2(xtrain, ytrain, b15)
        b3.append(fonk3(b9, b12, ytrain))
        b4.append(fonk3(b9, b13, b11))
        a1 += 1
    plt.semilogy(b2[1:], b3)
    plt.semilogy(b2[1:], b4)
    plt.legend(('Train', 'Test'), b14 = 'upper left')
    plt.xlabel('Degree of polynomial')
    plt.ylabel('RMSE')
    plt.title('RMSE for Training and Testing Data')
    plt.show()
def fonk5():
    for b15 in b2:
        if b15 = = 0:
            plt.plot([-5, 5], [b6.mean(), b6.mean()])
        else:
            b9 = fonk2(b5, b6, b15)
            b7 = fonk1(b5, b15)
            b7 = b7.dot(b9)
            print(f'Degree: {b15} : {b9}')
            plt.plot(b5, b7)
    plt.xlim((-6, 6))
    plt.legend(('ground truth', '$b5$', '$b5^2$', '$b5^3$', '$b5^5$', '$b5^{10}$'), b14 = 'lower right')
    plt.xlabel('b7')
    plt.ylabel('Y')
    plt.title('Polynomial Regression Fits')
    plt.show()
    fonk4()
fonk5()