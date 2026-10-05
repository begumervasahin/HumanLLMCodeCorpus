import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
degree_of_polynomial = 4
polynomial_features = PolynomialFeatures(degree=degree_of_polynomial)
X_poly = polynomial_features.fit_transform(X)
linear_regr_poly = LinearRegression()
linear_regr_poly.fit(X_poly, y)
simple_linear_regr = LinearRegression()
simple_linear_regr.fit(X, y)
predictions_simple_linear = simple_linear_regr.predict(X)
plt.scatter(X, y, color="blue")
plt.plot(X, predictions_simple_linear, color="green")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Simple Linear Regression")
plt.show()
predictions_polynomial = linear_regr_poly.predict(X_poly)
plt.scatter(X, y, color="blue")
plt.plot(X, predictions_polynomial, color="green")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.show()
print("Predictions using simple linear regression:")
print(simple_linear_regr.predict([[6.5]]))
print(simple_linear_regr.predict([[9.5]]))
print(simple_linear_regr.predict([[2.5]]))
print()
print("Predictions using polynomial regression:")
print(linear_regr_poly.predict(polynomial_features.fit_transform([[6.5]])))
print(linear_regr_poly.predict(polynomial_features.fit_transform([[9.5]])))
print(linear_regr_poly.predict(polynomial_features.fit_transform([[2.5]])))