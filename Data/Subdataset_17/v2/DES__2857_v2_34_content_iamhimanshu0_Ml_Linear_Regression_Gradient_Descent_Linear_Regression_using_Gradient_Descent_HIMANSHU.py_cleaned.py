import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 5.0)
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Points')
xi = np.mean(X)
yi = np.mean(Y)
x_xi = X - xi
y_yi = Y - yi
m = np.sum(x_xi * y_yi) / np.sum(x_xi ** 2)
c = yi - m * xi
Y_pred_initial = m * X + c
plt.plot(X, Y_pred_initial, color='red', label='Initial Regression Line')
plt.scatter(X, Y, label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Points with Initial Regression Line')
plt.legend()
plt.show()
m = 0
c = 0
learning_rate = 0.0001
epochs = 1000
n = float(len(X))
for _ in range(epochs):
    Y_pred = m * X + c
    D_m = (-2 / n) * sum(X * (Y - Y_pred))
    D_c = (-2 / n) * sum(Y - Y_pred)
    m = m - learning_rate * D_m
    c = c - learning_rate * D_c
print(f"Final values: m = {m}, c = {c}")
Y_pred = m * X + c
plt.scatter(X, Y, label='Data Points')
plt.plot(X, Y_pred, color='red', label='Final Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Points with Final Regression Line')
plt.legend()
plt.show()