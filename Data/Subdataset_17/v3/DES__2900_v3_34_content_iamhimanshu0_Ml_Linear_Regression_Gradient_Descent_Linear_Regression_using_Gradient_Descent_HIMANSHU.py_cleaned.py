import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 5.0)
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y, label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Points')
plt.show()
mean_x = np.mean(X)
mean_y = np.mean(Y)
diff_x = X - mean_x
diff_y = Y - mean_y
slope = np.sum(diff_x * diff_y) / np.sum(diff_x ** 2)
intercept = mean_y - slope * mean_x
initial_Y_pred = slope * X + intercept
plt.scatter(X, Y, label='Data Points')
plt.plot(X, initial_Y_pred, color='red', label='Initial Regression Line')
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
final_Y_pred = m * X + c
plt.scatter(X, Y, label='Data Points')
plt.plot(X, final_Y_pred, color='red', label='Final Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Points with Final Regression Line')
plt.legend()
plt.show()