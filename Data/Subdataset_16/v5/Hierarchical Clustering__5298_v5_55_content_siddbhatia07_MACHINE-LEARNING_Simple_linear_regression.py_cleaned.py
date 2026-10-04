import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def fonk1(filepath):
    b1 = pd.read_csv(filepath)
    b2 = b1.iloc[:, :-1].values
    b3 = b1.iloc[:, 1].values
    return b2, b3
def fonk2(b2, b3, b4 = 1/3, random_state=0):
    return train_test_split(b2, b3, b4 = b4, random_state=random_state)
def fonk3(X_train, y_train):
    b5 = LinearRegression()
    b5.fit(X_train, y_train)
    return b5
def fonk4(b2, b3, b9, title, xlabel, ylabel):
    plt.figure(b6 = (10, 6))
    plt.scatter(b2, b3, b7 = 'red', label='Actual Data')
    plt.plot(b2, b9.predict(b2), b7 = 'blue', label='Regression Line')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
def fonk5():
    b2, b3 = fonk1('Data.csv')
    X_train, X_test, y_train, b8 = fonk2(b2, b3)
    b9 = fonk3(X_train, y_train)
    fonk4(X_train, y_train, b9, 'Salary vs Experience (Training Set)', 'Years of Experience', 'Salary')
    fonk4(X_test, b8, b9, 'Salary vs Experience (Test Set)', 'Years of Experience', 'Salary')
if b10 = = "__main__":
    fonk5()