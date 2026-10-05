
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Path To Dataset')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_reg_model = LinearRegression()
linear_reg_model.fit(X, y)
poly_features = PolynomialFeatures(degree=5)
X_poly = poly_features.fit_transform(X)
poly_reg_model = LinearRegression()
poly_reg_model.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_reg_model.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, poly_reg_model.predict(poly_features.transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
level = float(input('Enter your Experience level: '))
linear_prediction = linear_reg_model.predict([[level]])[0]
print("Estimated Salary (Linear Regression):", linear_prediction)
level = float(input('Enter your Experience level: '))
poly_prediction = poly_reg_model.predict(poly_features.transform([[level]]))[0]
print("Estimated Salary (Polynomial Regression):", poly_prediction)