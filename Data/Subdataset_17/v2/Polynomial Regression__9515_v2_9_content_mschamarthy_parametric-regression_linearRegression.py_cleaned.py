import numpy as np
import matplotlib.pyplot as plt
d1 = np.loadtxt('data/svar-set1.dat.txt')
d2 = np.loadtxt('data/svar-set2.dat.txt')
d3 = np.loadtxt('data/svar-set3.dat.txt')
d4 = np.loadtxt('data/svar-set4.dat.txt')
def linear_regression_train(z, y):
    theta = np.linalg.pinv(z).dot(y)
    return theta
def linear_regression_fit(z, y):
    theta = linear_regression_train(z, y)
    y_fit = z.dot(theta)
    return y_fit, theta
def linear_regression_predict(theta, xIn):
    z = np.ones(shape=(1, xIn.size + 1))
    z[0, 1:] = xIn
    y_predict = z.dot(theta)
    return y_predict
def single_linear_regression(x):
    m, n = x.shape
    z = np.ones(shape=(m, n + 1))
    z[:, 1:] = x
    return z
def single_polynomial_regression(x, order):
    m, n = x.shape
    z = np.ones(shape=(m, n + order))
    for i in range(1, order + 1):
        z[:, n + i - 1] = np.power(x[:, 0], i)
    return z
def average_sum_of_squared_errors(y_fit, y):
    error = np.array(y_fit - y).T.dot(y_fit - y) / y.shape[0]
    return error
def data_split(x, n):
    row, col = x.shape
    split_size = row
    y = np.ndarray(shape=(n, split_size, col))
    for i in range(n):
        y[i] = x[i * split_size: (i + 1) * split_size, :]
    return y
def data_combine_except(x, i):
    splits, row, col = x.shape
    training = np.ndarray(shape=((splits - 1) * row, col))
    testing = x[i]
    j = 0
    for k in range(splits):
        if k == i:
            continue
        training[j * row: (j + 1) * row] = x[k]
        j += 1
    print(f"Training shape: {training.shape}")
    print(f"Testing shape: {testing.shape}")
    return training, testing
def single_linear_expt(data):
    row, col = data.shape
    X = data[:, :col - 1]
    y = data[:, col - 1:]
    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)
    Z = single_linear_regression(X)
    Y_fit, theta = linear_regression_fit(Z, y)
    Z_quad = single_polynomial_regression(X, 2)
    Y_fit_quad, theta_quad = linear_regression_fit(Z_quad, y)
    Z_third = single_polynomial_regression(X, 3)
    Y_fit_third, theta_third = linear_regression_fit(Z_third, y)
    print("Average SSE for linear:", average_sum_of_squared_errors(Y_fit, y),
          " Polynomial of degree 2:", average_sum_of_squared_errors(Y_fit_quad, y),
          " Polynomial of degree 3:", average_sum_of_squared_errors(Y_fit_third, y))
    plt.plot(X, y, 'r+', label='Data')
    plt.plot(X, Y_fit, '.', label='Linear Fit')
    plt.plot(X, Y_fit_quad, 'r.', label='Quadratic Fit')
    plt.plot(X, Y_fit_third, 'g.', label='Cubic Fit')
    plt.legend()
    plt.show()
single_linear_expt(d1)
single_linear_expt(d2)
single_linear_expt(d3)
single_linear_expt(d4)
X = data_split(d1, 10)
data_combine_except(X, 1)