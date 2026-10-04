import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
import math
training_data = pd.read_csv('project - part D - training data set.csv')
testing_data = pd.read_csv('project - part D - testing data set.csv')
X_train = training_data['Father'].values.reshape(-1, 1) / 10000
y_train = training_data['Son'].values.reshape(-1, 1)
X_test = testing_data['Father'].values.reshape(-1, 1) / 10000
y_test = testing_data['Son'].values.reshape(-1, 1)
poly = PolynomialFeatures(degree=10)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)
train_predictions_poly = poly_reg.predict(X_train_poly)
test_predictions_poly = poly_reg.predict(X_test_poly)
poly_reg_train_rmse = math.sqrt(metrics.mean_squared_error(y_train, train_predictions_poly))
poly_reg_test_rmse = math.sqrt(metrics.mean_squared_error(y_test, test_predictions_poly))
ridge_reg = Ridge()
ridge_reg.fit(X_train_poly, y_train)
train_predictions_ridge = ridge_reg.predict(X_train_poly)
test_predictions_ridge = ridge_reg.predict(X_test_poly)
ridge_reg_train_rmse = math.sqrt(metrics.mean_squared_error(y_train, train_predictions_ridge))
ridge_reg_test_rmse = math.sqrt(metrics.mean_squared_error(y_test, test_predictions_ridge))
print(f'Train RMSE of polynomial regression (degree 10): {poly_reg_train_rmse:.4f}')
print(f'Test RMSE of polynomial regression (degree 10): {poly_reg_test_rmse:.4f}')
print(f'Train RMSE of ridge regression (degree 10): {ridge_reg_train_rmse:.4f}')
print(f'Test RMSE of ridge regression (degree 10): {ridge_reg_test_rmse:.4f}')