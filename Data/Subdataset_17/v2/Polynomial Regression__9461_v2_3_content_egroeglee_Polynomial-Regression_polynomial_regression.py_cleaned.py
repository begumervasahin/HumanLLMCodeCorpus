import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
polynomial_features = PolynomialFeatures(degree=4)
x_poly = polynomial_features.fit_transform(x)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(x_poly, y)
plt.scatter(x, y, color='red')
plt.plot(x, linear_regressor.predict(x), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color='red')
plt.plot(x_grid, polynomial_regressor.predict(polynomial_features.fit_transform(x_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
linear_prediction = linear_regressor.predict([[6.5]])
print(f"Linear Regression Prediction for position level 6.5: {linear_prediction[0]}")
poly_prediction = polynomial_regressor.predict(polynomial_features.fit_transform([[6.5]]))
print(f"Polynomial Regression Prediction for position level 6.5: {poly_prediction[0]}")