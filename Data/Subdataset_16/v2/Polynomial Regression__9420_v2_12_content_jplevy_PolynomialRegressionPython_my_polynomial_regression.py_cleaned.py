import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = LinearRegression()
b4.fit(b2, b3)
a1 = 4
b5 = PolynomialFeatures(a1=a1)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red', label='Actual')
plt.plot(b2, b4.predict(b2), b8 = 'blue', label='Linear Model')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b9 = np.arange(min(b2), max(b2), 0.01).reshape(-1, 1)
plt.scatter(b2, b3, b8 = 'red', label='Actual')
plt.plot(b9, b7.predict(b5.fit_transform(b9)), b8 = 'blue', label='Polynomial Model')
plt.title(f'Truth or Bluff (Polynomial Regression, b10 = {a1})')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
a2 = 6.5
b11 = b4.predict([[a2]])
b12 = b7.predict(b5.fit_transform([[a2]]))
print(f"Linear Regression Prediction for position level {a2}: {b11[0]}")
print(f"Polynomial Regression Prediction for position level {a2}: {b12[0]}")