'''
Created by Omer Faruk
'''
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
plt.plot(X, y, 'ro')
plt.axis([0, 11, 0, 1100000])
plt.title("Veri Setinin DaÄÄ±lÄ±mÄ±")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(X,y)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
linear_reg_poly = LinearRegression()
linear_reg_poly.fit(X_poly, y)
plt.scatter(X, y, color = 'red')
plt.plot(X, linear_reg.predict(X), color = 'blue')
plt.title("Lineer Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("MaaÅ")
plt.show()
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, linear_reg_poly.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title("Polynomial Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("MaaÅ")
plt.show()
print("Lineer regresyon modeli doÄruluk skoru: %" + str(linear_reg.score(X,y)*100))
print("Polynomial regresyon modeli doÄruluk skoru: %" + str(linear_reg_poly.score(poly_reg.fit_transform(X), y)*100))
linear_reg.predict(4.2)
linear_reg_poly.predict(poly_reg.fit_transform(4.2))