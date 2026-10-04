import numpy as np
import matplotlib.pyplot as plt
x = np.array([[i] for i in range(21)])
y_train = np.array([
    [1], [6], [63], [364], [1365], [3906], [9331], [19608], [37449], [66430],
    [111111], [177156], [271453], [402234], [579195], [813616], [1118481],
    [1508598], [2000719], [2613660], [3368421]
])
def train_polynomial_model(x, y, degree, learning_rate, epochs):
    x_train = np.hstack([np.power(x, d) for d in range(1, degree + 1)])
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
    return y_pred, theta
def plot_model(x, y, y_pred, degree):
    plt.scatter(x[:, 0], y, label='Actual data')
    plt.plot(x[:, 0], y_pred, 'r', label='Fitted line')
    plt.title(f'Training for polynomial degree {degree}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
def main():
    degrees = [2, 3, 4]
    learning_rates = [0.00005, 0.0000001, 0.0000000005]
    epochs = 10000
    for degree, lr in zip(degrees, learning_rates):
        y_pred, theta = train_polynomial_model(x, y_train, degree, lr, epochs)
        plot_model(x, y_train, y_pred, degree)
        print('---------------------------------------------')
if __name__ == "__main__":
    main()