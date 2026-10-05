
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv('/home/chrx/Downloads/Machine-Learning-A-Z-New/Machine Learning A-Z New/Part 2 - Regression/Section 6 - Polynomial Regression/Position_Salaries.csv')
X = data['Level'].values.reshape(-1, 1)
Y = data['Salary'].values
linear_model = LinearRegression()
linear_model.fit(X, Y)
Y_pred_linear = linear_model.predict(X)
poly_features = PolynomialFeatures(degree=8)
X_poly = poly_features.fit_transform(X)
polynomial_model = LinearRegression()
polynomial_model.fit(X_poly, Y)
Y_pred_poly = polynomial_model.predict(X_poly)
plt.scatter(X, Y, color='red', label='Actual Data')
plt.plot(X, Y_pred_linear, color='blue', label='Linear Regression')
plt.title('Linear Regression Model')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.scatter(X, Y, color='red', label='Actual Data')
plt.plot(X, Y_pred_poly, color='blue', label='Polynomial Regression')
plt.title('Polynomial Regression Model')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
new_level = np.array([6.5]).reshape(1, -1)
linear_pred = linear_model.predict(new_level)
poly_pred = polynomial_model.predict(poly_features.transform(new_level))
print("Predicted salary using Linear Regression:", linear_pred)
print("Predicted salary using Polynomial Regression:", poly_pred)