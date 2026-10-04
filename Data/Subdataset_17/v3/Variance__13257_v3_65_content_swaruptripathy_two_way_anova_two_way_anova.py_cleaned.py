import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
plt.rcParams['figure.figsize'] = (20.0, 10.0)
data = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
print(f'Data Shape: {data.shape}')
print(data.head())
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values
mean_x = np.mean(X)
mean_y = np.mean(Y)
def calculate_coefficients(X, Y, mean_x, mean_y):
    numer = np.sum((X - mean_x) * (Y - mean_y))
    denom = np.sum((X - mean_x) ** 2)
    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)
    return b1, b0
b1, b0 = calculate_coefficients(X, Y, mean_x, mean_y)
print(f'Coefficients: b1 = {b1}, b0 = {b0}')
def plot_regression_line(X, Y, b0, b1):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100
    x = np.linspace(min_x, max_x, 1000)
    y = b0 + b1 * x
    plt.plot(x, y, color='
    plt.scatter(X, Y, c='
    plt.xlabel('Head Size in cm^3')
    plt.ylabel('Brain Weight in grams')
    plt.legend()
    plt.show()
plot_regression_line(X, Y, b0, b1)
def calculate_rmse(Y, y_pred):
    return np.sqrt(np.mean((Y - y_pred) ** 2))
y_pred = b0 + b1 * X
rmse = calculate_rmse(Y, y_pred)
print(f'RMSE: {rmse}')
def calculate_r2_score(Y, y_pred, mean_y):
    ss_t = np.sum((Y - mean_y) ** 2)
    ss_r = np.sum((Y - y_pred) ** 2)
    return 1 - (ss_r / ss_t)
r2 = calculate_r2_score(Y, y_pred, mean_y)
print(f'R2 Score: {r2}')
def sklearn_linear_regression(X, Y):
    X_reshaped = X.reshape((len(X), 1))
    reg = LinearRegression().fit(X_reshaped, Y)
    Y_pred = reg.predict(X_reshaped)
    mse = mean_squared_error(Y, Y_pred)
    rmse = np.sqrt(mse)
    r2_score = reg.score(X_reshaped, Y)
    return rmse, r2_score
rmse_sklearn, r2_score_sklearn = sklearn_linear_regression(X, Y)
print(f'Sklearn RMSE: {rmse_sklearn}')
print(f'Sklearn R2 Score: {r2_score_sklearn}')