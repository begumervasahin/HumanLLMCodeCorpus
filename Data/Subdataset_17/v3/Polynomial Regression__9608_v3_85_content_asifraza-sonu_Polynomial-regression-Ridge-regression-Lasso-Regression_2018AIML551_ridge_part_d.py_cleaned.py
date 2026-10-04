import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import math
def compute_rmse(y_true, y_pred):
    return math.sqrt(mean_squared_error(y_true, y_pred))
training_data = pd.read_csv('project - part D - training data set.csv')
testing_data = pd.read_csv('project - part D - testing data set.csv')
def prepare_data(data):
    X = data['Father'].values / 10000
    X = X.reshape(-1, 1)
    y = data['Son'].values.reshape(-1, 1)
    return X, y
X_train, y_train = prepare_data(training_data)
X_test, y_test = prepare_data(testing_data)
poly_degree = 10
poly = PolynomialFeatures(degree=poly_degree)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
poly_reg_model = LinearRegression()
poly_reg_model.fit(X_train_poly, y_train)
train_pred_poly = poly_reg_model.predict(X_train_poly)
test_pred_poly = poly_reg_model.predict(X_test_poly)
poly_reg_train_rmse = compute_rmse(y_train, train_pred_poly)
poly_reg_test_rmse = compute_rmse(y_test, test_pred_poly)
ridge_model = Ridge()
ridge_model.fit(X_train_poly, y_train)
train_pred_ridge = ridge_model.predict(X_train_poly)
test_pred_ridge = ridge_model.predict(X_test_poly)
ridge_train_rmse = compute_rmse(y_train, train_pred_ridge)
ridge_test_rmse = compute_rmse(y_test, test_pred_ridge)
print(f'Train RMSE of polynomial regression model (degree {poly_degree}): {poly_reg_train_rmse:.4f}')
print(f'Test RMSE of polynomial regression model (degree {poly_degree}): {poly_reg_test_rmse:.4f}')
print(f'Train RMSE of ridge regression model (degree {poly_degree}): {ridge_train_rmse:.4f}')
print(f'Test RMSE of ridge regression model (degree {poly_degree}): {ridge_test_rmse:.4f}')