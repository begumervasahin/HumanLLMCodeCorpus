
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
best_degree = 1
min_mse = float('inf')
for degree in range(1, 11):
    poly_reg = PolynomialFeatures(degree=degree)
    X_poly_temp = poly_reg.fit_transform(X)
    poly_reg.fit(X_poly_temp, y)
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly_temp, y)
    y_pred = lin_reg.predict(X_poly_temp)
    mse = np.mean((y_pred - y) ** 2)
    if mse < min_mse:
        min_mse = mse
        best_degree = degree
poly_reg = PolynomialFeatures(degree=best_degree)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()