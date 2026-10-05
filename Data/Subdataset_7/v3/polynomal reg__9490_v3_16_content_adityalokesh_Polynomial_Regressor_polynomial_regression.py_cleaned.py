
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = '/home/chrx/Downloads/Machine-Learning-A-Z-New/Machine Learning A-Z New/Part 2 - Regression/Section 6 - Polynomial Regression/Position_Salaries.csv'
b2 = pd.read_csv(b1)
b3 = b2['Level'].values.reshape(-1, 1)
b4 = b2['Salary'].values.reshape(-1, 1)
b5 = LinearRegression()
b5.fit(b3, b4)
b6 = b5.predict(b3)
a1 = 8
b7 = PolynomialFeatures(degree=a1)
b8 = b7.fit_transform(b3)
b9 = LinearRegression()
b9.fit(b8, b4)
b10 = b9.predict(b8)
plt.scatter(b3, b4, b11 = 'red')
plt.plot(b3, b6, b11 = 'blue')
plt.title('Linear Regression Model')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(b3, b4, b11 = 'red')
plt.plot(b3, b10, b11 = 'blue')
plt.title('Polynomial Regression Model')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
b12 = np.array([6.5]).reshape(1, -1)
b13 = b5.predict(b12)
print("Predicted Salary using Linear Regression:", b13[0][0])
b14 = b7.transform(b12)
b15 = b9.predict(b14)
print("Predicted Salary using Polynomial Regression:", b15[0][0])