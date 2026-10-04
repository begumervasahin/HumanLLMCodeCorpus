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
poly_degree = 4
poly_features = PolynomialFeatures(degree=poly_degree)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
def visualize_results(title, regressor, X, y, poly_features=None, X_grid=None):
    plt.scatter(X, y, color='red')
    if X_grid is not None:
        plt.plot(X_grid, regressor.predict(poly_features.fit_transform(X_grid)), color='blue')
    else:
        plt.plot(X, regressor.predict(X), color='blue')
    plt.title(title)
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
visualize_results('Truth or Bluff (Linear Regression)', linear_regressor, X, y)
visualize_results('Truth or Bluff (Polynomial Regression)', poly_regressor, X, y, poly_features)
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
visualize_results('Truth or Bluff (Polynomial Regression - Smooth Curve)', poly_regressor, X, y, poly_features, X_grid)
linear_prediction = linear_regressor.predict([[6.5]])
print(f"Linear Regression Prediction for level 6.5: {linear_prediction[0]}")
poly_prediction = poly_regressor.predict(poly_features.fit_transform([[6.5]]))
print(f"Polynomial Regression Prediction for level 6.5: {poly_prediction[0]}")