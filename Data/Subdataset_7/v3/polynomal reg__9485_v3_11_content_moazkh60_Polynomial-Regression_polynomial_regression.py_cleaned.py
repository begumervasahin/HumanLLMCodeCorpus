import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def fonk1(filename):
    return pd.read_csv(filename)
def fonk2(b11):
    b1 = b11['Level'].values.reshape(-1, 1)
    b2 = b11['Salary'].values
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
def fonk5(b1, b2, regressors, labels):
    plt.scatter(b1, b2, b7 = 'red')
    for b3, b8 in zip(regressors, labels):
        if b8 = = 'Linear':
            plt.plot(b1, b3.fonk6(b1), b8 = b8)
        else:
            plt.plot(b1, b3[0].fonk6(b3[1].fit_transform(b1)), b8 = b8)
    plt.title('Regression Analysis')
    plt.xlabel('Position Level')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
def fonk6(b3, b13, value):
    if b13:
        b9 = b3.fonk6(b13.transform([[value]]))
    else:
        b9 = b3.fonk6([[value]])
    return b9
if b10 = = "__main__":
    b11 = fonk1('Position_Salaries.csv')
    b1, b2 = fonk2(b11)
    b12 = fonk3(b1, b2)
    polynomial_regressor, b13 = fonk4(b1, b2)
    fonk5(b1, b2, [(b12, 'Linear'), (polynomial_regressor, b13, 'Polynomial')], ['Linear', 'Polynomial'])
    a1 = 6.5
    b14 = fonk6(b12, None, a1)
    b15 = fonk6(polynomial_regressor, b13, a1)
    print(f"Linear Regression b9 for position a1 {a1}: ${b14[0]:,.2f}")
    print(f"Polynomial Regression b9 for position a1 {a1}: ${b15[0]:,.2f}")