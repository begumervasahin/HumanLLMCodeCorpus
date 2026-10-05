
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
experience_levels = dataset['Level'].values.reshape(-1, 1)
salaries = dataset['Salary'].values
linear_reg = LinearRegression()
linear_reg.fit(experience_levels, salaries)
poly_features = PolynomialFeatures(degree=4)
experience_levels_poly = poly_features.fit_transform(experience_levels)
poly_reg = LinearRegression()
poly_reg.fit(experience_levels_poly, salaries)
plt.scatter(experience_levels, salaries, color='red')
plt.plot(experience_levels, linear_reg.predict(experience_levels), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Experience Level')
plt.ylabel('Salary')
plt.show()
experience_levels_grid = np.arange(min(experience_levels), max(experience_levels), 0.1).reshape(-1, 1)
experience_levels_poly_grid = poly_features.transform(experience_levels_grid)
plt.scatter(experience_levels, salaries, color='red')
plt.plot(experience_levels_grid, poly_reg.predict(experience_levels_poly_grid), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Experience Level')
plt.ylabel('Salary')
plt.show()
new_experience_level = 6.5
predicted_salary_linear = linear_reg.predict([[new_experience_level]])[0]
print("Predicted salary using Linear Regression:", predicted_salary_linear)
predicted_salary_poly = poly_reg.predict(poly_features.transform([[new_experience_level]]))[0]
print("Predicted salary using Polynomial Regression:", predicted_salary_poly)