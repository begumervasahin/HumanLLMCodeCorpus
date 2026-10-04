import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
import math
training_data = pd.read_csv('project - part D - training data set.csv')
testing_data = pd.read_csv('project - part D - testing data set.csv')
X_train = training_data['Father'].values / 10000
X_train = X_train.reshape(-1, 1)
y_train = training_data['Son'].values.reshape(-1, 1)
X_test = testing_data['Father'].values / 10000
X_test = X_test.reshape(-1, 1)
y_test = testing_data['Son'].values.reshape(-1, 1)
poly = PolynomialFeatures(degree=10)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
poly_reg_model = LinearRegression()
poly_reg_model.fit(X_train_poly, y_train)
train_predictions_poly = poly_reg_model.predict(X_train_poly)
test_predictions_poly = poly_reg_model.predict(X_test_poly)
train_rmse_poly = math.sqrt(metrics.mean_squared_error(y_train, train_predictions_poly))
test_rmse_poly = math.sqrt(metrics.mean_squared_error(y_test, test_predictions_poly))
lasso_model = Lasso()
lasso_model.fit(X_train_poly, y_train)
train_predictions_lasso = lasso_model.predict(X_train_poly)
test_predictions_lasso = lasso_model.predict(X_test_poly)
train_rmse_lasso = math.sqrt(metrics.mean_squared_error(y_train, train_predictions_lasso))
test_rmse_lasso = math.sqrt(metrics.mean_squared_error(y_test, test_predictions_lasso))
print(f'Train RMSE of polynomial regression model (degree 10): {train_rmse_poly:.4f}')
print(f'Test RMSE of polynomial regression model (degree 10): {test_rmse_poly:.4f}')
print(f'Train RMSE of Lasso regression model: {train_rmse_lasso:.4f}')
print(f'Test RMSE of Lasso regression model: {test_rmse_lasso:.4f}')