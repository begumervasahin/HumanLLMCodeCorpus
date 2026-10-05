import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = PolynomialFeatures(degree=4)
b5 = b4.fit_transform(b2)
b6 = LinearRegression()
b6.fit(b5, b3)
plt.scatter(b2, b3, b7 = 'orange', label='Actual data')
plt.plot(b2, b6.predict(b5), b7 = 'blue', label='Polynomial Regression')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b8 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.scatter(b2, b3, b7 = 'orange', label='Actual data')
plt.plot(b8, b6.predict(b4.transform(b8)), b7 = 'blue', label='Polynomial Regression')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
a1 = 6.5
b9 = b6.predict(b4.transform([[a1]]))
print(f"Predicted salary for position level {a1}: ${b9[0]}")