import numpy as np
import matplotlib.pyplot as plt
x = np.array([[i] for i in range(21)])
y_train = np.array([
    [1], [6], [63], [364], [1365], [3906], [9331], [19608], [37449], [66430],
    [111111], [177156], [271453], [402234], [579195], [813616], [1118481],
    [1508598], [2000719], [2613660], [3368421]
])
def train_and_plot_polynomial_model(x, y, degree, learning_rate, epochs):
    x_train = x
    for d in range(2, degree + 1):
        x_train = np.append(x_train, np.power(x, d), axis=1)
    print(f'Training for y = {" + ".join([f"w{d} * (x ^ {d})" for d in range(1, degree + 1)])}')
    print(f'Training with {len(x_train)} tuples')
    n = len(y)
    theta = np.zeros((1, degree))
    for i in range(epochs):
        y_pred = x_train @ theta.T
        error = (1 / n) * np.sum(np.square(y_pred - y))
        if i == 0:
            print(f'Initial error: {error}')
        elif i == (epochs - 1):
            print(f'Final error  : {error}')
        theta -= (1 / n) * learning_rate * np.sum((y_pred - y) * x_train, axis=0)
    plt.scatter(x[:, 0], y, label='Actual data')
    plt.plot(x[:, 0], y_pred, 'r', label='Fitted line')
    plt.title(f'Training for polynomial degree {degree}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
train_and_plot_polynomial_model(x, y_train, degree=2, learning_rate=0.00005, epochs=10000)
print('---------------------------------------------')
train_and_plot_polynomial_model(x, y_train, degree=3, learning_rate=0.0000001, epochs=10000)
print('---------------------------------------------')
train_and_plot_polynomial_model(x, y_train, degree=4, learning_rate=0.0000000005, epochs=10000)
print('---------------------------------------------')