
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
linear_regr_poly = LinearRegression()
linear_regr_poly.fit(X_poly, y)
linear_regr = LinearRegression()
linear_regr.fit(X, y)
predictions_linear = linear_regr.predict(X)
plt.scatter(X, y, color="blue")
plt.plot(X, predictions_linear, color="green")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.show()
predictions_poly = linear_regr_poly.predict(X_poly)
plt.scatter(X, y, color="blue")
plt.plot(X, predictions_poly, color="green")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.show()
print("Predictions using simple linear regression:")
print(linear_regr.predict([[6.5]]))
print(linear_regr.predict([[9.5]]))
print(linear_regr.predict([[2.5]]))
print()
print("Predictions using polynomial regression:")
print(linear_regr_poly.predict(polynomial_features.fit_transform([[6.5]])))
print(linear_regr_poly.predict(polynomial_features.fit_transform([[9.5]])))
print(linear_regr_poly.predict(polynomial_features.fit_transform([[2.5]])))