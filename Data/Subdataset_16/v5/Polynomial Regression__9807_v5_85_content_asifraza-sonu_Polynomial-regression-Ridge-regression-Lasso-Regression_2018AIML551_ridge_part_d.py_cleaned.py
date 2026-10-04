import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
import math
def fonk1(train_path, test_path):
    b1 = pd.read_csv(train_path)
    b2 = pd.read_csv(test_path)
    return b1, b2
def fonk2(data):
    b3 = data['Father'].values.reshape(-1, 1) / 10000
    b4 = data['Son'].values.reshape(-1, 1)
    return b3, b4
def fonk3(b3, a1):
    b5 = PolynomialFeatures(a1=a1)
    return b5.fit_transform(b3)
def fonk4(y_true, y_pred):
    return math.sqrt(metrics.mean_squared_error(y_true, y_pred))
def fonk5(model_name, train_rmse, test_rmse):
    print(f'Train RMSE of {model_name}: {train_rmse:.4f}')
    print(f'Test RMSE of {model_name}: {test_rmse:.4f}')
b1, b2 = fonk1('project - part D - training data set.csv', 'project - part D - testing data set.csv')
X_train, b6 = fonk2(b1)
X_test, b7 = fonk2(b2)
a1 = 10
b8 = fonk3(X_train, a1)
b9 = fonk3(X_test, a1)
b10 = LinearRegression()
b10.fit(b8, b6)
b11 = b10.predict(b8)
b12 = b10.predict(b9)
b13 = fonk4(b6, b11)
b14 = fonk4(b7, b12)
fonk5('polynomial regression (a1 10)', b13, b14)
b15 = Ridge()
b15.fit(b8, b6)
b16 = b15.predict(b8)
b17 = b15.predict(b9)
b18 = fonk4(b6, b16)
b19 = fonk4(b7, b17)
fonk5('ridge regression (a1 10)', b18, b19)