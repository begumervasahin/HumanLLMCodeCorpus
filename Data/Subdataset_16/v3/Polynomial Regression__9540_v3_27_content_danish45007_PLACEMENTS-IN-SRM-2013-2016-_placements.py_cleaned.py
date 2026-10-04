import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_excel('placements.xlsx')
b2 = b1.iloc[:, 2:3].values
b3 = b1.iloc[:, 3].values
def fonk1(b2, b3):
    b4 = LinearRegression()
    b4.fit(b2, b3)
    return b4
b4 = fonk1(b2, b3)
def fonk2(b2, b3, b5 = 4):
    b6 = PolynomialFeatures(b5=b5)
    b7 = b6.fit_transform(b2)
    b8 = LinearRegression()
    b8.fit(b7, b3)
    return b6, b8
b6, b8 = fonk2(b2, b3)
def fonk3(b2, b3, regressor):
    plt.scatter(b2, b3, b9 = 'red', label='Actual Data')
    plt.plot(b2, regressor.predict(b2), b9 = 'blue', label='Linear Regression')
    plt.title('Placement Record (Linear Regression)')
    plt.xlabel('Number of Students Placed')
    plt.ylabel('Year')
    plt.legend()
    plt.show()
fonk3(b2, b3, b4)
def fonk4(b2, b3, poly_features, poly_regressor):
    plt.scatter(b2, b3, b9 = 'red', label='Actual Data')
    plt.plot(b2, poly_regressor.predict(poly_features.fit_transform(b2)), b9 = 'blue', label='Polynomial Regression')
    plt.title('Placement Record (Polynomial Regression)')
    plt.xlabel('Number of Students Placed')
    plt.ylabel('Year')
    plt.legend()
    plt.show()
fonk4(b2, b3, b6, b8)
def fonk5(b2, b3, poly_features, poly_regressor):
    b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
    plt.scatter(b2, b3, b9 = 'red', label='Actual Data')
    plt.plot(b10, poly_regressor.predict(poly_features.fit_transform(b10)), b9 = 'blue', label='Polynomial Regression (Smooth)')
    plt.title('Placement Record (Polynomial Regression - High Resolution)')
    plt.xlabel('Number of Students Placed')
    plt.ylabel('Year')
    plt.legend()
    plt.show()
fonk5(b2, b3, b6, b8)