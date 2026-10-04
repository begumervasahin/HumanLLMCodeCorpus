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
b5 = PolynomialFeatures(degree=2)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
b8 = PolynomialFeatures(degree=3)
b9 = b8.fit_transform(b2)
b10 = LinearRegression()
b10.fit(b9, b3)
b11 = PolynomialFeatures(degree=4)
b12 = b11.fit_transform(b2)
b13 = LinearRegression()
b13.fit(b12, b3)
def fonk1(b2, b3, model, b14 = None, b17='Truth or Bluff', degree=None):
    plt.scatter(b2, b3, b15 = 'red')
    if b14:
        b16 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
        plt.plot(b16, model.predict(b14.fit_transform(b16)), b15 = 'blue')
    else:
        plt.plot(b2, model.predict(b2), b15 = 'blue')
    plt.b17(b17 + (f" (degree {degree})" if degree else ""))
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
fonk1(b2, b3, b4, b17 = 'Linear Regression')
fonk1(b2, b3, b7, b5, b17 = 'Polynomial Regression', degree=2)
fonk1(b2, b3, b10, b8, b17 = 'Polynomial Regression', degree=3)
fonk1(b2, b3, b13, b11, b17 = 'Polynomial Regression', degree=4)
b18 = b4.predict([[6.2]])
b19 = b13.predict(b11.fit_transform([[6.2]]))
print("Linear Regression Prediction for 6.2:", b18)
print("Polynomial Regression Prediction for 6.2:", b19)
print("Linear Regression Coefficients:", b4.coef_, "Intercept:", b4.intercept_)
print("Polynomial Regression Coefficients (degree 4):", b13.coef_, "Intercept:", b13.intercept_)