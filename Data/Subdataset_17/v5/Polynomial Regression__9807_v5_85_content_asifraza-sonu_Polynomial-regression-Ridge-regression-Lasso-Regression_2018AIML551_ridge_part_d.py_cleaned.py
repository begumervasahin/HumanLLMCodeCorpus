import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
import math
def load_data(train_path, test_path):
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    return train_data, test_data
def prepare_data(data):
    X = data['Father'].values.reshape(-1, 1) / 10000
    y = data['Son'].values.reshape(-1, 1)
    return X, y
def create_polynomial_features(X, degree):
    poly = PolynomialFeatures(degree=degree)
    return poly.fit_transform(X)
def calculate_rmse(y_true, y_pred):
    return math.sqrt(metrics.mean_squared_error(y_true, y_pred))
def print_rmse(model_name, train_rmse, test_rmse):
    print(f'Train RMSE of {model_name}: {train_rmse:.4f}')
    print(f'Test RMSE of {model_name}: {test_rmse:.4f}')
train_data, test_data = load_data('project - part D - training data set.csv', 'project - part D - testing data set.csv')
X_train, y_train = prepare_data(train_data)
X_test, y_test = prepare_data(test_data)
degree = 10
X_train_poly = create_polynomial_features(X_train, degree)
X_test_poly = create_polynomial_features(X_test, degree)
poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)
train_predictions_poly = poly_reg.predict(X_train_poly)
test_predictions_poly = poly_reg.predict(X_test_poly)
poly_reg_train_rmse = calculate_rmse(y_train, train_predictions_poly)
poly_reg_test_rmse = calculate_rmse(y_test, test_predictions_poly)
print_rmse('polynomial regression (degree 10)', poly_reg_train_rmse, poly_reg_test_rmse)
ridge_reg = Ridge()
ridge_reg.fit(X_train_poly, y_train)
train_predictions_ridge = ridge_reg.predict(X_train_poly)
test_predictions_ridge = ridge_reg.predict(X_test_poly)
ridge_reg_train_rmse = calculate_rmse(y_train, train_predictions_ridge)
ridge_reg_test_rmse = calculate_rmse(y_test, test_predictions_ridge)
print_rmse('ridge regression (degree 10)', ridge_reg_train_rmse, ridge_reg_test_rmse)