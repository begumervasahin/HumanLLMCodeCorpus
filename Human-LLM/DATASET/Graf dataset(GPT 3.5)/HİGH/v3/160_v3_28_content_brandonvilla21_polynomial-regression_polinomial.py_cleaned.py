import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b10):
    b1 = b10.iloc[:, 0:1].values
    b2 = b10.iloc[:, 1:2].values
    return b1, b2
def fonk3(b1, b2, b3 = 0.2, random_state=0):
    return train_test_split(b1, b2, b3 = b3, random_state=random_state)
def fonk4(b1, b2):
    b4 = LinearRegression()
    b4.fit(b1, b2)
    return b4
def fonk5(b1, b2, b5 = 2):
    b6 = PolynomialFeatures(b5=b5)
    b7 = b6.fit_transform(b1)
    b8 = LinearRegression()
    b8.fit(b7, b2)
    return b8, b6
def fonk6(b1, b2, regression_model, title):
    plt.scatter(b1, b2, b9 = 'red')
    plt.plot(b1, regression_model.predict(b1), b9 = 'blue')
    plt.title(title)
    plt.xlabel('Days of Year 1998')
    plt.ylabel('CO Values in AGU')
    plt.show()
b10 = fonk1('HORA08_AGU_CO_1998-01-01_1998-12-31_1521371719602.csv')
b1, b2 = fonk2(b10)
X_train, X_test, y_train, b11 = fonk3(b1, b2)
b4 = fonk4(X_train, y_train)
b8, b6 = fonk5(X_train, y_train)
fonk6(b1, b2, b4, 'Linear Regression')
fonk6(b1, b2, b8, 'Polynomial Regression (Degree 2)')