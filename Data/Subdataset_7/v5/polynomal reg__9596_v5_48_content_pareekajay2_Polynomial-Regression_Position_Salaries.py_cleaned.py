
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b4.predict(b2), b8 = 'blue')
plt.title('Position Level vs Salary (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b7.predict(b6), b8 = 'blue')
plt.title('Position Level vs Salary (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
b9 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
b10 = b5.transform(b9)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b9, b7.predict(b10), b8 = 'blue')
plt.title('Position Level vs Salary (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
b11 = b4.predict([[6.5]])
print("Predicted Salary using Linear Regression:", b11)
b12 = b7.predict(b5.transform([[6.5]]))
print("Predicted Salary using Polynomial Regression:", b12)