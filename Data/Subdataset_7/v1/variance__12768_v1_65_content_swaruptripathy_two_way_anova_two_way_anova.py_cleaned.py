import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
b7 = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
b2 = b7['Head Size(cm^3)'].values.reshape(-1, 1)
b3 = b7['Brain Weight(grams)'].values
b4 = np.mean(b2)
b5 = np.mean(b3)
b6 = len(b2)
a1 = 0
a2 = 0
for i in range(b6):
    a1 += (b2[i] - b4) * (b3[i] - b5)
    a2 += (b2[i] - b4) ** 2
b7 = a1 / a2
b8 = b5 - (b7 * b4)
b9 = b8 + b7 * b2
plt.figure(b10 = (20, 10))
plt.plot(b2, b9, b11 = 'red', label='Regression Line')
plt.scatter(b2, b3, b12 = 'blue', label='Scatter Plot')
plt.xlabel('Head Size in cm^3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
b13 = np.sqrt(mean_squared_error(b3, b9))
print("Root Mean Squared Error (RMSE):", b13)
b14 = np.sum((b3 - b5) ** 2)
b15 = np.sum((b3 - b9) ** 2)
b16 = 1 - (b15/b14)
print("R-squared:", b16)
b17 = LinearRegression()
b17.fit(b2, b3)
b18 = b17.predict(b2)
b19 = np.sqrt(mean_squared_error(b3, b18))
b20 = b17.score(b2, b3)
print("Sklearn RMSE:", b19)
print("Sklearn R-squared:", b20)