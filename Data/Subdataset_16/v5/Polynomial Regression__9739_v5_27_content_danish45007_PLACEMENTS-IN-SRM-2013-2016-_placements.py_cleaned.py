import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_excel('placements.xlsx')
b2 = b1.iloc[:, 2:3].values
b3 = b1.iloc[:, 3].values
b4 = LinearRegression()
b4.fit(b2, b3)
a1 = 4
b5 = PolynomialFeatures(a1=a1)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
def fonk1(b2, b3, model, title, xlabel, ylabel, b8 = None):
    plt.scatter(b2, b3, b9 = 'red')
    if b8:
        plt.plot(b2, model.predict(b8(b2)), b9 = 'blue')
    else:
        plt.plot(b2, model.predict(b2), b9 = 'blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
fonk1(b2, b3, b4, 'PLACEMENT RECORD (Linear Regression)', 'NO. of Students placed', 'YEAR')
fonk1(b2, b3, b7, 'PLACEMENT RECORD (Polynomial Regression)', 'NO. of Students placed', 'YEAR', b8 = b5.b8)
b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
fonk1(b10, b3, b7, 'PLACEMENT RECORD (Polynomial Regression - Smooth Curve)', 'NO. of Students placed', 'YEAR', b8 = b5.b8)