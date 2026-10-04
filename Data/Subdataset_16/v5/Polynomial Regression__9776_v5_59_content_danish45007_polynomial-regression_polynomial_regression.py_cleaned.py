import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('position_salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
def fonk1(b2, b3, model, title, b8 = None):
    plt.scatter(b2, b3, b9 = 'red')
    if b8:
        plt.plot(b2, model.predict(b8(b2)), b9 = 'blue')
    else:
        plt.plot(b2, model.predict(b2), b9 = 'blue')
    plt.title(title)
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
fonk1(b2, b3, b4, 'Truth or Bluff (Linear Regression)')
fonk1(b2, b3, b7, 'Truth or Bluff (Polynomial Regression)', b8 = b5.fit_transform)
b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
fonk1(b10, b3, b7, 'Truth or Bluff (Polynomial Regression - High Resolution)', b8 = b5.fit_transform)
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b10, b7.predict(b5.fit_transform(b10)), b9 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.savefig('position_salary.png')
