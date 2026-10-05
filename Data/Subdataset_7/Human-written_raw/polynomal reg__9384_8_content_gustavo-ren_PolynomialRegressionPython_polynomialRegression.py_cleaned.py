import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
b1 = pd.read_csv("Position_Salaries.csv")
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = PolynomialFeatures(degree=4)
b5 = b4.fit_transform(b2)
b6 = LinearRegression()
b6.fit(b5, b3)
b7 = LinearRegression()
b7.fit(b2, b3)
b7.predict(b2)
plt.scatter(b2, b3, b8 = "blue")
plt.plot(b2, b7.predict(b2), b8 = "green")
plt.xlabel("Salary")
plt.ylabel("Level")
plt.show()
plt.scatter(b2, b3, b8 = "blue")
plt.plot(b2, b6.predict(b4.fit_transform(b2)),
         b8 = "green")
plt.xlabel("Salary")
plt.ylabel("Level")
plt.show()
print(b7.predict(6.5))
print(b7.predict(9.5))
print(b7.predict(2.5))
print("\n")
print(b6.predict(b4.fit_transform(6.5)))
print(b6.predict(b4.fit_transform(9.5)))
print(b6.predict(b4.fit_transform(2.5)))