import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = PolynomialFeatures(degree=4)
b5 = b4.fit_transform(b2)
b6 = LinearRegression()
b6.fit(b5, b3)
plt.scatter(b2, b3, b7 = 'orange')
plt.plot(b2, b6.predict(b4.fit_transform(b2)), b7 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
b8 = np.arange(min(b2), max(b2), 0.1)
b8 = b8.reshape(len(b8), 1)
plt.scatter(b2, b3, b7 = 'orange')
plt.plot(b8, b6.predict(b4.fit_transform(b8)), b7 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
a1 = 6.5
b9 = b6.predict(b4.fit_transform([[a1]]))
print(f"Predicted salary for position level {a1}: ${b9[0]}")