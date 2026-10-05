
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='green')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.title('Linear Regression')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg2.predict(X_poly), color='blue')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.title('Polynomial Regression')
plt.show()
position_level = 6.5
predicted_salary = lin_reg2.predict(poly_reg.fit_transform([[position_level]]))
print(f'Predicted Salary for Position Level {position_level}: ${predicted_salary[0]}')