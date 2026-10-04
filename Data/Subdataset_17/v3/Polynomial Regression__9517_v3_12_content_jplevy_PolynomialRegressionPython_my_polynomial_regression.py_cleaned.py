import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def load_dataset(filename):
    return pd.read_csv(filename)
def train_linear_regression(X, y):
    regressor = LinearRegression()
    regressor.fit(X, y)
    return regressor
def train_polynomial_regression(X, y, degree):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    regressor = LinearRegression()
    regressor.fit(X_poly, y)
    return regressor, poly_features
def visualize_results(X, y, model, title, xlabel, ylabel, poly_features=None):
    plt.scatter(X, y, color='red', label='Actual')
    if poly_features is not None:
        X_grid = np.arange(min(X), max(X), 0.01).reshape(-1, 1)
        plt.plot(X_grid, model.predict(poly_features.fit_transform(X_grid)), color='blue', label='Model')
    else:
        plt.plot(X, model.predict(X), color='blue', label='Model')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
def predict(model, position_level, poly_features=None):
    if poly_features is not None:
        return model.predict(poly_features.fit_transform([[position_level]]))[0]
    else:
        return model.predict([[position_level]])[0]
if __name__ == "__main__":
    dataset = load_dataset('Position_Salaries.csv')
    X = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, 2].values
    linear_regressor = train_linear_regression(X, y)
    degree = 4
    polynomial_regressor, poly_features = train_polynomial_regression(X, y, degree)
    visualize_results(X, y, linear_regressor, 'Truth or Bluff (Linear Regression)', 'Position Level', 'Salary')
    visualize_results(X, y, polynomial_regressor, f'Truth or Bluff (Polynomial Regression, Degree={degree})', 'Position Level', 'Salary', poly_features)
    position_level = 6.5
    linear_prediction = predict(linear_regressor, position_level)
    polynomial_prediction = predict(polynomial_regressor, position_level, poly_features)
    print(f"Linear Regression Prediction for position level {position_level}: {linear_prediction}")
    print(f"Polynomial Regression Prediction for position level {position_level}: {polynomial_prediction}")