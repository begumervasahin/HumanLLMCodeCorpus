
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values
mean_x = np.mean(X)
mean_y = np.mean(Y)
numer = np.sum((X - mean_x) * (Y - mean_y))
denom = np.sum((X - mean_x) ** 2)
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)
plt.figure(figsize=(20, 10))
plt.scatter(X, Y, color='red', label='Data Points')
plt.plot(X, b0 + b1 * X, color='blue', label='Regression Line')
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
rmse = np.sqrt(np.mean((Y - (b0 + b1 * X)) ** 2))
print("Root Mean Squared Error:", rmse)
ss_t = np.sum((Y - mean_y) ** 2)
ss_r = np.sum((Y - (b0 + b1 * X)) ** 2)
r2 = 1 - (ss_r / ss_t)
print("R-squared Value:", r2)
reg = LinearRegression().fit(X.reshape(-1, 1), Y)
Y_pred = reg.predict(X.reshape(-1, 1))
rmse_sklearn = np.sqrt(mean_squared_error(Y, Y_pred))
r2_score_sklearn = reg.score(X.reshape(-1, 1), Y)
print("Root Mean Squared Error (Sklearn):", rmse_sklearn)
print("R-squared Value (Sklearn):", r2_score_sklearn)