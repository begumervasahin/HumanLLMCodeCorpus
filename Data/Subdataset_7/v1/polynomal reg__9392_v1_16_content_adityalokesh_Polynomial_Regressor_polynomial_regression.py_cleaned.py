import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('/home/chrx/Downloads/Machine-Learning-A-Z-New/Machine Learning A-Z New/Part 2 - Regression/Section 6 - Polynomial Regression/Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2:3].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = b4.predict(b2)
b6 = PolynomialFeatures(degree=8)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b5, b9 = 'blue')
plt.title('Regression-LinearModel')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b8.predict(b6.fit_transform(b2)), b9 = 'blue')
plt.title('Regression-PolynomialModel')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
b10 = np.array([6.5]).reshape(1, -1)
b11 = b4.predict(b10)
print("Linear Regression Prediction:", b11)
b12 = b8.predict(b6.fit_transform(b10))
print("Polynomial Regression Prediction:", b12)