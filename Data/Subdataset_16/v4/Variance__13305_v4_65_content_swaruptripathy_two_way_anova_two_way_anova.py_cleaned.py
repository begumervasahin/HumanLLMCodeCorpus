import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)
b9 = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
print(f"Dataset shape: {b9.shape}")
print(b9.head())
b2 = b9['Head Size(cm^3)'].values
b3 = b9['Brain Weight(grams)'].values
b4 = np.mean(b2)
b5 = np.mean(b3)
b6 = len(b2)
b7 = sum((b2[i] - b4) * (b3[i] - b5) for i in range(b6))
b8 = sum((b2[i] - b4) ** 2 for i in range(b6))
b9 = b7 / b8
b10 = b5 - (b9 * b4)
print(f"Coefficients: b9 = {b9}, b10 = {b10}")
b11 = np.max(b2) + 100
b12 = np.min(b2) - 100
b13 = np.linspace(b12, b11, 1000)
b14 = b10 + b9 * b13
plt.plot(b13, b14, b15 = 'blue', label='Regression Line')
plt.scatter(b2, b3, b16 = 'red', label='Scatter Plot')
plt.xlabel('Head Size in cmÂ³')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
b17 = np.sqrt(sum((b3[i] - (b10 + b9 * b2[i])) ** 2 for i in range(b6)) / b6)
print(f"RMSE: {b17}")
b18 = sum((b3[i] - b5) ** 2 for i in range(b6))
b19 = sum((b3[i] - (b10 + b9 * b2[i])) ** 2 for i in range(b6))
b20 = 1 - (b19 / b18)
print(f"RÂ²: {b20}")
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
b2 = b2.reshape((b6, 1))
b21 = LinearRegression().fit(b2, b3)
b22 = b21.predict(b2)
b23 = mean_squared_error(b3, b22)
b17 = np.sqrt(b23)
b24 = b21.score(b2, b3)
print(f"Sklearn RMSE: {b17}")
print(f"Sklearn RÂ²: {b24}")