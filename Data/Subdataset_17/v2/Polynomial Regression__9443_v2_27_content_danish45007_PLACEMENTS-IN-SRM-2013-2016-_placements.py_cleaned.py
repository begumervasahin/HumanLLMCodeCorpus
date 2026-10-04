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
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X, linear_regressor.predict(X), color='blue', label='Linear Regression')
plt.title('Placement Record (Linear Regression)')
plt.xlabel('Number of Students Placed')
plt.ylabel('Year')
plt.legend()
plt.show()
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X, polynomial_regressor.predict(X_poly), color='blue', label='Polynomial Regression')
plt.title('Placement Record (Polynomial Regression)')
plt.xlabel('Number of Students Placed')
plt.ylabel('Year')
plt.legend()
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X_grid, polynomial_regressor.predict(polynomial_features.fit_transform(X_grid)), color='blue', label='Polynomial Regression (Smooth)')
plt.title('Placement Record (Polynomial Regression - High Resolution)')
plt.xlabel('Number of Students Placed')
plt.ylabel('Year')
plt.legend()
plt.show()