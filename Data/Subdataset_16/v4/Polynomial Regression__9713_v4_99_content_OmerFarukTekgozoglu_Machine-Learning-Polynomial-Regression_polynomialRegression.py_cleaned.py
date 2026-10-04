
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
plt.plot(b2, b3, 'ro')
plt.axis([0, 11, 0, 1100000])
plt.title("Veri Setinin DaÄÄ±lÄ±mÄ±")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b4.predict(b2), b8 = 'blue')
plt.title("Lineer Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("MaaÅ")
plt.show()
b9 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b9, b7.predict(b5.fit_transform(b9)), b8 = 'blue')
plt.title("Polynomial Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("MaaÅ")
plt.show()
print("Lineer regresyon modeli doÄruluk skoru: %" + str(b4.score(b2, b3) * 100))
print("Polynomial regresyon modeli doÄruluk skoru: %" + str(b7.score(b5.fit_transform(b2), b3) * 100))
print("Lineer regresyon tahmini (4.2):", b4.predict(np.array([[4.2]])))
print("Polynomial regresyon tahmini (4.2):", b7.predict(b5.fit_transform(np.array([[4.2]]))))