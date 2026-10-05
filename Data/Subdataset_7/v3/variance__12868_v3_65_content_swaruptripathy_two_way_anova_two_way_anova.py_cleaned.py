
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b9 = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
b2 = b9['Head Size(cm^3)'].values.reshape(-1, 1)
b3 = b9['Brain Weight(grams)'].values
b4 = np.mean(b2)
b5 = np.mean(b3)
b6 = len(b2)
b7 = np.sum((b2 - b4) * (b3 - b5))
b8 = np.sum((b2 - b4) ** 2)
b9 = b7 / b8
b10 = b5 - (b9 * b4)
b11 = b10 + b9 * b2
plt.figure(b12 = (20, 10))
plt.plot(b2, b11, b13 = 'red', label='Regression Line')
plt.scatter(b2, b3, b14 = 'blue', label='Scatter Plot')
plt.xlabel('Head Size in cm^3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
b15 = np.sqrt(np.mean((b3 - b11) ** 2))
print("Root Mean Squared Error (RMSE):", b15)
b16 = np.sum((b3 - b5) ** 2)
b17 = np.sum((b3 - b11) ** 2)
b18 = 1 - (b17 / b16)
print("R-squared:", b18)
b19 = LinearRegression()
b19.fit(b2, b3)
b20 = b19.predict(b2)
b21 = np.sqrt(mean_squared_error(b3, b20))
b22 = b19.score(b2, b3)
print("Sklearn RMSE:", b21)
print("Sklearn R-squared:", b22)