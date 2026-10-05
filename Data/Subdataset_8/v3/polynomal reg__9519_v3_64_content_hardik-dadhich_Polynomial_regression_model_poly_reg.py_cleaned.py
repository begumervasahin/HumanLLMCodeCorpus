
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
polynomial_features = PolynomialFeatures(degree=2)
X_poly = polynomial_features.fit_transform(X)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X, linear_regressor.predict(X), color='blue', label='Linear Regression')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X, polynomial_regressor.predict(X_poly), color='blue', label='Polynomial Regression')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
predicted_salary_linear = linear_regressor.predict([[6.5]])[0]
print("Predicted salary with Linear Regression for position level 6.5:", predicted_salary_linear)
predicted_salary_poly = polynomial_regressor.predict(polynomial_features.transform([[6.5]]))[0]
print("Predicted salary with Polynomial Regression for position level 6.5:", predicted_salary_poly)