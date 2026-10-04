import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_regressor.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, poly_regressor.predict(X_poly), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, poly_regressor.predict(poly_features.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression - Smooth Curve)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
linear_prediction = linear_regressor.predict([[6.5]])
print(f"Linear Regression Prediction for level 6.5: {linear_prediction[0]}")
poly_prediction = poly_regressor.predict(poly_features.fit_transform([[6.5]]))
print(f"Polynomial Regression Prediction for level 6.5: {poly_prediction[0]}")