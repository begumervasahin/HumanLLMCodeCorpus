
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
from sklearn.linear_model import LinearRegression
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = b4.predict(b2)
from sklearn.preprocessing import PolynomialFeatures
b6 = PolynomialFeatures(degree=4)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
b9 = b8.predict(b7)
plt.scatter(b2, b3, b10 = 'red')
plt.plot(b2, b5, b10 = 'blue')
plt.title('Truth or Bluf (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(b2, b3, b10 = 'red')
plt.plot(b2, b9, b10 = 'blue')
plt.title('Truth or Bluf (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()