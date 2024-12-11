import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
a1 = 1
b4 = float('inf')
for degree in range(1, 11):
    b5 = PolynomialFeatures(degree=degree)
    b6 = b5.fit_transform(b2)
    b7 = LinearRegression()
    b7.fit(b6, b3)
    b8 = b7.predict(b6)
    b9 = np.mean((b8 - b3) ** 2)
    if b9 < b4:
        b4 = b9
        a1 = degree
b5 = PolynomialFeatures(degree=a1)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b10 = 'red', label='Actual data')
plt.plot(b2, b7.predict(b6), b10 = 'blue', label='Polynomial Regression')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.legend()
plt.show()