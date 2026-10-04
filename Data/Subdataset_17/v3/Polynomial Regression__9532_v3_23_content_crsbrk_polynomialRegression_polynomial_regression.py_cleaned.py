import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('~/Desktop/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
degree = 4
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
def visualize_regression(model, title, X, y, poly_transform=None, high_res=False):
    plt.scatter(X, y, color='red')
    if high_res:
        X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
        if poly_transform:
            plt.plot(X_grid, model.predict(poly_transform.fit_transform(X_grid)), color='blue')
        else:
            plt.plot(X_grid, model.predict(X_grid), color='blue')
    else:
        if poly_transform:
            plt.plot(X, model.predict(poly_transform.fit_transform(X)), color='blue')
        else:
            plt.plot(X, model.predict(X), color='blue')
    plt.title(title)
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
visualize_regression(linear_regressor, 'Truth or Bluff (Linear Regression)', X, y)
visualize_regression(poly_regressor, 'Truth or Bluff (Polynomial Regression)', X, y, poly_transform=poly_features)
visualize_regression(poly_regressor, 'Truth or Bluff (Polynomial Regression - High Resolution)', X, y, poly_transform=poly_features, high_res=True)
linear_pred = linear_regressor.predict(np.array([[6.5]]))
polynomial_pred = poly_regressor.predict(poly_features.fit_transform(np.array([[6.5]])))
print(f'Linear Regression prediction for 6.5: {linear_pred[0]}')
print(f'Polynomial Regression prediction for 6.5: {polynomial_pred[0]}')