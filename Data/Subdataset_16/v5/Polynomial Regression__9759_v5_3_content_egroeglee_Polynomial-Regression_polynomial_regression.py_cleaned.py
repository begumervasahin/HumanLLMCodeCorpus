
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
from sklearn.linear_model import LinearRegression
b4 = LinearRegression()
b4.fit(b2, b3)
from sklearn.preprocessing import PolynomialFeatures
a1 = 4
b5 = PolynomialFeatures(a1=a1)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.figure(b8 = (10, 6))
plt.scatter(b2, b3, b9 = 'red', label='Actual Data')
plt.plot(b2, b4.predict(b2), b9 = 'blue', label='Linear Regression')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.figure(b8 = (10, 6))
plt.scatter(b2, b3, b9 = 'red', label='Actual Data')
plt.plot(b10, b7.predict(b5.fit_transform(b10)), b9 = 'blue', label='Polynomial Regression')
plt.title(f'Truth or Bluff (Polynomial Regression - Degree {a1})')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
a2 = 6.5
b11 = b4.predict(np.array([[a2]]))[0]
b12 = b7.predict(b5.fit_transform(np.array([[a2]])))[0]
print(f'Predicted salary (Linear Regression) for position level {a2}: {b11}')
print(f'Predicted salary (Polynomial Regression) for position level {a2}: {b12}')