import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
salary_data = pd.read_csv('Position_Salaries.csv')
position_levels = salary_data['Level'].values.reshape(-1, 1)
salaries = salary_data['Salary'].values
linear_model = LinearRegression()
linear_model.fit(position_levels, salaries)
polynomial_features = PolynomialFeatures(degree=4)
position_poly = polynomial_features.fit_transform(position_levels)
polynomial_model = LinearRegression()
polynomial_model.fit(position_poly, salaries)
plt.scatter(position_levels, salaries, color='blue')
plt.plot(position_levels, linear_model.predict(position_levels), color='red')
plt.title('Linear regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
plt.scatter(position_levels, salaries, color='blue')
plt.plot(position_levels, polynomial_model.predict(polynomial_features.transform(position_levels)), color='red')
plt.title('Polynomial regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
position_grid = np.arange(min(position_levels), max(position_levels), 0.1).reshape(-1, 1)
plt.scatter(position_levels, salaries, color='blue')
plt.plot(position_grid, polynomial_model.predict(polynomial_features.transform(position_grid)), color='red')
plt.title('Polynomial regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()