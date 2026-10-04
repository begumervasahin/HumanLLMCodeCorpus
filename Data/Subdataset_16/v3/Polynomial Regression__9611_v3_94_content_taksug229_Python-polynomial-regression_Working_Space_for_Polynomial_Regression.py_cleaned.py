import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
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
    b4 = LinearRegression()
    b4.fit(b6, b3)
    return b5, b4
def fonk4(b2, b3, b13, b14, b5):
    plt.figure(b7 = (14, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(b2, b3, b8 = 'red', label='Actual Data')
    plt.plot(b2, b13.predict(b2), b8 = 'blue', label='Linear Prediction')
    plt.title('Linear Regression')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.scatter(b2, b3, b8 = 'red', label='Actual Data')
    plt.plot(b2, b14.predict(b5.transform(b2)), b8 = 'blue', label='Polynomial Prediction')
    plt.title('Polynomial Regression')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.legend()
    plt.tight_layout()
    plt.show()
    b9 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
    plt.scatter(b2, b3, b8 = 'red', label='Actual Data')
    plt.plot(b9, b14.predict(b5.transform(b9)), b8 = 'blue', label='Polynomial Prediction')
    plt.title('Polynomial Regression (Smoother Curve)')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
def fonk5(b13, b14, b5, a1):
    b10 = b13.predict([[a1]])
    b11 = b14.predict(b5.transform([[a1]]))
    return b10[0], b11[0]
if b12 = = "__main__":
    b2, b3 = fonk1('Position_Salaries.csv')
    b13 = fonk2(b2, b3)
    b5, b14 = fonk3(b2, b3, degree=4)
    fonk4(b2, b3, b13, b14, b5)
    a1 = 6.5
    b10, b11 = fonk5(b13, b14, b5, a1)
    print(f"Linear Regression Prediction for position a1 {a1}: {b10}")
    print(f"Polynomial Regression Prediction for position a1 {a1}: {b11}")