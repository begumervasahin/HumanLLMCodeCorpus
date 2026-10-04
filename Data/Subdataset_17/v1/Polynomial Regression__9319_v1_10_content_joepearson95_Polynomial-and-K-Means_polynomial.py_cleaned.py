import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
my_data = pd.read_csv('CMP3751M_ML_Assignment 1_Task1 - dataset - pol_regression.csv')
x = my_data['x'].values
y = my_data['y'].values
def get_polynomial_data_matrix(x, degree):
    X = np.ones(x.shape)
    for i in range(1, degree + 1):
        X = np.column_stack((X, x ** i))
    return X
def polynomial_regression(features_train, y_train, degree):
    X = get_polynomial_data_matrix(features_train, degree)
    XX = X.transpose().dot(X)
    w = np.linalg.solve(XX, X.transpose().dot(y_train))
    return w
def train_test_split(X, Y, train_split):
    X_train, X_test, Y_train, Y_test = [], [], [], []
    for position in range(len(X)):
        if position >= len(X) * train_split:
            X_test.append(X[position])
            Y_test.append(Y[position])
        else:
            X_train.append(X[position])
            Y_train.append(Y[position])
    return np.array(X_train), np.array(X_test), np.array(Y_train), np.array(Y_test)
def eval_polynomial_regression(x, y, degree):
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, 0.7)
    RMSE_train = np.zeros(degree)
    RMSE_test = np.zeros(degree)
    for i in range(1, degree + 1):
        X_train_poly = get_polynomial_data_matrix(X_train, i)
        X_test_poly = get_polynomial_data_matrix(X_test, i)
        params = polynomial_regression(X_train, Y_train, i)
        RMSE_train[i - 1] = np.sqrt(((X_train_poly.dot(params) - Y_train) ** 2).mean())
        RMSE_test[i - 1] = np.sqrt(((X_test_poly.dot(params) - Y_test) ** 2).mean())
    plt.figure()
    plt.title(f'{degree} Degree')
    plt.semilogy(range(1, degree + 1), RMSE_train, label='RMSE Train')
    plt.semilogy(range(1, degree + 1), RMSE_test, label='RMSE Test')
    plt.legend()
    plt.show()
    return RMSE_train, RMSE_test
def plot_graph(x, x_test, y, degree, color):
    if degree == 0:
        w1 = np.mean(y)
    else:
        w1 = polynomial_regression(x, y, degree)
    X_test_poly = get_polynomial_data_matrix(x_test, degree)
    y_test_pred = X_test_poly.dot(w1)
    plt.figure()
    plt.plot(x, y, 'bo', label='Data Points')
    plt.plot(x_test, y_test_pred, color=color, label=f'{degree} Degrees')
    plt.xlabel("Range of Polynomials")
    plt.ylabel("Points of Polynomial")
    plt.legend()
    plt.show()
def plot_evaluation(x, y, degree):
    RMSE_train, RMSE_test = eval_polynomial_regression(x, y, degree)
    plt.figure()
    plt.semilogy(range(1, degree + 1), RMSE_train, label='RMSE Train')
    plt.semilogy(range(1, degree + 1), RMSE_test, label='RMSE Test')
    plt.title(f'{degree} Degrees')
    plt.xlabel("Degree of RMSE")
    plt.ylabel("Points of RMSE")
    plt.legend()
    plt.show()
x_test = np.linspace(-5, 5, len(x))
y_test = np.linspace(-5, 5, len(x))
for i in range(4):
    plot_graph(x, x_test, y, i, 'r')
plot_graph(x, x_test, y, 5, 'r')
plot_graph(x, x_test, y, 10, 'r')
for i in range(4):
    eval_polynomial_regression(x, y, i)
eval_polynomial_regression(x, y, 5)
eval_polynomial_regression(x, y, 10)