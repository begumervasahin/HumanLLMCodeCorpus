
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
"""from sklearn.preprocessing import StandardScaler
b4 = StandardScaler()
b5 = b4.fit_transform(b5)
b6 = b4.transform(b6)""
from sklearn.linear_model import LinearRegression
b7 = LinearRegression()
b7.fit(b2,b3)
b8 = b7.predict(b2)
from sklearn.preprocessing import PolynomialFeatures
b9 = PolynomialFeatures(degree=4)
b10 = b9.fit_transform(b2)
b11 = LinearRegression()
b11.fit(b10, b3)
b12 = b11.predict(b10)
ï¿¼
%matplotlib inline
plt.scatter(b2, b3, b13 = 'red')
plt.plot(b2, b8, b13 = 'blue')
plt.title('Truth or Bluf (Linear Regression)')
plt.b14 = ('position level')
plt.b15 = ('salary')
plt.show()
plt.scatter(b2, b3, b13 = 'red')
plt.plot(b2, b12, b13 = 'blue')
plt.title('Truth or Bluf (Polynomial Regression)')
plt.b14 = ('position level')
plt.b15 = ('salary')
plt.show()