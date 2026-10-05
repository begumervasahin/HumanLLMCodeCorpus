
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('/home/chrx/Downloads/Machine-Learning-A-Z-New/Machine Learning A-Z New/Part 2 - Regression/Section 6 - Polynomial Regression/Position_Salaries.csv')
X = data.iloc[:, 1:2].values
Y = data.iloc[:, 2:3].values
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(X, Y)
Y_pred = lin_reg_1.predict(X)
from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=8)
X_poly = poly_features.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y)
plt.scatter(X, Y, color='red')
plt.plot(X, Y_pred, color='blue')
plt.title('Linear Regression Model')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, Y, color='red')
plt.plot(X, lin_reg_2.predict(poly_features.transform(X)), color='blue')
plt.title('Polynomial Regression Model')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
new_level = np.array([6.5]).reshape(1, -1)
linear_pred = lin_reg_1.predict(new_level)
poly_pred = lin_reg_2.predict(poly_features.transform(new_level))
print("Predicted salary using Linear Regression:", linear_pred)
print("Predicted salary using Polynomial Regression:", poly_pred)