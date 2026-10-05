import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def load_dataset(file_path):
    return pd.read_csv(file_path)
def extract_features_and_target(dataset):
    X = dataset.iloc[:, 0:1].values
    y = dataset.iloc[:, 1:2].values
    return X, y
def split_dataset(X, y, test_size=0.2, random_state=0):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
def fit_linear_regression(X, y):
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, y)
    return linear_regressor
def fit_polynomial_regression(X, y, degree=2):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    poly_regressor = LinearRegression()
    poly_regressor.fit(X_poly, y)
    return poly_regressor, poly_features
def visualize_results(X, y, regression_model, title):
    plt.scatter(X, y, color='red')
    plt.plot(X, regression_model.predict(X), color='blue')
    plt.title(title)
    plt.xlabel('Days of Year 1998')
    plt.ylabel('CO Values in AGU')
    plt.show()
dataset = load_dataset('HORA08_AGU_CO_1998-01-01_1998-12-31_1521371719602.csv')
X, y = extract_features_and_target(dataset)
X_train, X_test, y_train, y_test = split_dataset(X, y)
linear_regressor = fit_linear_regression(X_train, y_train)
poly_regressor, poly_features = fit_polynomial_regression(X_train, y_train)
visualize_results(X, y, linear_regressor, 'Linear Regression')
visualize_results(X, y, poly_regressor, 'Polynomial Regression (Degree 2)')