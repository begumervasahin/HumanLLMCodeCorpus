import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    X = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, 2].values
    return X, y
def fit_linear_regression(X, y):
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, y)
    return linear_regressor
def fit_polynomial_regression(X, y, degree):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    poly_regressor = LinearRegression()
    poly_regressor.fit(X_poly, y)
    return poly_features, poly_regressor
def visualize_regression_results(X, y, model, model_type, poly_features=None, resolution=0.1):
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='red')
    if model_type == 'linear':
        plt.plot(X, model.predict(X), color='blue')
        plt.title('Truth or Bluff (Linear Regression)')
    elif model_type == 'polynomial':
        X_grid = np.arange(min(X), max(X), resolution)
        X_grid = X_grid.reshape((len(X_grid), 1))
        plt.plot(X_grid, model.predict(poly_features.fit_transform(X_grid)), color='blue')
        plt.title('Truth or Bluff (Polynomial Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
X, y = load_dataset('position_salaries.csv')
linear_model = fit_linear_regression(X, y)
poly_features, poly_model = fit_polynomial_regression(X, y, degree=4)
visualize_regression_results(X, y, linear_model, model_type='linear')
visualize_regression_results(X, y, poly_model, model_type='polynomial', poly_features=poly_features)
plt.savefig('position_salary.png')
