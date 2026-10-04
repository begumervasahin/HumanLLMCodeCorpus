import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from sklearn.model_selection import train_test_split
import numpy.linalg as linalg
data = 'CMP3751M_ML_Assignment 1_Task1_pol_regression.csv'
data = pd.read_csv(data)
degrees = [0, 1, 2, 3, 5, 10]
RMSETrain = []
RMSETest = []
x = data['x']
y = data['y']
x = np.sort(x, axis=0)
y = np.sort(y, axis=0)
plt.figure()
plt.plot(x, y, 'bo')
plt.xlabel('X')
plt.ylabel('Y')
def Designmatrix(x, degree):
    X = np.ones(x.shape)
    for i in range(1,degree + 1):
        X = np.column_stack((X, x ** i))
    return X
def pol_regression(x, y, degree):
    X = Designmatrix(x, degree)
    XX = X.transpose().dot(X)
    print(XX)
    w = np.linalg.solve(XX, X.transpose().dot(y))
    return w
def eval_pol_regression(parameters, x, y):
    rmse = np.sqrt(((x.dot(parameters) - y) ** 2).mean())
    return rmse
def evaluation():
    index = 0
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.30, shuffle=True)
    for d in degrees[1:]:
        x_train = Designmatrix(xtrain ,d)
        x_test = Designmatrix(xtest ,d)
        w = pol_regression(xtrain, ytrain, d)
        RMSETrain.append( eval_pol_regression(w, x_train, ytrain) )
        RMSETest.append( eval_pol_regression(w, x_test, ytest) )
        index+=1
    plt.semilogy(degrees[1:], RMSETrain)
    plt.semilogy(degrees[1:], RMSETest)
    plt.legend(('Train','Test'), loc = 'upper left')
    plt.show()
def main():
    for d in degrees:
        if d is 0: plt.plot([-5, 5],[y.mean(), y.mean()])
        else:
            w = pol_regression(x, y, d)
            X = Designmatrix(x ,d)
            X = X.dot(w)
            print('Degree : ' + str(d) + ' : ' + str(w))
            plt.plot(x, X)
    plt.xlim((-6, 6))
    plt.legend(('ground truth', '$x$', '$x^2$', '$x^3$', '$x^5$', '$x^10$'), loc = 'lower right')
    plt.show()
    evaluation()
main()