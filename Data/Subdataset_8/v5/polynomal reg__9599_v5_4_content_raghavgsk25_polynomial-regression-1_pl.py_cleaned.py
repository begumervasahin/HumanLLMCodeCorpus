
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1].values.reshape(-1, 1)
y = dataset.iloc[:, 2].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_poly, y)
plt.scatter(X, y, color='blue')
plt.plot(X, linear_regressor.predict(X), color='red')
plt.title('Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, y, color='blue')
plt.plot(X, polynomial_regressor.predict(polynomial_features.fit_transform(X)), color='red')
plt.title('Polynomial Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='blue')
plt.plot(X_grid, polynomial_regressor.predict(polynomial_features.transform(X_grid)), color='red')
plt.title('Polynomial Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()