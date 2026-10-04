
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
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
def fonk1(b2, b3, regressor, title, xlabel, ylabel, b8 = None):
    plt.scatter(b2, b3, b9 = 'red')
    if b8:
        plt.plot(b2, regressor.predict(b8(b2)), b9 = 'blue')
    else:
        plt.plot(b2, regressor.predict(b2), b9 = 'blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
fonk1(b2, b3, b4, 'Truth or Bluff (Linear Regression)', 'Position Level', 'Salary')
b10 = np.arange(min(b2), max(b2), 0.01).reshape(-1, 1)
fonk1(b10, b3, b7, 'Truth or Bluff (Polynomial Regression)', 'Position Level', 'Salary', b8 = b5.fit_transform)
b11 = b4.predict(np.array([[6.5]]))
print(f'Linear Regression Prediction for 6.5: {b11[0]}')
b12 = b7.predict(b5.fit_transform(np.array([[6.5]])))
print(f'Polynomial Regression Prediction for 6.5: {b12[0]}')