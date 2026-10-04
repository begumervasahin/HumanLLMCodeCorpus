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
def fonk1(degree):
    b5 = PolynomialFeatures(degree=degree)
    b6 = b5.fit_transform(b2)
    b7 = LinearRegression()
    b7.fit(b6, b3)
    return b7, b5
poly_regressor2, b8 = fonk1(degree=2)
poly_regressor3, b9 = fonk1(degree=3)
poly_regressor4, b10 = fonk1(degree=4)
def fonk2(b2, b3, model, b11 = None, b14='Truth or Bluff', degree=None):
    plt.scatter(b2, b3, b12 = 'red')
    if b11:
        b13 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
        plt.plot(b13, model.predict(b11.fit_transform(b13)), b12 = 'blue')
        plt.b14(f'{b14} (Polynomial Regression degree {degree})')
    else:
        plt.plot(b2, model.predict(b2), b12 = 'blue')
        plt.b14(f'{b14} (Linear Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
fonk2(b2, b3, b4, b14 = 'Linear Regression')
fonk2(b2, b3, poly_regressor2, b8, b14 = 'Polynomial Regression', degree=2)
fonk2(b2, b3, poly_regressor3, b9, b14 = 'Polynomial Regression', degree=3)
fonk2(b2, b3, poly_regressor4, b10, b14 = 'Polynomial Regression', degree=4)
b15 = b4.predict([[6.2]])
b16 = poly_regressor4.predict(b10.fit_transform([[6.2]]))
print("Linear Regression Prediction for 6.2:", b15)
print("Polynomial Regression Prediction for 6.2:", b16)
print("Linear Regression Coefficients:", b4.coef_, "Intercept:", b4.intercept_)
print("Polynomial Regression Coefficients (degree 4):", poly_regressor4.coef_, "Intercept:", poly_regressor4.intercept_)