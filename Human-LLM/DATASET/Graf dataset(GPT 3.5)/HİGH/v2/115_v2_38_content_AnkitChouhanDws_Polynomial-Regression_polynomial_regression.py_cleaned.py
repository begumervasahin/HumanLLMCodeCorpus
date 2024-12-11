
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.b4 import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Path To Dataset')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=5)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b4.predict(b2), b8 = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
b9 = np.arange(min(b2), max(b2), 0.1)
b9 = b9.reshape(len(b9), 1)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b9, b7.predict(b5.fit_transform(b9)), b8 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
b10 = float(input('Enter your Experience level for Linear Regression: '))
b11 = b4.predict(np.array([[b10]]))[0]
print("Predicted Salary (Linear Regression):", b11)
b12 = float(input('Enter your Experience level for Polynomial Regression: '))
b13 = b7.predict(b5.fit_transform([[b12]]))[0]
print("Predicted Salary (Polynomial Regression):", b13)