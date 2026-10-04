import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linReg = LinearRegression()
linReg.fit(x, y)
degrees = [2, 3, 4]
for degree in degrees:
    polyReg = PolynomialFeatures(degree=degree)
    Xpoly = polyReg.fit_transform(x)
    linReg2 = LinearRegression()
    linReg2.fit(Xpoly, y)
    plt.scatter(x, y, color='red')
    Xgrid = np.arange(min(x), max(x), 0.1)
    Xgrid = Xgrid.reshape((len(Xgrid)), 1)
    plt.plot(Xgrid, linReg2.predict(polyReg.fit_transform(Xgrid)), color='blue')
    plt.title(f'Truth or Bluff (Polynomial Regression degree={degree})')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
linear_prediction = linReg.predict([[6.2]])
print(f'Linear Regression prediction for 6.2: {linear_prediction[0]}')
polyReg = PolynomialFeatures(degree=4)
Xpoly = polyReg.fit_transform(x)
linReg2 = LinearRegression()
linReg2.fit(Xpoly, y)
poly_prediction = linReg2.predict(polyReg.fit_transform([[6.2]]))
print(f'Polynomial Regression (degree=4) prediction for 6.2: {poly_prediction[0]}')
print(f'Linear Regression intercept: {linReg.intercept_}')
print(f'Linear Regression coefficients: {linReg.coef_}')
print(f'Polynomial Regression (degree=4) intercept: {linReg2.intercept_}')
print(f'Polynomial Regression (degree=4) coefficients: {linReg2.coef_}')