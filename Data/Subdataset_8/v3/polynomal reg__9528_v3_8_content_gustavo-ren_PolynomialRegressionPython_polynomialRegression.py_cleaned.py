
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset["Level"].values.reshape(-1, 1)
y = dataset["Salary"].values
linear_model = LinearRegression()
linear_model.fit(X, y)
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_model = LinearRegression()
polynomial_model.fit(X_poly, y)
predictions_linear = linear_model.predict(X)
predictions_polynomial = polynomial_model.predict(X_poly)
plt.scatter(X, y, color="blue")
plt.plot(X, predictions_linear, color="green", label="Linear Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.show()
plt.scatter(X, y, color="blue")
plt.plot(X, predictions_polynomial, color="green", label="Polynomial Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.legend()
plt.show()
levels_to_predict = [6.5, 9.5, 2.5]
for level in levels_to_predict:
    linear_prediction = linear_model.predict([[level]])
    polynomial_prediction = polynomial_model.predict(polynomial_features.transform([[level]]))
    print(f"Linear Regression Prediction for level {level}: {linear_prediction}")
    print(f"Polynomial Regression Prediction for level {level}: {polynomial_prediction}")
    print()