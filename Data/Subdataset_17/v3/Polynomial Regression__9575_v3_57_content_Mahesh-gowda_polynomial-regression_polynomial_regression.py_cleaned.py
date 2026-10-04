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
degree = 4
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
def visualize_regression_results(X, y, model, title, xlabel, ylabel, poly_features=None):
    plt.scatter(X, y, color='red')
    if poly_features is not None:
        plt.plot(X, model.predict(poly_features.fit_transform(X)), color='blue')
    else:
        plt.plot(X, model.predict(X), color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
visualize_regression_results(X, y, linear_regressor, 'Truth or Bluff (Linear Regression)', 'Position level', 'Salary')
visualize_regression_results(X, y, poly_regressor, 'Truth or Bluff (Polynomial Regression)', 'Position level', 'Salary', poly_features)
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
visualize_regression_results(X_grid, y, poly_regressor, 'Truth or Bluff (Polynomial Regression - High Resolution)', 'Position level', 'Salary', poly_features)
linear_prediction = linear_regressor.predict([[6.5]])
poly_prediction = poly_regressor.predict(poly_features.fit_transform([[6.5]]))
print("Linear Regression prediction for position level 6.5: ", linear_prediction[0])
print("Polynomial Regression prediction for position level 6.5: ", poly_prediction[0])