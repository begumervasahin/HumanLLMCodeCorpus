
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_regressor.predict(X), color='blue')
plt.title('Level vs Salary (Linear Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, polynomial_regressor.predict(X_poly), color='blue')
plt.title('Level vs Salary (Polynomial Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, polynomial_regressor.predict(polynomial_features.transform(X_grid)), color='blue')
plt.title('Level vs Salary (Polynomial Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
level = [[6.5]]
linear_pred = linear_regressor.predict(level)[0]
poly_pred = polynomial_regressor.predict(polynomial_features.transform(level))[0]
print("Linear Regression Prediction:", linear_pred)
print("Polynomial Regression Prediction:", poly_pred)