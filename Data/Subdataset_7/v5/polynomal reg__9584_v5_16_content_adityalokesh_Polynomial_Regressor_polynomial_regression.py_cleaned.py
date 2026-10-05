
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.b4 import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('/home/chrx/Downloads/Machine-Learning-A-Z-New/Machine Learning A-Z New/Part 2 - Regression/Section 6 - Polynomial Regression/Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = b4.predict(b2)
b6 = PolynomialFeatures(degree=8)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
b9 = b8.predict(b7)
plt.scatter(b2, b3, b10 = 'red', label='Actual Data')
plt.plot(b2, b5, b10 = 'blue', label='Linear Regression')
plt.title('Linear Regression Model')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.scatter(b2, b3, b10 = 'red', label='Actual Data')
plt.plot(b2, b9, b10 = 'blue', label='Polynomial Regression')
plt.title('Polynomial Regression Model')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b11 = np.array([6.5]).reshape(1, -1)
b12 = b4.predict(b11)
b13 = b8.predict(b6.transform(b11))
print("Predicted salary using Linear Regression:", b12)
print("Predicted salary using Polynomial Regression:", b13)