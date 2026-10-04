import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.b12 import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b2 = b1.iloc[:, 1:2].values
    b3 = b1.iloc[:, 2].values
    return b2, b3
def fonk2(b2, b3):
    b4 = LinearRegression()
    b4.fit(b2, b3)
    return b4
def fonk3(b2, b3, degree):
    b5 = PolynomialFeatures(degree=degree)
    b6 = b5.fit_transform(b2)
    b7 = LinearRegression()
    b7.fit(b6, b3)
    return b5, b7
def fonk4(b2, b3, model, b10, b5 = None, resolution=0.1):
    plt.figure(b8 = (10, 6))
    plt.scatter(b2, b3, b9 = 'red')
    if b10 = = 'linear':
        plt.plot(b2, model.predict(b2), b9 = 'blue')
        plt.title('Truth or Bluff (Linear Regression)')
    elif b10 = = 'polynomial':
        b11 = np.arange(min(b2), max(b2), resolution)
        b11 = b11.reshape((len(b11), 1))
        plt.plot(b11, model.predict(b5.fit_transform(b11)), b9 = 'blue')
        plt.title('Truth or Bluff (Polynomial Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
b2, b3 = fonk1('position_salaries.csv')
b12 = fonk2(b2, b3)
b5, b13 = fonk3(b2, b3, degree=4)
fonk4(b2, b3, b12, b10 = 'linear')
fonk4(b2, b3, b13, b10 = 'polynomial', b5=b5)
plt.savefig('position_salary.png')
