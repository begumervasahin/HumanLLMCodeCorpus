import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.read_excel('placements.xlsx')
b2 = b1.iloc[:,2:3].values
b3 = b1.iloc[:, 3].values
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
plt.title('PLACEMENT RECORD(Linear Regression)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
plt.show()
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b8.predict(b6.fit_transform(b2)), b9 = 'blue')
plt.title('Truth or Bluff (PLACEMENTS RECORD)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
b10 = np.arange(min(b2), max(b2), 0.1)
b10 = b10.reshape((len(b10), 1))
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b10, b8.predict(b6.fit_transform(b10)), b9 = 'blue')
plt.title('PLACEMENT RECORD (Polynomial Regression)')
plt.xlabel('NO. of Students placed')
plt.ylabel('YEAR')
plt.show()