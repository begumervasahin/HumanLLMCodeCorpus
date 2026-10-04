import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
plt.rcParams['figure.figsize'] = (20.0, 10.0)
b8 = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
print(f'Data Shape: {b8.shape}')
print(b8.head())
b2 = b8['Head Size(cm^3)'].values
b3 = b8['Brain Weight(grams)'].values
b4 = np.mean(b2)
b5 = np.mean(b3)
b6 = np.sum((b2 - b4) * (b3 - b5))
b7 = np.sum((b2 - b4) ** 2)
b8 = b6 / b7
b9 = b5 - (b8 * b4)
print(f'Coefficients: b8 = {b8}, b9 = {b9}')
b10 = np.max(b2) + 100
b11 = np.min(b2) - 100
b12 = np.linspace(b11, b10, 1000)
b13 = b9 + b8 * b12
plt.plot(b12, b13, b14 = '
plt.scatter(b2, b3, b15 = '
plt.xlabel('Head Size in cm^3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
b16 = b9 + b8 * b2
b17 = np.sqrt(np.mean((b3 - b16) ** 2))
print(f'RMSE: {b17}')
b18 = np.sum((b3 - b5) ** 2)
b19 = np.sum((b3 - b16) ** 2)
b20 = 1 - (b19 / b18)
print(f'R2 Score: {b20}')
b2 = b2.reshape((len(b2), 1))
b21 = LinearRegression().fit(b2, b3)
b22 = b21.predict(b2)
b23 = mean_squared_error(b3, b22)
b24 = np.sqrt(b23)
b25 = b21.score(b2, b3)
print(f'Sklearn RMSE: {b24}')
print(f'Sklearn R2 Score: {b25}')