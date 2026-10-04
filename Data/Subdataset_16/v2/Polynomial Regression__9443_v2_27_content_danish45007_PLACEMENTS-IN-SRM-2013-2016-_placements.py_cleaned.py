import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_excel('placements.xlsx')
b2 = b1.iloc[:, 2:3].values
b3 = b1.iloc[:, 3].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red', label='Actual Data')
plt.plot(b2, b4.predict(b2), b8 = 'blue', label='Linear Regression')
plt.title('Placement Record (Linear Regression)')
plt.xlabel('Number of Students Placed')
plt.ylabel('Year')
plt.legend()
plt.show()
plt.scatter(b2, b3, b8 = 'red', label='Actual Data')
plt.plot(b2, b7.predict(b6), b8 = 'blue', label='Polynomial Regression')
plt.title('Placement Record (Polynomial Regression)')
plt.xlabel('Number of Students Placed')
plt.ylabel('Year')
plt.legend()
plt.show()
b9 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.scatter(b2, b3, b8 = 'red', label='Actual Data')
plt.plot(b9, b7.predict(b5.fit_transform(b9)), b8 = 'blue', label='Polynomial Regression (Smooth)')
plt.title('Placement Record (Polynomial Regression - High Resolution)')
plt.xlabel('Number of Students Placed')
plt.ylabel('Year')
plt.legend()
plt.show()