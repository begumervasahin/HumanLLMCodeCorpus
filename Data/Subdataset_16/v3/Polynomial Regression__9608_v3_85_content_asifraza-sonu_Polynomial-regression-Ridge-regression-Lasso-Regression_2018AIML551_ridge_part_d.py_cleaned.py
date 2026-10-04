import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import math
def fonk1(y_true, y_pred):
    return math.sqrt(mean_squared_error(y_true, y_pred))
b1 = pd.read_csv('project - part D - training data set.csv')
b2 = pd.read_csv('project - part D - testing data set.csv')
def fonk2(data):
    b3 = data['Father'].values / 10000
    b3 = b3.reshape(-1, 1)
    b4 = data['Son'].values.reshape(-1, 1)
    return b3, b4
X_train, b5 = fonk2(b1)
X_test, b6 = fonk2(b2)
a1 = 10
b7 = PolynomialFeatures(degree=a1)
b8 = b7.fit_transform(X_train)
b9 = b7.transform(X_test)
b10 = LinearRegression()
b10.fit(b8, b5)
b11 = b10.predict(b8)
b12 = b10.predict(b9)
b13 = fonk1(b5, b11)
b14 = fonk1(b6, b12)
b15 = Ridge()
b15.fit(b8, b5)
b16 = b15.predict(b8)
b17 = b15.predict(b9)
b18 = fonk1(b5, b16)
b19 = fonk1(b6, b17)
print(f'Train RMSE of polynomial regression model (degree {a1}): {b13:.4f}')
print(f'Test RMSE of polynomial regression model (degree {a1}): {b14:.4f}')
print(f'Train RMSE of ridge regression model (degree {a1}): {b18:.4f}')
print(f'Test RMSE of ridge regression model (degree {a1}): {b19:.4f}')