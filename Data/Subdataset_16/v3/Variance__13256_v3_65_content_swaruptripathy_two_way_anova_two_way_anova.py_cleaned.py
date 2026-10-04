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
def fonk1(b2, b3, b4, b5):
    b6 = np.sum((b2 - b4) * (b3 - b5))
    b7 = np.sum((b2 - b4) ** 2)
    b8 = b6 / b7
    b9 = b5 - (b8 * b4)
    return b8, b9
b8, b9 = fonk1(b2, b3, b4, b5)
print(f'Coefficients: b8 = {b8}, b9 = {b9}')
def fonk2(b2, b3, b9, b8):
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
fonk2(b2, b3, b9, b8)
def fonk3(b3, b16):
    return np.sqrt(np.mean((b3 - b16) ** 2))
b16 = b9 + b8 * b2
b17 = fonk3(b3, b16)
print(f'RMSE: {b17}')
def fonk4(b3, b16, b5):
    b18 = np.sum((b3 - b5) ** 2)
    b19 = np.sum((b3 - b16) ** 2)
    return 1 - (b19 / b18)
b20 = fonk4(b3, b16, b5)
print(f'R2 Score: {b20}')
def fonk5(b2, b3):
    b21 = b2.reshape((len(b2), 1))
    b22 = LinearRegression().fit(b21, b3)
    b23 = b22.predict(b21)
    b24 = mean_squared_error(b3, b23)
    b17 = np.sqrt(b24)
    b25 = b22.score(b21, b3)
    return b17, b25
rmse_sklearn, b26 = fonk5(b2, b3)
print(f'Sklearn RMSE: {rmse_sklearn}')
print(f'Sklearn R2 Score: {b26}')