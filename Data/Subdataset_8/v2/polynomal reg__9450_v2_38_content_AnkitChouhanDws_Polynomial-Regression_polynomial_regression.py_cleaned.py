
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Path To Dataset')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_model = LinearRegression()
linear_model.fit(X, y)
polynomial_features = PolynomialFeatures(degree=5)
X_poly = polynomial_features.fit_transform(X)
polynomial_model = LinearRegression()
polynomial_model.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_model.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, polynomial_model.predict(polynomial_features.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
level_linear = float(input('Enter your Experience level for Linear Regression: '))
predicted_salary_linear = linear_model.predict(np.array([[level_linear]]))[0]
print("Predicted Salary (Linear Regression):", predicted_salary_linear)
level_poly = float(input('Enter your Experience level for Polynomial Regression: '))
predicted_salary_poly = polynomial_model.predict(polynomial_features.fit_transform([[level_poly]]))[0]
print("Predicted Salary (Polynomial Regression):", predicted_salary_poly)