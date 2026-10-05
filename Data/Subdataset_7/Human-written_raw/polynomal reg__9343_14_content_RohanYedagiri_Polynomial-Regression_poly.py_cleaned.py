import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.read_csv('Position_Salaries.csv')
'''
Level column is like the encoded version of Position column, so we don't need to consider
Position
'''
b2 = b1.drop(['Position','Salary'],axis=1)
b3 = b1.Salary
from sklearn.linear_model import LinearRegression
b4 = LinearRegression()
b4.fit(b2,b3)
from sklearn.preprocessing import PolynomialFeatures
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b6 = pd.DataFrame(b6)
b7 = LinearRegression()
b7.fit(b6,b3)
plt.scatter(b2,b3,b8 = 'red')
plt.plot(b2, b4.predict(b2),b8 = 'blue')
plt.title('linear regression 1 predictions')
plt.xlabel('Position level')
plt.ylabel('salaries')
plt.show()
plt.scatter(b2,b3,b8 = 'red')
plt.plot(b2, b7.predict(b6),b8 = 'blue')
plt.title('linear regression 1 predictions')
plt.xlabel('Position level')
plt.ylabel('salaries')
plt.show()
b4.predict(6.5)
b7.predict(b5.fit_transform(6.5))