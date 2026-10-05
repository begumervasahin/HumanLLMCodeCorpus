
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b4 = 1; b9 = float('Inf'); b10 = 1
while b4<=10:
    b5 = PolynomialFeatures(degree = b4)
    b6 = b5.fit_transform(b2)
    b5.fit(b6, b3)
    b7 = LinearRegression()
    b7.fit(b6, b3)
    b8 = b7.predict(b6)
    a1 = 0
    for i in range(10):
        a1 = a1 + ((b8[i]-b3[i])**2)
    a1/=20
    if a1 < b9:
        b9 = a1
        b10 = b4
    b4+=1
b5 = PolynomialFeatures(degree = b10)
b11 = b5.fit_transform(b2)
b5.fit(b11, b3)
b7 = LinearRegression()
b7.fit(b11, b3)
plt.scatter(b2, b3, b12 = 'red')
plt.plot(b2, b7.predict(b5.fit_transform(b2)), b12 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()