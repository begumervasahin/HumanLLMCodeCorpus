
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
from sklearn.preprocessing import PolynomialFeatures
degree = 4
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X, linear_regressor.predict(X), color='blue', label='Linear Regression')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X_grid, poly_regressor.predict(poly_features.fit_transform(X_grid)), color='blue', label='Polynomial Regression')
plt.title(f'Truth or Bluff (Polynomial Regression - Degree {degree})')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
position_level = 6.5
linear_pred = linear_regressor.predict(np.array([[position_level]]))[0]
poly_pred = poly_regressor.predict(poly_features.fit_transform(np.array([[position_level]])))[0]
print(f'Predicted salary (Linear Regression) for position level {position_level}: {linear_pred}')
print(f'Predicted salary (Polynomial Regression) for position level {position_level}: {poly_pred}')