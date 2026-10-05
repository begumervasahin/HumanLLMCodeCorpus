import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
salary_data = pd.read_csv('Position_Salaries.csv')
position_level = salary_data['Level'].values.reshape(-1, 1)
salary = salary_data['Salary'].values
linear_regressor = LinearRegression()
linear_regressor.fit(position_level, salary)
polynomial_features = PolynomialFeatures(degree=4)
position_poly = polynomial_features.fit_transform(position_level)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(position_poly, salary)
plt.scatter(position_level, salary, color='blue')
plt.plot(position_level, linear_regressor.predict(position_level), color='red')
plt.title('Linear regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
plt.scatter(position_level, salary, color='blue')
plt.plot(position_level, polynomial_regressor.predict(polynomial_features.transform(position_level)), color='red')
plt.title('Polynomial regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
position_grid = np.arange(min(position_level), max(position_level), 0.1).reshape(-1, 1)
plt.scatter(position_level, salary, color='blue')
plt.plot(position_grid, polynomial_regressor.predict(polynomial_features.transform(position_grid)), color='red')
plt.title('Polynomial regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()