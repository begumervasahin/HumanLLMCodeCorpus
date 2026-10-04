import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
my_data = pd.read_csv('CMP3751M_ML_Assignment 1_Task1 - dataset - pol_regression.csv')
x = my_data['x'].values
y = my_data['y'].values
def get_polynomial_data_matrix(x, degree):
    X = np.ones((x.shape[0], degree + 1))
    for i in range(1, degree + 1):
        X[:, i] = x ** i
    return X
def polynomial_regression(features_train, y_train, degree):
    X = get_polynomial_data_matrix(features_train, degree)
    XX = X.T.dot(X)
    w = np.linalg.solve(XX, X.T.dot(y_train))
    return w
def train_test_split(X, Y, train_split):
    split_idx = int(len(X) * train_split)
    return X[:split_idx], X[split_idx:], Y[:split_idx], Y[split_idx:]
def eval_polynomial_regression(x, y, degree):
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, 0.7)
    RMSE_train = np.zeros(degree)
    RMSE_test = np.zeros(degree)
    for i in range(1, degree + 1):
        X_train_poly = get_polynomial_data_matrix(np.asarray(X_train), i)
        X_test_poly = get_polynomial_data_matrix(np.asarray(X_test), i)
        params = polynomial_regression(np.asarray(X_train), np.asarray(Y_train), i)
        RMSE_train[i - 1] = np.sqrt(((X_train_poly.dot(params) - np.asarray(Y_train)) ** 2).mean())
        RMSE_test[i - 1] = np.sqrt(((X_test_poly.dot(params) - np.asarray(Y_test)) ** 2).mean())
    plt.figure()
    plt.title(f'{degree} Degree Polynomial Regression')
    plt.semilogy(range(1, degree + 1), RMSE_train, label='Training RMSE')
    plt.semilogy(range(1, degree + 1), RMSE_test, label='Test RMSE')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('RMSE')
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
    plt.plot(x_test, y_test_pred, color=color, label=f'{degree} Degree Polynomial')
    plt.title(f'{degree} Degrees')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
def plot_evaluation(x, y, degree):
    RMSE_train, RMSE_test = eval_polynomial_regression(x, y, degree)
    plt.figure()
    plt.semilogy(range(1, degree + 1), RMSE_train, label='Training RMSE')
    plt.semilogy(range(1, degree + 1), RMSE_test, label='Test RMSE')
    plt.title(f'{degree} Degree Polynomial Regression Evaluation')
    plt.xlabel('Polynomial Degree')
    plt.ylabel('RMSE')
    plt.legend()
    plt.show()
x_test = np.linspace(-5, 5, len(x))
y_test = np.linspace(-5, 5, len(x))
for i in range(0, 5):
    plot_graph(x, x_test, y, i, 'r')
plot_graph(x, x_test, y, 5, 'r')
plot_graph(x, x_test, y, 10, 'r')
for i in range(0, 5):
    eval_polynomial_regression(x, y, i)
eval_polynomial_regression(x, y, 5)
eval_polynomial_regression(x, y, 10)