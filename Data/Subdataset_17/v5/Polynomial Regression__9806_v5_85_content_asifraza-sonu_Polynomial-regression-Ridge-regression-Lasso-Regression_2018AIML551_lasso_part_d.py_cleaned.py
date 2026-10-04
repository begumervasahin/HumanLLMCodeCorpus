import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso
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
def compute_rmse(y_true, y_pred):
    return math.sqrt(metrics.mean_squared_error(y_true, y_pred))
def main():
    train_data, test_data = load_data('project - part D - training data set.csv', 'project - part D - testing data set.csv')
    X_train, y_train = prepare_data(train_data)
    X_test, y_test = prepare_data(test_data)
    degree = 10
    X_train_poly = create_polynomial_features(X_train, degree)
    X_test_poly = create_polynomial_features(X_test, degree)
    poly_reg = LinearRegression()
    poly_reg.fit(X_train_poly, y_train)
    y_train_pred_poly = poly_reg.predict(X_train_poly)
    y_test_pred_poly = poly_reg.predict(X_test_poly)
    lasso_reg = Lasso()
    lasso_reg.fit(X_train_poly, y_train)
    y_train_pred_lasso = lasso_reg.predict(X_train_poly)
    y_test_pred_lasso = lasso_reg.predict(X_test_poly)
    train_rmse_poly = compute_rmse(y_train, y_train_pred_poly)
    test_rmse_poly = compute_rmse(y_test, y_test_pred_poly)
    train_rmse_lasso = compute_rmse(y_train, y_train_pred_lasso)
    test_rmse_lasso = compute_rmse(y_test, y_test_pred_lasso)
    print(f'Train RMSE of polynomial regression (degree {degree}): {train_rmse_poly:.4f}')
    print(f'Test RMSE of polynomial regression (degree {degree}): {test_rmse_poly:.4f}')
    print(f'Train RMSE of Lasso regression (degree {degree}): {train_rmse_lasso:.4f}')
    print(f'Test RMSE of Lasso regression (degree {degree}): {test_rmse_lasso:.4f}')
if __name__ == "__main__":
    main()