
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_pred = lin_reg.predict(X)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)
y_pred_2 = lin_reg2.predict(X_poly)
plt.scatter(X, y, color='red')
plt.plot(X, y_pred, color='blue')
plt.title('Truth or Bluf (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, y_pred_2, color='blue')
plt.title('Truth or Bluf (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()