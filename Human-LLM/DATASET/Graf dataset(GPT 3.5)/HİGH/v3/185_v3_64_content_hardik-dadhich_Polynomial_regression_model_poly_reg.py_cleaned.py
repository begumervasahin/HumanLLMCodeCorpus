
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=2)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red', label='Actual Data')
plt.plot(b2, b4.predict(b2), b8 = 'blue', label='Linear Regression')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.scatter(b2, b3, b8 = 'red', label='Actual Data')
plt.plot(b2, b7.predict(b6), b8 = 'blue', label='Polynomial Regression')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b9 = b4.predict([[6.5]])[0]
print("Predicted salary with Linear Regression for position level 6.5:", b9)
b10 = b7.predict(b5.transform([[6.5]]))[0]
print("Predicted salary with Polynomial Regression for position level 6.5:", b10)