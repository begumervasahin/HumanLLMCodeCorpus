import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
plt.scatter(X, y, color='red')
plt.title("Veri Setinin DaÄÄ±lÄ±mÄ±")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_regressor.predict(X), color='blue')
plt.title("Lineer Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, poly_regressor.predict(poly_features.transform(X_grid)), color='blue')
plt.title("Polynomial Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
linear_score = linear_regressor.score(X, y) * 100
poly_score = poly_regressor.score(X_poly, y) * 100
print(f"Lineer regresyon modeli doÄruluk skoru: %{linear_score:.2f}")
print(f"Polynomial regresyon modeli doÄruluk skoru: %{poly_score:.2f}")
level = 4.2
linear_pred = linear_regressor.predict([[level]])[0]
poly_pred = poly_regressor.predict(poly_features.transform([[level]]))[0]
print(f"Lineer regresyon tahmini (Kademe {level}): {linear_pred}")
print(f"Polynomial regresyon tahmini (Kademe {level}): {poly_pred}")