import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('~/Desktop/Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = LinearRegression()
b4.fit(b2, b3)
a1 = 4
b5 = PolynomialFeatures(a1=a1)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
def fonk1(model, title, b2, b3, b8 = None, high_res=False):
    plt.scatter(b2, b3, b9 = 'red')
    if high_res:
        b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
        if b8:
            plt.plot(b10, model.predict(b8.fit_transform(b10)), b9 = 'blue')
        else:
            plt.plot(b10, model.predict(b10), b9 = 'blue')
    else:
        if b8:
            plt.plot(b2, model.predict(b8.fit_transform(b2)), b9 = 'blue')
        else:
            plt.plot(b2, model.predict(b2), b9 = 'blue')
    plt.title(title)
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
fonk1(b4, 'Truth or Bluff (Linear Regression)', b2, b3)
fonk1(b7, 'Truth or Bluff (Polynomial Regression)', b2, b3, b8 = b5)
fonk1(b7, 'Truth or Bluff (Polynomial Regression - High Resolution)', b2, b3, b8 = b5, high_res=True)
b11 = b4.predict(np.array([[6.5]]))
b12 = b7.predict(b5.fit_transform(np.array([[6.5]])))
print(f'Linear Regression prediction for 6.5: {b11[0]}')
print(f'Polynomial Regression prediction for 6.5: {b12[0]}')