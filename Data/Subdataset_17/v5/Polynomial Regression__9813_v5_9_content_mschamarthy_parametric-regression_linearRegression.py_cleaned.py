import numpy as np
import matplotlib.pyplot as plt
datasets = [
    np.loadtxt('data/svar-set1.dat.txt'),
    np.loadtxt('data/svar-set2.dat.txt'),
    np.loadtxt('data/svar-set3.dat.txt'),
    np.loadtxt('data/svar-set4.dat.txt')
]
def linear_regression_train(z, y):
    return np.linalg.pinv(z).dot(y)
def linear_regression_fit(z, y):
    theta = linear_regression_train(z, y)
    y_fit = z.dot(theta)
    return y_fit, theta
def linear_regression_predict(theta, xIn):
    z = np.ones((1, xIn.size + 1))
    z[0, 1:] = xIn
    return z.dot(theta)
def design_matrix_linear(x):
    m, n = x.shape
    z = np.ones((m, n + 1))
    z[:, 1:] = x
    return z
def design_matrix_polynomial(x, order):
    m, n = x.shape
    z = np.ones((m, n + order))
    for i in range(1, order + 1):
        z[:, n + i - 1] = np.power(x[:, 0], i)
    return z
def average_sum_of_squared_errors(y_fit, y):
    m = y.shape[0]
    error = np.dot((y_fit - y).T, (y_fit - y)) / m
    return error
def data_split(x, n):
    row, col = x.shape
    split_size = row
    splits = np.ndarray((n, split_size, col))
    for i in range(n):
        splits[i, :, :] = x[i * split_size: (i + 1) * split_size, :]
    return splits
def data_combine_except(splits, exclude_index):
    splits_count, row, col = splits.shape
    training_data = np.ndarray(((splits_count - 1) * row, col))
    testing_data = splits[exclude_index, :, :]
    j = 0
    for k in range(splits_count):
        if k == exclude_index:
            continue
        training_data[j * row: (j + 1) * row, :] = splits[k, :, :]
        j += 1
    print("training:", training_data.shape)
    print("testing:", testing_data.shape)
    return training_data, testing_data
def single_linear_expt(data):
    row, col = data.shape
    X = data[:, :col - 1]
    y = data[:, col - 1:].reshape(-1, 1)
    X = X.reshape(-1, 1)
    Z_linear = design_matrix_linear(X)
    Y_fit_linear, theta_linear = linear_regression_fit(Z_linear, y)
    Z_quad = design_matrix_polynomial(X, 2)
    Y_fit_quad, theta_quad = linear_regression_fit(Z_quad, y)
    Z_cubic = design_matrix_polynomial(X, 3)
    Y_fit_cubic, theta_cubic = linear_regression_fit(Z_cubic, y)
    print("Average SSE for linear:", average_sum_of_squared_errors(Y_fit_linear, y),
          " Polynomial of degree 2:", average_sum_of_squared_errors(Y_fit_quad, y),
          " Polynomial of degree 3:", average_sum_of_squared_errors(Y_fit_cubic, y))
    plt.plot(X, y, 'r+', label='Data')
    plt.plot(X, Y_fit_linear, 'b.', label='Linear fit')
    plt.plot(X, Y_fit_quad, 'r.', label='Quadratic fit')
    plt.plot(X, Y_fit_cubic, 'g.', label='Cubic fit')
    plt.legend()
    plt.show()
for dataset in datasets:
    single_linear_expt(dataset)
X_splits = data_split(datasets[0], 10)
data_combine_except(X_splits, 1)