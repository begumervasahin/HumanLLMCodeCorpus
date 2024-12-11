import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:-1].values
b3 = b1.iloc[:, -1].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b4.predict(b2), b8 = 'blue')
plt.title('Level vs Salary (Linear Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b7.predict(b6), b8 = 'blue')
plt.title('Level vs Salary (Polynomial Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
b9 = np.arange(min(b2), max(b2), 0.1)
b9 = b9.reshape((len(b9), 1))
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b9, b7.predict(b5.fit_transform(b9)), b8 = 'blue')
plt.title('Level vs Salary (Polynomial Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
print("Linear Regression prediction for level 6.5:", b4.predict([[6.5]])[0])
print("Polynomial Regression prediction for level 6.5:", b7.predict(b5.fit_transform([[6.5]]))[0])