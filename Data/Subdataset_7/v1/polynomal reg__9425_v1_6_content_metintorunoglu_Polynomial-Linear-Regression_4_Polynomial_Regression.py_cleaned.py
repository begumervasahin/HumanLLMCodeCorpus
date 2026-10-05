import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = b4.predict(b2)
b6 = PolynomialFeatures(degree=4)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
b9 = b8.predict(b7)
plt.figure(b10 = (10, 5))
plt.subplot(1, 2, 1)
plt.scatter(b2, b3, b11 = 'red')
plt.plot(b2, b5, b11 = 'blue')
plt.title('Truth or Bluf (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.subplot(1, 2, 2)
plt.scatter(b2, b3, b11 = 'red')
plt.plot(b2, b9, b11 = 'blue')
plt.title('Truth or Bluf (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()