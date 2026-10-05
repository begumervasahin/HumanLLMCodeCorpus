
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
head_size = data['Head Size(cm^3)'].values.reshape(-1, 1)
brain_weight = data['Brain Weight(grams)'].values
mean_head_size = np.mean(head_size)
mean_brain_weight = np.mean(brain_weight)
m = len(head_size)
numer = 0
denom = 0
for i in range(m):
    numer += (head_size[i] - mean_head_size) * (brain_weight[i] - mean_brain_weight)
    denom += (head_size[i] - mean_head_size) ** 2
b1 = numer / denom
b0 = mean_brain_weight - (b1 * mean_head_size)
predicted_brain_weight = b0 + b1 * head_size
plt.figure(figsize=(20, 10))
plt.plot(head_size, predicted_brain_weight, color='red', label='Regression Line')
plt.scatter(head_size, brain_weight, c='blue', label='Scatter Plot')
plt.xlabel('Head Size in cm^3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
rmse = np.sqrt(np.sum((brain_weight - predicted_brain_weight) ** 2) / m)
print("Root Mean Squared Error (RMSE):", rmse)
ss_total = np.sum((brain_weight - mean_brain_weight) ** 2)
ss_residual = np.sum((brain_weight - predicted_brain_weight) ** 2)
r_squared = 1 - (ss_residual / ss_total)
print("R-squared:", r_squared)
regressor = LinearRegression()
regressor.fit(head_size, brain_weight)
predicted_brain_weight_sklearn = regressor.predict(head_size)
rmse_sklearn = np.sqrt(mean_squared_error(brain_weight, predicted_brain_weight_sklearn))
r_squared_sklearn = regressor.score(head_size, brain_weight)
print("Sklearn RMSE:", rmse_sklearn)
print("Sklearn R-squared:", r_squared_sklearn)