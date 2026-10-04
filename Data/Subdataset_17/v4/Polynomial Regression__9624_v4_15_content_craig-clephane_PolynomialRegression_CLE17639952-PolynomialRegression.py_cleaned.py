import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv('CMP3751M_ML_Assignment 1_Task1_pol_regression.csv')
degrees = [0, 1, 2, 3, 5, 10]
RMSETrain = []
RMSETest = []
x = np.sort(data['x'].values)
y = np.sort(data['y'].values)
plt.figure()
plt.plot(x, y, 'bo')
plt.xlabel('X')
plt.ylabel('Y')
def DesignMatrix(x, degree):
    X = np.ones(x.shape)
    for i in range(1, degree + 1):
        X = np.column_stack((X, x ** i))
    return X
def polynomial_regression(x, y, degree):
    X = DesignMatrix(x, degree)
    XX = X.T.dot(X)
    w = np.linalg.solve(XX, X.T.dot(y))
    return w
def eval_polynomial_regression(parameters, x, y):
    predictions = x.dot(parameters)
    rmse = np.sqrt(((predictions - y) ** 2).mean())
    return rmse
def evaluation():
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.30, shuffle=True)
    for d in degrees[1:]:
        x_train = DesignMatrix(xtrain, d)
        x_test = DesignMatrix(xtest, d)
        w = polynomial_regression(xtrain, ytrain, d)
        RMSETrain.append(eval_polynomial_regression(w, x_train, ytrain))
        RMSETest.append(eval_polynomial_regression(w, x_test, ytest))
    plt.semilogy(degrees[1:], RMSETrain, label='Train')
    plt.semilogy(degrees[1:], RMSETest, label='Test')
    plt.legend(loc='upper left')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('RMSE')
    plt.title('RMSE vs Polynomial Degree')
    plt.show()
def main():
    for d in degrees:
        if d == 0:
            plt.plot([-5, 5], [y.mean(), y.mean()], label='Mean')
        else:
            w = polynomial_regression(x, y, d)
            X = DesignMatrix(x, d)
            predictions = X.dot(w)
            print(f'Degree: {d}, Weights: {w}')
            plt.plot(x, predictions, label=f'Degree {d}')
    plt.xlim((-6, 6))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc='lower right')
    plt.title('Polynomial Regression Fits')
    plt.show()
    evaluation()
main()