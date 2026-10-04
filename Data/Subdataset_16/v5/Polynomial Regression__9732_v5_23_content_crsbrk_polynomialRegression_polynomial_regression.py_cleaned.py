import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('~/Desktop/Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
def fonk1(b2, b3, model, title):
    plt.scatter(b2, b3, b8 = 'red')
    plt.plot(b2, model.predict(b2), b8 = 'blue')
    plt.title(title)
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
fonk1(b2, b3, b4, 'Truth or Bluff (Linear Regression)')
fonk1(b2, b3, b7, 'Truth or Bluff (Polynomial Regression)')
b9 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b9, b7.predict(b5.transform(b9)), b8 = 'blue')
plt.title('Truth or Bluff (Polynomial Regression - High Resolution)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
b10 = b4.predict([[6.5]])
print(f"Linear Regression prediction for 6.5: {b10[0]}")
b11 = b7.predict(b5.transform([[6.5]]))
print(f"Polynomial Regression prediction for 6.5: {b11[0]}")