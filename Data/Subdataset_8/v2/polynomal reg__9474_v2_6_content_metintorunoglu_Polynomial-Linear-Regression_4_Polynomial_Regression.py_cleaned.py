
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
y_pred_linear = linear_regressor.predict(X)
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_poly, y)
y_pred_poly = polynomial_regressor.predict(X_poly)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X, y, color='red')
plt.plot(X, y_pred_linear, color='blue')
plt.title('Truth or Bluf (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.subplot(1, 2, 2)
plt.scatter(X, y, color='red')
plt.plot(X, y_pred_poly, color='blue')
plt.title('Truth or Bluf (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()