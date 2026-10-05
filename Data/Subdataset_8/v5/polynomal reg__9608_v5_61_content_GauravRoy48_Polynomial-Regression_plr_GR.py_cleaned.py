
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_poly, Y)
plt.scatter(X, Y, color='red')
plt.plot(X, linear_regressor.predict(X), color='blue')
plt.title('Linear Regression Results')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, Y, color='red')
plt.plot(X, polynomial_regressor.predict(polynomial_features.fit_transform(X)), color='green')
plt.title('Polynomial Regression Results')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.grid()
plt.show()
predicted_salary_linear = linear_regressor.predict([[6.5]])
print("Predicted salary using Linear Regression:", predicted_salary_linear)
predicted_salary_poly = polynomial_regressor.predict(polynomial_features.transform([[6.5]]))
print("Predicted salary using Polynomial Regression:", predicted_salary_poly)