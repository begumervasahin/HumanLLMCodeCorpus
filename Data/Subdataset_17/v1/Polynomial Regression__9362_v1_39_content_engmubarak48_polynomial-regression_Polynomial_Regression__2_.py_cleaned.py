import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def Gradient_Descent(X, y, desired_output, learning_rate, iters):
    temp = np.matrix(np.zeros(desired_output.shape))
    parameters = int(desired_output.ravel().shape[1])
    cost = np.zeros(iters)
    for i in range(iters):
        error = (X * desired_output.T) - y
        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = desired_output[0, j] - ((learning_rate / len(X)) * np.sum(term))
        desired_output = temp
        cost[i] = Cost(X, y, desired_output)
    return desired_output, cost
def Cost(X, y, desired_output):
    inner = np.power(((X * desired_output.T) - y), 2)
    return np.sum(inner) / (2 * len(X))
data = pd.read_csv('Data_poly.csv', header=None, names=['x1', 'x2'])
print(data.head())
print(data.describe())
x = np.array(data.x1, dtype=np.float64)
y = np.array(data.x2, dtype=np.float64)
data.plot(kind='scatter', x='x1', y='x2', figsize=(8, 3))
plt.show()
x_ones = np.ones(len(x))
x_square = np.power(x, 2)
Xs = [x_ones, x, x_square]
X = np.transpose(Xs)
y = data.iloc[:, 1:2]
y = np.matrix(y.values)
desired_output = np.matrix(np.array([0, 0, 0]))
learning_rate = 0.0000000001
iteration = 6000
initial_cost = Cost(X, y, desired_output)
print(f"Initial Cost: {initial_cost}")
g, cost = Gradient_Descent(X, y, desired_output, learning_rate, iteration)
final_cost = Cost(X, y, g)
print(f"Final Cost: {final_cost}")
x = np.linspace(data.x1.min(), data.x1.max(), 150)
f = g[0, 0] + (g[0, 1] * x) + (g[0, 2] * np.power(x, 2))
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(x, f, 'g', label='Prediction line')
ax.scatter(data.x1, data.x2, label='Dataset')
ax.legend(loc=2)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
plt.show()