
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv("Position_Salaries.csv")
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = PolynomialFeatures(degree=4)
b5 = b4.fit_transform(b2)
b6 = LinearRegression()
b6.fit(b5, b3)
b7 = LinearRegression()
b7.fit(b2, b3)
b8 = b7.predict(b2)
plt.scatter(b2, b3, b9 = "blue")
plt.plot(b2, b8, b9 = "green")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.show()
b10 = b6.predict(b5)
plt.scatter(b2, b3, b9 = "blue")
plt.plot(b2, b10, b9 = "green")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.show()
print("Predictions using simple linear regression:")
print(b7.predict([[6.5]]))
print(b7.predict([[9.5]]))
print(b7.predict([[2.5]]))
print()
print("Predictions using polynomial regression:")
print(b6.predict(b4.fit_transform([[6.5]])))
print(b6.predict(b4.fit_transform([[9.5]])))
print(b6.predict(b4.fit_transform([[2.5]])))