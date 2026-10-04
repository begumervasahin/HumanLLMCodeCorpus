import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def compute_cost(X, y, theta):
    squared_errors = np.power(((X * theta.T) - y), 2)
    return np.sum(squared_errors) / (2 * len(X))
def gradient_descent(X, y, theta, learning_rate, iterations):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iterations)
    for i in range(iterations):
        error = (X * theta.T) - y
        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((learning_rate / len(X)) * np.sum(term))
        theta = temp
        cost[i] = compute_cost(X, y, theta)
    return theta, cost
learning_rate = 1e-10
iterations = 6000
data = pd.read_csv('Data_poly.csv', header=None, names=['x1', 'x2'])
print(data.head())
print(data.describe())
x = np.array(data.x1, dtype=np.float64)
y = np.array(data.x2, dtype=np.float64)
data.plot(kind='scatter', x='x1', y='x2', figsize=(8, 3))
x_ones = np.ones(len(x))
x_square = np.power(x, 2)
X = np.column_stack((x_ones, x, x_square))
X = np.matrix(X)
y = np.matrix(y).T
theta = np.matrix(np.array([0, 0, 0]))
print(f"Shape of X: {X.shape}")
print(f"Shape of theta: {theta.shape}")
print(f"Shape of y: {y.shape}")
initial_cost = compute_cost(X, y, theta)
print(f"Initial Cost: {initial_cost}")
theta, cost = gradient_descent(X, y, theta, learning_rate, iterations)
final_cost = compute_cost(X, y, theta)
print(f"Final Cost: {final_cost}")
x_pred = np.linspace(data.x1.min(), data.x1.max(), 150)
f = theta[0, 0] + (theta[0, 1] * x_pred) + (theta[0, 2] * np.power(x_pred, 2))
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(x_pred, f, 'g', label='Prediction Line')
ax.scatter(data.x1, data.x2, label='Dataset')
ax.legend(loc=2)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
plt.show()