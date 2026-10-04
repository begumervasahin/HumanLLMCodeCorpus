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
a1 = 4
b5 = PolynomialFeatures(degree=a1)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
def fonk1(title, regressor, b2, b3, b5 = None, b9=None):
    plt.scatter(b2, b3, b8 = 'red')
    if b9 is not None:
        plt.plot(b9, regressor.predict(b5.fit_transform(b9)), b8 = 'blue')
    else:
        plt.plot(b2, regressor.predict(b2), b8 = 'blue')
    plt.title(title)
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
fonk1('Truth or Bluff (Linear Regression)', b4, b2, b3)
fonk1('Truth or Bluff (Polynomial Regression)', b7, b2, b3, b5)
b9 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
fonk1('Truth or Bluff (Polynomial Regression - Smooth Curve)', b7, b2, b3, b5, b9)
b10 = b4.predict([[6.5]])
print(f"Linear Regression Prediction for level 6.5: {b10[0]}")
b11 = b7.predict(b5.fit_transform([[6.5]]))
print(f"Polynomial Regression Prediction for level 6.5: {b11[0]}")