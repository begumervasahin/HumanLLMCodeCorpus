import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
lin_reg = LinearRegression()
lin_reg.fit(X, y)
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
plt.scatter(X, y, color='blue')
plt.plot(X, lin_reg.predict(X), color='red')
plt.title('Linear regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, y, color='blue')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='red')
plt.title('Polynomial regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='blue')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color='red')
plt.title('Polynomial regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()