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
degree = 4
poly_reg = PolynomialFeatures(degree=degree)
X_poly = poly_reg.fit_transform(X)
polynomial_linear_regressor = LinearRegression()
polynomial_linear_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red', label='Actual')
plt.plot(X, linear_regressor.predict(X), color='blue', label='Linear Model')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
X_grid = np.arange(min(X), max(X), 0.01).reshape(-1, 1)
plt.scatter(X, y, color='red', label='Actual')
plt.plot(X_grid, polynomial_linear_regressor.predict(poly_reg.fit_transform(X_grid)), color='blue', label='Polynomial Model')
plt.title(f'Truth or Bluff (Polynomial Regression, Degree={degree})')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
position_level = 6.5
linear_prediction = linear_regressor.predict([[position_level]])
polynomial_prediction = polynomial_linear_regressor.predict(poly_reg.fit_transform([[position_level]]))
print(f"Linear Regression Prediction for position level {position_level}: {linear_prediction[0]}")
print(f"Polynomial Regression Prediction for position level {position_level}: {polynomial_prediction[0]}")