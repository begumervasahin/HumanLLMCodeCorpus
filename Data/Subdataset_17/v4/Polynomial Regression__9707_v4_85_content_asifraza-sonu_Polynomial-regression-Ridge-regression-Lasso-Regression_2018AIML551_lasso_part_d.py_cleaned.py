import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
import math
train_data = pd.read_csv('project - part D - training data set.csv')
test_data = pd.read_csv('project - part D - testing data set.csv')
X_train = train_data['Father'].values.reshape(-1, 1) / 10000
y_train = train_data['Son'].values.reshape(-1, 1)
X_test = test_data['Father'].values.reshape(-1, 1) / 10000
y_test = test_data['Son'].values.reshape(-1, 1)
poly = PolynomialFeatures(degree=10)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)
train_rmse_poly = math.sqrt(metrics.mean_squared_error(y_train, poly_reg.predict(X_train_poly)))
test_rmse_poly = math.sqrt(metrics.mean_squared_error(y_test, poly_reg.predict(X_test_poly)))
lasso_reg = Lasso()
lasso_reg.fit(X_train_poly, y_train)
train_rmse_lasso = math.sqrt(metrics.mean_squared_error(y_train, lasso_reg.predict(X_train_poly)))
test_rmse_lasso = math.sqrt(metrics.mean_squared_error(y_test, lasso_reg.predict(X_test_poly)))
print(f'Train RMSE of polynomial regression (degree 10): {train_rmse_poly:.4f}')
print(f'Test RMSE of polynomial regression (degree 10): {test_rmse_poly:.4f}')
print(f'Train RMSE of Lasso regression (degree 10): {train_rmse_lasso:.4f}')
print(f'Test RMSE of Lasso regression (degree 10): {test_rmse_lasso:.4f}')