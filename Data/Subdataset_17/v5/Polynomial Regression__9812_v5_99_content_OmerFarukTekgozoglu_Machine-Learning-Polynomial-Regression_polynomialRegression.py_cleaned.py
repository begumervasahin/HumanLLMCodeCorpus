
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='red')
plt.title("Veri Setinin DaÄÄ±lÄ±mÄ±")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.axis([0, 11, 0, 1100000])
plt.show()
linear_reg = LinearRegression()
linear_reg.fit(X, y)
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
linear_reg_poly = LinearRegression()
linear_reg_poly.fit(X_poly, y)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='red')
plt.plot(X, linear_reg.predict(X), color='blue')
plt.title("Lineer Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='red')
plt.plot(X_grid, linear_reg_poly.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title("Polynomial Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
linear_reg_score = linear_reg.score(X, y) * 100
poly_reg_score = linear_reg_poly.score(poly_reg.fit_transform(X), y) * 100
print(f"Lineer regresyon modeli doÄruluk skoru: %{linear_reg_score:.2f}")
print(f"Polynomial regresyon modeli doÄruluk skoru: %{poly_reg_score:.2f}")
linear_prediction = linear_reg.predict(np.array([[4.2]]))
poly_prediction = linear_reg_poly.predict(poly_reg.fit_transform(np.array([[4.2]])))
print(f"Lineer regresyon tahmini (4.2): {linear_prediction[0]:.2f}")
print(f"Polynomial regresyon tahmini (4.2): {poly_prediction[0]:.2f}")