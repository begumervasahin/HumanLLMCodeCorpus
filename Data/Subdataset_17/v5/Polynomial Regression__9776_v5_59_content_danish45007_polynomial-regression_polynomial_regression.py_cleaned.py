import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('position_salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
def visualize_regression_results(X, y, model, title, X_transformation=None):
    plt.scatter(X, y, color='red')
    if X_transformation:
        plt.plot(X, model.predict(X_transformation(X)), color='blue')
    else:
        plt.plot(X, model.predict(X), color='blue')
    plt.title(title)
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
visualize_regression_results(X, y, linear_regressor, 'Truth or Bluff (Linear Regression)')
visualize_regression_results(X, y, poly_regressor, 'Truth or Bluff (Polynomial Regression)', X_transformation=poly_features.fit_transform)
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
visualize_regression_results(X_grid, y, poly_regressor, 'Truth or Bluff (Polynomial Regression - High Resolution)', X_transformation=poly_features.fit_transform)
plt.scatter(X, y, color='red')
plt.plot(X_grid, poly_regressor.predict(poly_features.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.savefig('position_salary.png')
