
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
linear_reg = LinearRegression()
linear_reg.fit(X, y)
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_reg.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, poly_reg.predict(X_poly), color='blue')
plt.title('Truth or Bluff (Polynomial Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
level_to_predict = 6.5
linear_prediction = linear_reg.predict([[level_to_predict]])
polynomial_prediction = poly_reg.predict(poly_features.transform([[level_to_predict]]))
print("Predicted Salary using Linear Regression:", linear_prediction)
print("Predicted Salary using Polynomial Regression:", polynomial_prediction)