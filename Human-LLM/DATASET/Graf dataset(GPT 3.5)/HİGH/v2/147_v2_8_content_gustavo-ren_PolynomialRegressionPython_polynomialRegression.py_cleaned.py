
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
b1 = pd.read_csv("Position_Salaries.csv")
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
b8 = b4.predict(b2)
b9 = b7.predict(b5.fit_transform(b2))
plt.scatter(b2, b3, b10 = "blue")
plt.plot(b2, b8, b10 = "green", label="Linear Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.show()
plt.scatter(b2, b3, b10 = "blue")
plt.plot(b2, b9, b10 = "green", label="Polynomial Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.legend()
plt.show()
b11 = [6.5, 9.5, 2.5]
for level in b11:
    b12 = b4.predict([[level]])
    b13 = b7.predict(b5.fit_transform([[level]]))
    print(f"Linear Regression Prediction for level {level}: {b12}")
    print(f"Polynomial Regression Prediction for level {level}: {b13}")
    print()