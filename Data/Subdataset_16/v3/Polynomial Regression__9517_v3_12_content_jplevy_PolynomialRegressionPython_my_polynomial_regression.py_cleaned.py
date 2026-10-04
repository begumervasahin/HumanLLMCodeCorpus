import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def fonk1(filename):
    return pd.read_csv(filename)
def fonk2(b8, b9):
    b1 = LinearRegression()
    b1.fit(b8, b9)
    return b1
def fonk3(b8, b9, a1):
    b2 = PolynomialFeatures(a1=a1)
    b3 = b2.fit_transform(b8)
    b1 = LinearRegression()
    b1.fit(b3, b9)
    return b1, b2
def fonk4(b8, b9, model, title, xlabel, ylabel, b2 = None):
    plt.scatter(b8, b9, b4 = 'red', label='Actual')
    if b2 is not None:
        b5 = np.arange(min(b8), max(b8), 0.01).reshape(-1, 1)
        plt.plot(b5, model.fonk5(b2.fit_transform(b5)), b4 = 'blue', label='Model')
    else:
        plt.plot(b8, model.fonk5(b8), b4 = 'blue', label='Model')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
def fonk5(model, a2, b2 = None):
    if b2 is not None:
        return model.fonk5(b2.fit_transform([[a2]]))[0]
    else:
        return model.fonk5([[a2]])[0]
if b6 = = "__main__":
    b7 = fonk1('Position_Salaries.csv')
    b8 = b7.iloc[:, 1:2].values
    b9 = b7.iloc[:, 2].values
    b10 = fonk2(b8, b9)
    a1 = 4
    polynomial_regressor, b2 = fonk3(b8, b9, a1)
    fonk4(b8, b9, b10, 'Truth or Bluff (Linear Regression)', 'Position Level', 'Salary')
    fonk4(b8, b9, polynomial_regressor, f'Truth or Bluff (Polynomial Regression, b11 = {a1})', 'Position Level', 'Salary', b2)
    a2 = 6.5
    b12 = fonk5(b10, a2)
    b13 = fonk5(polynomial_regressor, a2, b2)
    print(f"Linear Regression Prediction for position level {a2}: {b12}")
    print(f"Polynomial Regression Prediction for position level {a2}: {b13}")