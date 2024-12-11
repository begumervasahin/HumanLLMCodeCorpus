import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.b12 import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b11):
    b1 = b11.iloc[:, 1:2].values
    b2 = b11.iloc[:, 2].values
    return b1, b2
def fonk3(b1, b2):
    b3 = LinearRegression()
    b3.fit(b1, b2)
    return b3
def fonk4(b1, b2, b4 = 4):
    b5 = PolynomialFeatures(b4=b4)
    b6 = b5.fit_transform(b1)
    b3 = LinearRegression()
    b3.fit(b6, b2)
    return b3, b5
def fonk5(b1, b2, b3):
    plt.scatter(b1, b2, b7 = 'red')
    plt.plot(b1, b3.predict(b1), b7 = 'blue')
    plt.title('Linear Regression Results')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.grid()
    plt.show()
def fonk6(b1, b2, b3, b5):
    plt.scatter(b1, b2, b7 = 'red')
    b8 = np.arange(min(b1), max(b1), 0.1).reshape(-1, 1)
    plt.plot(b8, b3.predict(b5.transform(b8)), b7 = 'green')
    plt.title('Polynomial Regression Results')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.grid()
    plt.show()
def fonk7(a1, b12, poly_model, b5):
    b9 = b12.predict([[a1]])[0]
    b10 = poly_model.predict(b5.transform([[a1]]))[0]
    return b9, b10
b11 = fonk1('Position_Salaries.csv')
b1, b2 = fonk2(b11)
b12 = fonk3(b1, b2)
poly_model, b5 = fonk4(b1, b2, b4=4)
fonk5(b1, b2, b12)
fonk6(b1, b2, poly_model, b5)
a1 = 6.5
b9, b10 = fonk7(a1, b12, poly_model, b5)
print(f"Linear Regression Prediction for Position Level {a1}: {b9}")
print(f"Polynomial Regression Prediction for Position Level {a1}: {b10}")