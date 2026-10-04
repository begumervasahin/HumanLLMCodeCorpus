import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
def fonk1(b2, b3):
    b4 = LinearRegression()
    b4.fit(b2, b3)
    plt.scatter(b2, b3, b5 = 'red')
    plt.plot(b2, b4.predict(b2), b5 = 'blue')
    plt.title('Truth or Bluff (Linear Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    return b4
def fonk2(b2, b3, b6 = 4):
    b7 = PolynomialFeatures(b6=b6)
    b8 = b7.fit_transform(b2)
    b9 = LinearRegression()
    b9.fit(b8, b3)
    plt.scatter(b2, b3, b5 = 'red')
    plt.plot(b2, b9.predict(b8), b5 = 'blue')
    plt.title(f'Truth or Bluff (Polynomial Regression - Degree {b6})')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
    plt.scatter(b2, b3, b5 = 'red')
    plt.plot(b10, b9.predict(b7.fit_transform(b10)), b5 = 'blue')
    plt.title(f'Truth or Bluff (Polynomial Regression - Degree {b6}, High Resolution)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    return b9, b7
b4 = fonk1(b2, b3)
b9, b7 = fonk2(b2, b3, b6=4)
def fonk3(b2, b4, b9, b7, b11 = 6.5):
    b12 = b4.predict([[b11]])
    b13 = b9.predict(b7.fit_transform([[b11]]))
    print(f'Linear Regression prediction for position level {b11}: {b12[0]}')
    print(f'Polynomial Regression prediction for position level {b11}: {b13[0]}')
fonk3(b2, b4, b9, b7)