import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import math
def load_data(train_path, test_path):
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    return train_data, test_data
def preprocess_data(data):
    X = data['Father'].values / 10000
    X = X.reshape(-1, 1)
    y = data['Son'].values.reshape(-1, 1)
    return X, y
def polynomial_transform(X, degree):
    poly = PolynomialFeatures(degree=degree)
    return poly.fit_transform(X)
def calculate_rmse(y_true, y_pred):
    return math.sqrt(mean_squared_error(y_true, y_pred))
def main():
    train_path = 'project - part D - training data set.csv'
    test_path = 'project - part D - testing data set.csv'
    training_data, testing_data = load_data(train_path, test_path)
    X_train, y_train = preprocess_data(training_data)
    X_test, y_test = preprocess_data(testing_data)
    degree = 10
    X_train_poly = polynomial_transform(X_train, degree)
    X_test_poly = polynomial_transform(X_test, degree)
    poly_reg_model = LinearRegression()
    poly_reg_model.fit(X_train_poly, y_train)
    train_pred_poly = poly_reg_model.predict(X_train_poly)
    test_pred_poly = poly_reg_model.predict(X_test_poly)
    train_rmse_poly = calculate_rmse(y_train, train_pred_poly)
    test_rmse_poly = calculate_rmse(y_test, test_pred_poly)
    lasso_model = Lasso()
    lasso_model.fit(X_train_poly, y_train)
    train_pred_lasso = lasso_model.predict(X_train_poly)
    test_pred_lasso = lasso_model.predict(X_test_poly)
    train_rmse_lasso = calculate_rmse(y_train, train_pred_lasso)
    test_rmse_lasso = calculate_rmse(y_test, test_pred_lasso)
    print(f'Train RMSE of polynomial regression model (degree {degree}): {train_rmse_poly:.4f}')
    print(f'Test RMSE of polynomial regression model (degree {degree}): {test_rmse_poly:.4f}')
    print(f'Train RMSE of Lasso regression model: {train_rmse_lasso:.4f}')
    print(f'Test RMSE of Lasso regression model: {test_rmse_lasso:.4f}')
if __name__ == "__main__":
    main()