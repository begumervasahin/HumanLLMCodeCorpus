import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('position_salaries.csv')
b2 = b1.iloc[:,1:2].values
b3 = b1.iloc[:, 2].values
'''from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, b4 = train_test_split(b2, b3, test_size = 0.2, random_state = 0)'''
from sklearn.linear_model import LinearRegression
b5 = LinearRegression()
b5.fit(b2, b3)
from sklearn.preprocessing import PolynomialFeatures
b6 = PolynomialFeatures(degree = 4)
b7 = b6.fit_transform(b2)
b6.fit(b7, b3)
b8 = LinearRegression()
b8.fit(b7, b3)
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b5.predict(b2), b9 = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b8.predict(b6.fit_transform(b2)), b9 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
b10 = np.arange(min(b2), max(b2), 0.1)
b10 = b10.reshape((len(b10), 1))
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b10, b8.predict(b6.fit_transform(b10)), b9 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
plt.savefig('position_salary.png')
'''b5.predict(6.5)
b8.predict(b6.fit_transform(6.5)'''