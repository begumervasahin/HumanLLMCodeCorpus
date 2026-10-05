
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = LinearRegression()
b4.fit(b2, b3)
a1 = 4
b5 = PolynomialFeatures(a1=a1)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b4.predict(b2), b8 = 'green', label='Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.title('Linear Regression')
plt.legend()
plt.show()
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b7.predict(b6), b8 = 'blue', label='Polynomial Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.title('Polynomial Regression (Degree {})'.format(a1))
plt.legend()
plt.show()
a2 = 6.5
b9 = b5.transform([[a2]])
b10 = b7.predict(b9)
print(f'Predicted Salary for Position Level {a2}: ${b10[0]}')