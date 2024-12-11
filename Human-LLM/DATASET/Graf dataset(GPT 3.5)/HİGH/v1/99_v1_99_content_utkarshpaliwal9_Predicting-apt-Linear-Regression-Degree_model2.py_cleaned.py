import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
a1 = 1
b4 = float('inf')
a2 = 1
while a1 <= 10:
    b5 = PolynomialFeatures(degree=a1)
    b6 = b5.fit_transform(b2)
    b5.fit(b6, b3)
    b7 = LinearRegression()
    b7.fit(b6, b3)
    b8 = b7.predict(b6)
    b9 = np.mean((b8 - b3) ** 2)
    if b9 < b4:
        b4 = b9
        a2 = a1
    a1 += 1
b5 = PolynomialFeatures(degree=a2)
b10 = b5.fit_transform(b2)
b5.fit(b10, b3)
b7 = LinearRegression()
b7.fit(b10, b3)
plt.scatter(b2, b3, b11 = 'red')
plt.plot(b2, b7.predict(b5.fit_transform(b2)), b11 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()