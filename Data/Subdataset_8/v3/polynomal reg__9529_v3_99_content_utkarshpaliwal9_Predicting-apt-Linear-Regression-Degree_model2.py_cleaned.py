import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
best_degree = 1
min_mse = float('inf')
for degree in range(1, 11):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    polynomial_regression = LinearRegression()
    polynomial_regression.fit(X_poly, y)
    y_pred = polynomial_regression.predict(X_poly)
    mse = np.mean((y_pred - y) ** 2)
    if mse < min_mse:
        min_mse = mse
        best_degree = degree
poly_features = PolynomialFeatures(degree=best_degree)
X_poly = poly_features.fit_transform(X)
polynomial_regression = LinearRegression()
polynomial_regression.fit(X_poly, y)
plt.scatter(X, y, color='red', label='Actual data')
plt.plot(X, polynomial_regression.predict(X_poly), color='blue', label='Polynomial Regression')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.legend()
plt.show()