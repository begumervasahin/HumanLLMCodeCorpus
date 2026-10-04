import numpy as np
import matplotlib.pyplot as plt
x = np.array([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]])
y_train = np.array([[1], [6], [63], [364], [1365], [3906], [9331], [19608], [37449], [66430], [111111], [177156], [271453], [402234], [579195], [813616], [1118481], [1508598], [2000719], [2613660], [3368421]])
def polynomial_regression(x, y, degree, learning_rate, epochs):
    x_train = np.hstack([np.power(x, i) for i in range(1, degree + 1)])
    theta = np.zeros((1, degree))
    n = len(y)
    for i in range(epochs):
        y_pred = x_train @ theta.T
        error = (1 / (2 * n)) * np.sum(np.square(y_pred - y))
        if i == 0:
            print(f'Initial error: {error}')
        elif i == (epochs - 1):
            print(f'Final error  : {error}')
        theta -= (1/n) * learning_rate * np.sum((y_pred - y) * x_train, axis=0)
    return theta, x_train, y_pred
def plot_regression(x, y, y_pred, title):
    plt.scatter(x, y, label='Actual')
    plt.plot(x, y_pred, 'r', label='Predicted')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
print('y = w1 * x + w2 * (x ^ 2)')
theta, x_train, y_pred = polynomial_regression(x, y_train, degree=2, learning_rate=0.00005, epochs=10000)
plot_regression(x_train[:, 0], y_train, y_pred, 'Training for y = w1 * x + w2 * (x ^ 2)')
print('---------------------------------------------')
print('y = w1 * x + w2 * (x ^ 2) + w3 * (x ^ 3)')
theta, x_train, y_pred = polynomial_regression(x, y_train, degree=3, learning_rate=0.0000001, epochs=10000)
plot_regression(x_train[:, 0], y_train, y_pred, 'Training for y = w1 * x + w2 * (x ^ 2) + w3 * (x ^ 3)')
print('---------------------------------------------')
print('y = w1 * x + w2 * (x ^ 2) + w3 * (x ^ 3) + w4 * (x ^ 4)')
theta, x_train, y_pred = polynomial_regression(x, y_train, degree=4, learning_rate=0.0000000005, epochs=10000)
plot_regression(x_train[:, 0], y_train, y_pred, 'Training for y = w1 * x + w2 * (x ^ 2) + w3 * (x ^ 3) + w4 * (x ^ 4)')
print('---------------------------------------------')