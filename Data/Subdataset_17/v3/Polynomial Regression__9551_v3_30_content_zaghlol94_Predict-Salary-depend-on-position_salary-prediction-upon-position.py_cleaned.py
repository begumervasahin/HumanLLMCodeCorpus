import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
polynomial_degrees = [2, 3, 4]
def fit_and_plot_polynomial_regression(degree):
    poly_features = PolynomialFeatures(degree=degree)
    x_poly = poly_features.fit_transform(x)
    poly_regressor = LinearRegression()
    poly_regressor.fit(x_poly, y)
    plt.scatter(x, y, color='red')
    x_grid = np.arange(min(x), max(x), 0.1).reshape(-1, 1)
    plt.plot(x_grid, poly_regressor.predict(poly_features.fit_transform(x_grid)), color='blue')
    plt.title(f'Truth or Bluff (Polynomial Regression degree={degree})')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    return poly_regressor, poly_features
polynomial_regressors = {}
for degree in polynomial_degrees:
    poly_regressor, poly_features = fit_and_plot_polynomial_regression(degree)
    polynomial_regressors[degree] = (poly_regressor, poly_features)
linear_prediction = linear_regressor.predict([[6.2]])
print(f'Linear Regression prediction for position level 6.2: {linear_prediction[0]}')
degree = 4
poly_regressor, poly_features = polynomial_regressors[degree]
polynomial_prediction = poly_regressor.predict(poly_features.fit_transform([[6.2]]))
print(f'Polynomial Regression (degree={degree}) prediction for position level 6.2: {polynomial_prediction[0]}')
print(f'Linear Regression intercept: {linear_regressor.intercept_}')
print(f'Linear Regression coefficients: {linear_regressor.coef_}')
print(f'Polynomial Regression (degree={degree}) intercept: {poly_regressor.intercept_}')
print(f'Polynomial Regression (degree={degree}) coefficients: {poly_regressor.coef_}')