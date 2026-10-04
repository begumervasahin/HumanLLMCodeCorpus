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
b5 = PolynomialFeatures(degree = 4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.figure(b8 = (10, 6))
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b4.predict(b2), b9 = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
plt.figure(b8 = (10, 6))
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b7.predict(b5.fit_transform(b2)), b9 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
b10 = np.arange(min(b2), max(b2), 0.1)
b10 = b10.reshape((len(b10), 1))
plt.figure(b8 = (10, 6))
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b10, b7.predict(b5.fit_transform(b10)), b9 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
plt.savefig('position_salary.png')
