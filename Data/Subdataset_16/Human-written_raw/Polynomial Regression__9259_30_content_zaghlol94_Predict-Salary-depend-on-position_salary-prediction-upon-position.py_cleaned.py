
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:,1:2].values
b3 = b1.iloc[:,2].values
'''
we don't need to do split data because the data here is very small
'''
from sklearn.linear_model import LinearRegression
b4 = LinearRegression()
b4.fit(b2,b3)
from sklearn.preprocessing import PolynomialFeatures
b5 = PolynomialFeatures(degree=2)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6,b3)
plt.scatter(b2,b3,b8 = 'red')
plt.plot(b2,b4.predict(b2),b8 = 'blue')
plt.title('Truth or Bluff')
plt.xlabel('position level')
plt.ylabel('Sallary')
plt.show()
plt.scatter(b2,b3,b8 = 'red')
plt.plot(b2,b7.predict(b5.fit_transform(b2)),b8 = 'blue')
plt.title('Truth or Bluff')
plt.xlabel('position level')
plt.ylabel('Sallary')
plt.show()
b5 = PolynomialFeatures(degree=3)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6,b3)
plt.scatter(b2,b3,b8 = 'red')
plt.plot(b2,b7.predict(b5.fit_transform(b2)),b8 = 'blue')
plt.title('Truth or Bluff')
plt.xlabel('position level')
plt.ylabel('Sallary')
plt.show()
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6,b3)
b9 = np.arange(min(b2),max(b2),0.1)
b9 = b9.reshape((len(b9)),1)
plt.scatter(b2,b3,b8 = 'red')
plt.plot(b9,b7.predict(b5.fit_transform(b9)),b8 = 'blue')
plt.title('Truth or Bluff')
plt.xlabel('position level')
plt.ylabel('Sallary')
plt.show()
b4.predict(6.2)
print(b4.intercept_,b4.coef_)
b7.predict(b5.fit_transform(6.2))
print(b7.intercept_,b7.coef_)