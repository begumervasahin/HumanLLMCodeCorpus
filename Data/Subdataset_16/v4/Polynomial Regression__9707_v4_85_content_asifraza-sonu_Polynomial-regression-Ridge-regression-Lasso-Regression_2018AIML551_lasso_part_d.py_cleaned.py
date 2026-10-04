import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
import math
b1 = pd.read_csv('project - part D - training data set.csv')
b2 = pd.read_csv('project - part D - testing data set.csv')
b3 = b1['Father'].values.reshape(-1, 1) / 10000
b4 = b1['Son'].values.reshape(-1, 1)
b5 = b2['Father'].values.reshape(-1, 1) / 10000
b6 = b2['Son'].values.reshape(-1, 1)
b7 = PolynomialFeatures(degree=10)
b8 = b7.fit_transform(b3)
b9 = b7.transform(b5)
b10 = LinearRegression()
b10.fit(b8, b4)
b11 = math.sqrt(metrics.mean_squared_error(b4, b10.predict(b8)))
b12 = math.sqrt(metrics.mean_squared_error(b6, b10.predict(b9)))
b13 = Lasso()
b13.fit(b8, b4)
b14 = math.sqrt(metrics.mean_squared_error(b4, b13.predict(b8)))
b15 = math.sqrt(metrics.mean_squared_error(b6, b13.predict(b9)))
print(f'Train RMSE of polynomial regression (degree 10): {b11:.4f}')
print(f'Test RMSE of polynomial regression (degree 10): {b12:.4f}')
print(f'Train RMSE of Lasso regression (degree 10): {b14:.4f}')
print(f'Test RMSE of Lasso regression (degree 10): {b15:.4f}')