import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('CMP3751M_ML_Assignment 1_Task1 - dataset - pol_regression.csv')
x = data['x'].values
y = data['y'].values
def get_polynomial_data_matrix(x, degree):
    X = np.ones((x.shape[0], degree + 1))
    for i in range(1, degree + 1):
        X[:, i] = x ** i
    return X
def polynomial_regression(features_train, y_train, degree):
    X = get_polynomial_data_matrix(features_train, degree)
    w = np.linalg.solve(X.T.dot(X), X.T.dot(y_train))
    return w
def train_test_split(X, Y, train_split=0.7):
    split_index = int(len(X) * train_split)
    X_train, X_test = X[:split_index], X[split_index:]
    Y_train, Y_test = Y[:split_index], Y[split_index:]
    return X_train, X_test, Y_train, Y_test
def eval_polynomial_regression(x, y, max_degree):
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, 0.7)
    RMSE_train = []
    RMSE_test = []
    for degree in range(1, max_degree + 1):
        X_train_poly = get_polynomial_data_matrix(X_train, degree)
        X_test_poly = get_polynomial_data_matrix(X_test, degree)
        params = polynomial_regression(X_train, Y_train, degree)
        train_predictions = X_train_poly.dot(params)
        test_predictions = X_test_poly.dot(params)
        RMSE_train.append(np.sqrt(np.mean((train_predictions - Y_train) ** 2)))
        RMSE_test.append(np.sqrt(np.mean((test_predictions - Y_test) ** 2)))
    plt.figure()
    plt.semilogy(range(1, max_degree + 1), RMSE_train, label='RMSE Train')
    plt.semilogy(range(1, max_degree + 1), RMSE_test, label='RMSE Test')
    plt.title(f'{max_degree} Degree Polynomial Regression')
    plt.xlabel("Degree of Polynomial")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()
    return RMSE_train, RMSE_test
def plot_graph(x, x_test, y, degree, color):
    if degree == 0:
        y_pred = np.mean(y) * np.ones_like(x_test)
    else:
        params = polynomial_regression(x, y, degree)
        X_test_poly = get_polynomial_data_matrix(x_test, degree)
        y_pred = X_test_poly.dot(params)
    plt.figure()
    plt.plot(x, y, 'bo', label='Data Points')
    plt.plot(x_test, y_pred, color=color, label=f'{degree} Degrees')
    plt.xlabel("Input Feature")
    plt.ylabel("Target Value")
    plt.legend()
    plt.show()
def plot_evaluation(x, y, max_degree):
    RMSE_train, RMSE_test = eval_polynomial_regression(x, y, max_degree)
    plt.figure()
    plt.semilogy(range(1, max_degree + 1), RMSE_train, label='RMSE Train')
    plt.semilogy(range(1, max_degree + 1), RMSE_test, label='RMSE Test')
    plt.title(f'{max_degree} Degrees Polynomial Regression Evaluation')
    plt.xlabel("Degree of Polynomial")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()
x_test = np.linspace(min(x), max(x), len(x))
for i in range(4):
    plot_graph(x, x_test, y, i, 'r')
plot_graph(x, x_test, y, 5, 'r')
plot_graph(x, x_test, y, 10, 'r')
for i in range(4):
    eval_polynomial_regression(x, y, i)
eval_polynomial_regression(x, y, 5)
eval_polynomial_regression(x, y, 10)