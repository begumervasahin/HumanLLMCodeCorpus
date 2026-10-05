
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = b4.predict(b2)
b6 = PolynomialFeatures(degree=4)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
b9 = b8.predict(b7)
plt.scatter(b2, b3, b10 = 'red', label='Actual data')
plt.plot(b2, b5, b10 = 'blue', label='Linear Regression')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.scatter(b2, b3, b10 = 'red', label='Actual data')
plt.plot(b2, b9, b10 = 'blue', label='Polynomial Regression')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()