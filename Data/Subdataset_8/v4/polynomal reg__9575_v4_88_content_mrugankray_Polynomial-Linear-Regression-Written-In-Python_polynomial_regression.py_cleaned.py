
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values
from sklearn.linear_model import LinearRegression
linear_reg_model = LinearRegression()
linear_reg_model.fit(X, Y)
from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
polynomial_reg_model = LinearRegression()
polynomial_reg_model.fit(X_poly, Y)
plt.scatter(X, Y, color='red')
plt.plot(X, linear_reg_model.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, Y, color='red')
plt.plot(X_grid, polynomial_reg_model.predict(poly_features.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
linear_prediction = linear_reg_model.predict([[6.5]])
polynomial_prediction = polynomial_reg_model.predict(poly_features.fit_transform([[6.5]]))
print("Predicted salary using Linear Regression:", linear_prediction)
print("Predicted salary using Polynomial Regression:", polynomial_prediction)