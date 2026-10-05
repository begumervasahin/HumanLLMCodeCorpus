
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
linear_reg = LinearRegression()
linear_reg.fit(X, y)
y_pred_linear = linear_reg.predict(X)
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_reg = LinearRegression()
polynomial_reg.fit(X_poly, y)
y_pred_poly = polynomial_reg.predict(X_poly)
plt.scatter(X, y, color='red', label='Actual data')
plt.plot(X, y_pred_linear, color='blue', label='Linear Regression')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.scatter(X, y, color='red', label='Actual data')
plt.plot(X, y_pred_poly, color='blue', label='Polynomial Regression')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()