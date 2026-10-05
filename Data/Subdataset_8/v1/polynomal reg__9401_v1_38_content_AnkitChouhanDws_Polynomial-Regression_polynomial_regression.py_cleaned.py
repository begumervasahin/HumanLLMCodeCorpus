import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Path To Dataset')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
lin_reg = LinearRegression()
lin_reg.fit(X, y)
poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
level = float(input('Enter your Experience level for Linear Regression: '))
print("Predicted Salary (Linear Regression):", lin_reg.predict(np.array([[level]]))[0])
level = float(input('Enter your Experience level for Polynomial Regression: '))
print("Predicted Salary (Polynomial Regression):", lin_reg2.predict(poly_reg.fit_transform([[level]]))[0])