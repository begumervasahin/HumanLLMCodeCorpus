
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
b8 = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
b2 = b8['Head Size(cm^3)'].values
b3 = b8['Brain Weight(grams)'].values
b4 = np.mean(b2)
b5 = np.mean(b3)
b6 = np.sum((b2 - b4) * (b3 - b5))
b7 = np.sum((b2 - b4) ** 2)
b8 = b6 / b7
b9 = b5 - (b8 * b4)
plt.figure(b10 = (20, 10))
plt.scatter(b2, b3, b11 = 'red', label='Data Points')
plt.plot(b2, b9 + b8 * b2, b11 = 'blue', label='Regression Line')
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
b12 = np.sqrt(np.mean((b3 - (b9 + b8 * b2)) ** 2))
print("Root Mean Squared Error:", b12)
b13 = np.sum((b3 - b5) ** 2)
b14 = np.sum((b3 - (b9 + b8 * b2)) ** 2)
b15 = 1 - (b14 / b13)
print("R-squared Value:", b15)
b16 = LinearRegression().fit(b2.reshape(-1, 1), b3)
b17 = b16.predict(b2.reshape(-1, 1))
b18 = np.sqrt(mean_squared_error(b3, b17))
b19 = b16.score(b2.reshape(-1, 1), b3)
print("Root Mean Squared Error (Sklearn):", b18)
print("R-squared Value (Sklearn):", b19)