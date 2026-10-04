import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def gradient_descent(X, y, theta, learning_rate, iterations):
    temp = np.matrix(np.zeros(theta.shape))
    num_parameters = theta.shape[1]
    cost_history = np.zeros(iterations)
    for i in range(iterations):
        error = (X * theta.T) - y
        for j in range(num_parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((learning_rate / len(X)) * np.sum(term))
        theta = temp
        cost_history[i] = compute_cost(X, y, theta)
    return theta, cost_history
def compute_cost(X, y, theta):
    squared_errors = np.power(((X * theta.T) - y), 2)
    return np.sum(squared_errors) / (2 * len(X))
def plot_data(data):
    data.plot(kind='scatter', x='x1', y='x2', figsize=(8, 3))
    plt.show()
def prepare_data(data):
    x = data['x1'].values
    x_ones = np.ones(len(x))
    x_square = np.power(x, 2)
    X = np.vstack([x_ones, x, x_square]).T
    y = data['x2'].values.reshape(-1, 1)
    return np.matrix(X), np.matrix(y)
def plot_results(data, theta):
    x_plot = np.linspace(data['x1'].min(), data['x1'].max(), 150)
    f = theta[0, 0] + (theta[0, 1] * x_plot) + (theta[0, 2] * np.power(x_plot, 2))
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x_plot, f, 'g', label='Prediction line')
    ax.scatter(data['x1'], data['x2'], label='Dataset')
    ax.legend(loc=2)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    plt.show()
data = pd.read_csv('Data_poly.csv', header=None, names=['x1', 'x2'])
print(data.head())
print(data.describe())
plot_data(data)
X, y = prepare_data(data)
learning_rate = 1e-10
iterations = 6000
initial_theta = np.matrix(np.array([0, 0, 0]))
initial_cost = compute_cost(X, y, initial_theta)
print(f"Initial Cost: {initial_cost}")
theta, cost_history = gradient_descent(X, y, initial_theta, learning_rate, iterations)
final_cost = compute_cost(X, y, theta)
print(f"Final Cost: {final_cost}")
plot_results(data, theta)