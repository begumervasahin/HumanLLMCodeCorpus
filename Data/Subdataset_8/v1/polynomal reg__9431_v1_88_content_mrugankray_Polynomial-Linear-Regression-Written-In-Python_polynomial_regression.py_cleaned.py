import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values
line_reg = LinearRegression()
line_reg.fit(X, Y)
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
line_reg_2 = LinearRegression()
line_reg_2.fit(X_poly, Y)
plt.scatter(X, Y, color='red')
plt.plot(X, line_reg.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Experience Level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, Y, color='red')
plt.plot(X_grid, line_reg_2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Experience Level')
plt.ylabel('Salary')
plt.show()
print("Predicted salary using Linear Regression:", line_reg.predict([[6.5]])[0])
print("Predicted salary using Polynomial Regression:", line_reg_2.predict(poly_reg.fit_transform([[6.5]]))[0])