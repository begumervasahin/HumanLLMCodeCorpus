import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
linearRegr = LinearRegression()
linearRegr.fit(X, y)
polynomFeat = PolynomialFeatures(degree=4)
X_poly = polynomFeat.fit_transform(X)
linearRegrPoly = LinearRegression()
linearRegrPoly.fit(X_poly, y)
predictions_linear = linearRegr.predict(X)
predictions_poly = linearRegrPoly.predict(polynomFeat.fit_transform(X))
plt.scatter(X, y, color="blue")
plt.plot(X, predictions_linear, color="green", label="Linear Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.show()
plt.scatter(X, y, color="blue")
plt.plot(X, predictions_poly, color="green", label="Polynomial Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.legend()
plt.show()
levels = [6.5, 9.5, 2.5]
for level in levels:
    print(f"Linear Regression Prediction for level {level}: {linearRegr.predict([[level]])}")
    print(f"Polynomial Regression Prediction for level {level}: {linearRegrPoly.predict(polynomFeat.fit_transform([[level]]))}")
    print()