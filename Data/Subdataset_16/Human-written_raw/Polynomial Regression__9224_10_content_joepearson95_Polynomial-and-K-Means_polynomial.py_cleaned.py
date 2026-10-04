
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('CMP3751M_ML_Assignment 1_Task1 - dataset - pol_regression.csv')
b2 = b1['b2'].values
b3 = b1['b3'].values
def fonk1(b2, degree):
    b4 = np.ones(b2.shape)
    for i in range(1, degree + 1):
        b4 = np.column_stack((b4, b2 ** i))
    return b4
def fonk2(features_train,y_train,degree):
    b4 = fonk1(features_train, degree)
    b5 = b4.transpose().dot(b4)
    b6 = np.linalg.solve(b5, b4.transpose().dot(y_train))
    return b6
def fonk3(b4,Y,train_split):
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    for position in range(len(b4)):
        if position >= len(b4)*train_split:
            b8.append(b4[position])
            b10.append(Y[position])
        else:
            b7.append(b4[position])
            b9.append(Y[position])
    return b7, b8, b9, b10
def fonk4(b2, b3, degree):
    b7, b8, b9, b10 = fonk3(b2,b3,0.7)
    b11 = np.zeros((degree, 1))
    b12 = np.zeros((degree,1))
    for i in range(1, degree +1):
        b13 = fonk1(np.asarray(b7), i)
        b14 = fonk1(np.asarray(b8), i)
        b15 = fonk2(np.asarray(b7),np.asarray(b9), i)
        b11[i - 1] = np.sqrt((b13.dot(b15) - np.asarray(b9))**2).mean()
        b12[i - 1] = np.sqrt((b14.dot(b15) - np.asarray(b10))**2).mean()
    plt.figure();
    plt.title(str(degree) + ' Degree')
    plt.semilogy(range(1,len(b11) + 1), b11)
    plt.semilogy(range(1,len(b12) + 1), b12)
    return b11, b12
def fonk5(b2,b21,b3,b16, b20):
    if b16 = = 0:
        b17 = np.mean(b3)
    else:
        b17 = fonk2(b2,b3,b16)
    b18 = fonk1(b21, b16)
    b19 = b18.dot(b17)
    plt.figure()
    plt.plot(b2,b3, 'bo')
    plt.plot(b21, b19,b20 = b20)
    plt.title(str(b16) + ' Degrees')
    plt.xlabel("Range of Polynomials")
    plt.ylabel("Points of Polynomial")
    plt.ylabel("Points of Polynomial")
    plt.show()
def fonk6(b2,b3,degree):
    b11, b12 = fonk4(b2,b3,degree)
    plt.figure();
    plt.semilogy(range(1,len(b11) + 1), b11)
    plt.semilogy(range(1,len(b12) + 1), b12)
    plt.title((str(degree) + ' Degrees'))
    plt.xlabel("Degree of RMSE")
    plt.ylabel("Points of RSME")
    plt.legend(('RMSE on training set', 'RMSE on test set'))
    plt.show()
b21 = np.linspace(-5,5,len(b2))
b22 = np.linspace(-5,5,len(b2))
for i in range(0,4):
    fonk5(b2,b21,b3,i, 'r')
fonk5(b2,b21,b3,5, 'r')
fonk5(b2,b21,b3,10, 'r')
for i in range(0,4):
    fonk4(b2,b3, i)
fonk4(b2,b3,5)
fonk4(b2,b3,10)