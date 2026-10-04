import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import math
def fonk1(b6, b7):
    b1 = pd.read_csv(b6)
    b2 = pd.read_csv(b7)
    return b1, b2
def fonk2(data):
    b3 = data['Father'].values / 10000
    b3 = b3.reshape(-1, 1)
    b4 = data['Son'].values.reshape(-1, 1)
    return b3, b4
def fonk3(b3, a1):
    b5 = PolynomialFeatures(a1=a1)
    return b5.fit_transform(b3)
def fonk4(y_true, y_pred):
    return math.sqrt(mean_squared_error(y_true, y_pred))
def fonk5():
    b6 = 'project - part D - training data set.csv'
    b7 = 'project - part D - testing data set.csv'
    training_data, b8 = fonk1(b6, b7)
    X_train, b9 = fonk2(training_data)
    X_test, b10 = fonk2(b8)
    a1 = 10
    b11 = fonk3(X_train, a1)
    b12 = fonk3(X_test, a1)
    b13 = LinearRegression()
    b13.fit(b11, b9)
    b14 = b13.predict(b11)
    b15 = b13.predict(b12)
    b16 = fonk4(b9, b14)
    b17 = fonk4(b10, b15)
    b18 = Lasso()
    b18.fit(b11, b9)
    b19 = b18.predict(b11)
    b20 = b18.predict(b12)
    b21 = fonk4(b9, b19)
    b22 = fonk4(b10, b20)
    print(f'Train RMSE of polynomial regression model (a1 {a1}): {b16:.4f}')
    print(f'Test RMSE of polynomial regression model (a1 {a1}): {b17:.4f}')
    print(f'Train RMSE of Lasso regression model: {b21:.4f}')
    print(f'Test RMSE of Lasso regression model: {b22:.4f}')
if b23 = = "__main__":
    fonk5()