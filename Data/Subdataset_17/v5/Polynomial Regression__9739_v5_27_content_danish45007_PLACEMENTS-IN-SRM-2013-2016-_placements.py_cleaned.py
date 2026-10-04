import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_excel('placements.xlsx')
X = dataset.iloc[:, 2:3].values
y = dataset.iloc[:, 3].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
degree = 4
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
def visualize_results(X, y, model, title, xlabel, ylabel, transform=None):
    plt.scatter(X, y, color='red')
    if transform:
        plt.plot(X, model.predict(transform(X)), color='blue')
    else:
        plt.plot(X, model.predict(X), color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
visualize_results(X, y, linear_regressor, 'PLACEMENT RECORD (Linear Regression)', 'NO. of Students placed', 'YEAR')
visualize_results(X, y, poly_regressor, 'PLACEMENT RECORD (Polynomial Regression)', 'NO. of Students placed', 'YEAR', transform=poly_features.transform)
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
visualize_results(X_grid, y, poly_regressor, 'PLACEMENT RECORD (Polynomial Regression - Smooth Curve)', 'NO. of Students placed', 'YEAR', transform=poly_features.transform)