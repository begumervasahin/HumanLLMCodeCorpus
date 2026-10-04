import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
def create_polynomial_regression(degree):
    polynomial_features = PolynomialFeatures(degree=degree)
    X_poly = polynomial_features.fit_transform(X)
    polynomial_regressor = LinearRegression()
    polynomial_regressor.fit(X_poly, y)
    return polynomial_regressor, polynomial_features
poly_regressor2, poly_features2 = create_polynomial_regression(degree=2)
poly_regressor3, poly_features3 = create_polynomial_regression(degree=3)
poly_regressor4, poly_features4 = create_polynomial_regression(degree=4)
def plot_regression(X, y, model, poly_features=None, title='Truth or Bluff', degree=None):
    plt.scatter(X, y, color='red')
    if poly_features:
        X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
        plt.plot(X_grid, model.predict(poly_features.fit_transform(X_grid)), color='blue')
        plt.title(f'{title} (Polynomial Regression degree {degree})')
    else:
        plt.plot(X, model.predict(X), color='blue')
        plt.title(f'{title} (Linear Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
plot_regression(X, y, linear_regressor, title='Linear Regression')
plot_regression(X, y, poly_regressor2, poly_features2, title='Polynomial Regression', degree=2)
plot_regression(X, y, poly_regressor3, poly_features3, title='Polynomial Regression', degree=3)
plot_regression(X, y, poly_regressor4, poly_features4, title='Polynomial Regression', degree=4)
linear_prediction = linear_regressor.predict([[6.2]])
poly_prediction = poly_regressor4.predict(poly_features4.fit_transform([[6.2]]))
print("Linear Regression Prediction for 6.2:", linear_prediction)
print("Polynomial Regression Prediction for 6.2:", poly_prediction)
print("Linear Regression Coefficients:", linear_regressor.coef_, "Intercept:", linear_regressor.intercept_)
print("Polynomial Regression Coefficients (degree 4):", poly_regressor4.coef_, "Intercept:", poly_regressor4.intercept_)