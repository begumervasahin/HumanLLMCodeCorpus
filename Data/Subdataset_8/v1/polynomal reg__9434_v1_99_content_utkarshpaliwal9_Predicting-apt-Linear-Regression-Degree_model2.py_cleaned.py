import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
deg = 1
min_mse = float('inf')
apt_deg = 1
while deg <= 10:
    poly_reg = PolynomialFeatures(degree=deg)
    X_poly_temp = poly_reg.fit_transform(X)
    poly_reg.fit(X_poly_temp, y)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly_temp, y)
    y_pred = lin_reg_2.predict(X_poly_temp)
    mse = np.mean((y_pred - y) ** 2)
    if mse < min_mse:
        min_mse = mse
        apt_deg = deg
    deg += 1
poly_reg = PolynomialFeatures(degree=apt_deg)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()