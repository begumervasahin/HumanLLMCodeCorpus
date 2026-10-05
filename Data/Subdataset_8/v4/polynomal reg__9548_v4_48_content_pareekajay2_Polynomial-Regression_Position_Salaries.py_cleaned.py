
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
from sklearn.preprocessing import PolynomialFeatures
poly_feature = PolynomialFeatures(degree=4)
X_poly = poly_feature.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_regressor.predict(X), color='blue')
plt.title('Position Level vs Salary (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, poly_regressor.predict(X_poly), color='blue')
plt.title('Position Level vs Salary (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, poly_regressor.predict(poly_feature.transform(X_grid)), color='blue')
plt.title('Position Level vs Salary (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
predicted_salary_linear = linear_regressor.predict([[6.5]])
print("Predicted Salary using Linear Regression:", predicted_salary_linear)
predicted_salary_poly = poly_regressor.predict(poly_feature.transform([[6.5]]))
print("Predicted Salary using Polynomial Regression:", predicted_salary_poly)