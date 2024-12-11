
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
from sklearn.linear_model import LinearRegression
b4 = LinearRegression()
b4.fit(b2, b3)
from sklearn.preprocessing import PolynomialFeatures
b5 = PolynomialFeatures(degree=2)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b4.predict(b2), b8 = 'blue')
plt.title('Truth or Bluff (Linear Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b7.predict(b5.fit_transform(b2)), b8 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
b9 = b4.predict([[6.5]])
b10 = b7.predict(b5.fit_transform([[6.5]]))
print("Predicted Salary using Linear Regression:", b9)
print("Predicted Salary using Polynomial Regression:", b10)