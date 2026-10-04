import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = [2, 3, 4]
for b11 in b5:
    b6 = PolynomialFeatures(b11=b11)
    b7 = b6.fit_transform(b2)
    b8 = LinearRegression()
    b8.fit(b7, b3)
    plt.scatter(b2, b3, b9 = 'red')
    b10 = np.arange(min(b2), max(b2), 0.1)
    b10 = b10.reshape((len(b10)), 1)
    plt.plot(b10, b8.predict(b6.fit_transform(b10)), b9 = 'blue')
    plt.title(f'Truth or Bluff (Polynomial Regression b11 = {b11})')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
b12 = b4.predict([[6.2]])
print(f'Linear Regression prediction for position level 6.2: {b12[0]}')
b6 = PolynomialFeatures(b11=4)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
b13 = b8.predict(b6.fit_transform([[6.2]]))
print(f'Polynomial Regression (b11 = 4) prediction for position level 6.2: {b13[0]}')
print(f'Linear Regression intercept: {b4.intercept_}')
print(f'Linear Regression coefficients: {b4.coef_}')
print(f'Polynomial Regression (b11 = 4) intercept: {b8.intercept_}')
print(f'Polynomial Regression (b11 = 4) coefficients: {b8.coef_}')