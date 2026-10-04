import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
plt.rcParams['figure.figsize'] = (20.0, 10.0)
data = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
print(f"Dataset shape: {data.shape}")
print(data.head())
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values
mean_x = np.mean(X)
mean_y = np.mean(Y)
m = len(X)
numer = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(m))
denom = sum((X[i] - mean_x) ** 2 for i in range(m))
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)
print(f"Coefficients: b1 = {b1}, b0 = {b0}")
max_x = np.max(X) + 100
min_x = np.min(X) - 100
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x
plt.plot(x, y, color='blue', label='Regression Line')
plt.scatter(X, Y, c='red', label='Scatter Plot')
plt.xlabel('Head Size in cmÂ³')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
rmse = np.sqrt(sum((Y[i] - (b0 + b1 * X[i])) ** 2 for i in range(m)) / m)
print(f"RMSE: {rmse}")
ss_t = sum((Y[i] - mean_y) ** 2 for i in range(m))
ss_r = sum((Y[i] - (b0 + b1 * X[i])) ** 2 for i in range(m))
r2 = 1 - (ss_r / ss_t)
print(f"RÂ²: {r2}")
X = X.reshape((m, 1))
reg = LinearRegression().fit(X, Y)
Y_pred = reg.predict(X)
mse = mean_squared_error(Y, Y_pred)
rmse_sklearn = np.sqrt(mse)
r2_sklearn = reg.score(X, Y)
print(f"Sklearn RMSE: {rmse_sklearn}")
print(f"Sklearn RÂ²: {r2_sklearn}")