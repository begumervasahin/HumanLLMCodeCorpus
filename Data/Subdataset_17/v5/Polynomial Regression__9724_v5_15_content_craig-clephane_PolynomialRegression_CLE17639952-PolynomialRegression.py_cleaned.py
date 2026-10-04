import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv('CMP3751M_ML_Assignment 1_Task1_pol_regression.csv')
degrees = [0, 1, 2, 3, 5, 10]
rmse_train = []
rmse_test = []
x = np.sort(data['x'].values)
y = np.sort(data['y'].values)
plt.figure()
plt.plot(x, y, 'bo')
plt.xlabel('X')
plt.ylabel('Y')
def design_matrix(x, degree):
    X = np.ones(x.shape)
    for i in range(1, degree + 1):
        X = np.column_stack((X, x ** i))
    return X
def polynomial_regression(x, y, degree):
    X = design_matrix(x, degree)
    XX = X.T.dot(X)
    w = np.linalg.solve(XX, X.T.dot(y))
    return w
def evaluate_polynomial_regression(parameters, x, y):
    predictions = x.dot(parameters)
    rmse = np.sqrt(((predictions - y) ** 2).mean())
    return rmse
def evaluate():
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, shuffle=True)
    for degree in degrees[1:]:
        X_train = design_matrix(x_train, degree)
        X_test = design_matrix(x_test, degree)
        w = polynomial_regression(x_train, y_train, degree)
        rmse_train.append(evaluate_polynomial_regression(w, X_train, y_train))
        rmse_test.append(evaluate_polynomial_regression(w, X_test, y_test))
    plt.semilogy(degrees[1:], rmse_train, label='Train')
    plt.semilogy(degrees[1:], rmse_test, label='Test')
    plt.legend(loc='upper left')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('RMSE')
    plt.title('RMSE vs Polynomial Degree')
    plt.show()
def main():
    for degree in degrees:
        if degree == 0:
            plt.plot([-5, 5], [y.mean(), y.mean()], label='Mean')
        else:
            w = polynomial_regression(x, y, degree)
            X = design_matrix(x, degree)
            predictions = X.dot(w)
            print(f'Degree: {degree}, Weights: {w}')
            plt.plot(x, predictions, label=f'Degree {degree}')
    plt.xlim((-6, 6))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc='lower right')
    plt.title('Polynomial Regression Fits')
    plt.show()
    evaluate()
main()