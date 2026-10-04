
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
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
polynomial_linear_regressor = LinearRegression()
polynomial_linear_regressor.fit(X_poly, y)
def plot_regression_results(X, y, regressor, title, xlabel, ylabel, transform=None):
    plt.scatter(X, y, color='red')
    if transform:
        plt.plot(X, regressor.predict(transform(X)), color='blue')
    else:
        plt.plot(X, regressor.predict(X), color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
plot_regression_results(X, y, linear_regressor, 'Truth or Bluff (Linear Regression)', 'Position Level', 'Salary')
X_grid = np.arange(min(X), max(X), 0.01).reshape(-1, 1)
plot_regression_results(X_grid, y, polynomial_linear_regressor, 'Truth or Bluff (Polynomial Regression)', 'Position Level', 'Salary', transform=poly_reg.fit_transform)
linear_prediction = linear_regressor.predict(np.array([[6.5]]))
print(f'Linear Regression Prediction for 6.5: {linear_prediction[0]}')
poly_prediction = polynomial_linear_regressor.predict(poly_reg.fit_transform(np.array([[6.5]])))
print(f'Polynomial Regression Prediction for 6.5: {poly_prediction[0]}')