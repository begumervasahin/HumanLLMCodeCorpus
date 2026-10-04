import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_excel('placements.xlsx')
X = dataset.iloc[:, 2:3].values
y = dataset.iloc[:, 3].values
def perform_linear_regression(X, y):
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, y)
    return linear_regressor
linear_regressor = perform_linear_regression(X, y)
def perform_polynomial_regression(X, y, degree=4):
    polynomial_features = PolynomialFeatures(degree=degree)
    X_poly = polynomial_features.fit_transform(X)
    polynomial_regressor = LinearRegression()
    polynomial_regressor.fit(X_poly, y)
    return polynomial_features, polynomial_regressor
polynomial_features, polynomial_regressor = perform_polynomial_regression(X, y)
def plot_linear_regression(X, y, regressor):
    plt.scatter(X, y, color='red', label='Actual Data')
    plt.plot(X, regressor.predict(X), color='blue', label='Linear Regression')
    plt.title('Placement Record (Linear Regression)')
    plt.xlabel('Number of Students Placed')
    plt.ylabel('Year')
    plt.legend()
    plt.show()
plot_linear_regression(X, y, linear_regressor)
def plot_polynomial_regression(X, y, poly_features, poly_regressor):
    plt.scatter(X, y, color='red', label='Actual Data')
    plt.plot(X, poly_regressor.predict(poly_features.fit_transform(X)), color='blue', label='Polynomial Regression')
    plt.title('Placement Record (Polynomial Regression)')
    plt.xlabel('Number of Students Placed')
    plt.ylabel('Year')
    plt.legend()
    plt.show()
plot_polynomial_regression(X, y, polynomial_features, polynomial_regressor)
def plot_high_resolution_polynomial_regression(X, y, poly_features, poly_regressor):
    X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
    plt.scatter(X, y, color='red', label='Actual Data')
    plt.plot(X_grid, poly_regressor.predict(poly_features.fit_transform(X_grid)), color='blue', label='Polynomial Regression (Smooth)')
    plt.title('Placement Record (Polynomial Regression - High Resolution)')
    plt.xlabel('Number of Students Placed')
    plt.ylabel('Year')
    plt.legend()
    plt.show()
plot_high_resolution_polynomial_regression(X, y, polynomial_features, polynomial_regressor)