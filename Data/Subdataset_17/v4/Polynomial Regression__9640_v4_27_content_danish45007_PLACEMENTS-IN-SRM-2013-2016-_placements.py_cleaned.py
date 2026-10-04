import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_excel('placements.xlsx')
X = dataset.iloc[:, 2:3].values
y = dataset.iloc[:, 3].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_regressor.predict(X), color='blue')
plt.title('PLACEMENT RECORD (Linear Regression)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, poly_regressor.predict(poly_features.transform(X)), color='blue')
plt.title('PLACEMENT RECORD (Polynomial Regression)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, poly_regressor.predict(poly_features.transform(X_grid)), color='blue')
plt.title('PLACEMENT RECORD (Polynomial Regression)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
plt.show()