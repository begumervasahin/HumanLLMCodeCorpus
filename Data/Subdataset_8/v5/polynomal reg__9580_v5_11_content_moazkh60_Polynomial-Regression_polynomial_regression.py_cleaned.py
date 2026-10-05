
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
lin_reg = LinearRegression()
lin_reg.fit(X, y)
degree = 4
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='green', label='Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.title('Linear Regression')
plt.legend()
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, poly_reg.predict(X_poly), color='blue', label='Polynomial Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.title('Polynomial Regression (Degree {})'.format(degree))
plt.legend()
plt.show()
position_level = 6.5
position_level_poly = poly_features.transform([[position_level]])
predicted_salary = poly_reg.predict(position_level_poly)
print(f'Predicted Salary for Position Level {position_level}: ${predicted_salary[0]}')