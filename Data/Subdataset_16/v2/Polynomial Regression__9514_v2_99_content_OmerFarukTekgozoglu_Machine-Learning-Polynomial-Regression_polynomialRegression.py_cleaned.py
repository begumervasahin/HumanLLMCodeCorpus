import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
plt.scatter(b2, b3, b4 = 'red')
plt.title("Veri Setinin DaÄÄ±lÄ±mÄ±")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
b5 = LinearRegression()
b5.fit(b2, b3)
plt.scatter(b2, b3, b4 = 'red')
plt.plot(b2, b5.predict(b2), b4 = 'blue')
plt.title("Lineer Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
b6 = PolynomialFeatures(degree=4)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
b9 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.scatter(b2, b3, b4 = 'red')
plt.plot(b9, b8.predict(b6.transform(b9)), b4 = 'blue')
plt.title("Polynomial Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
b10 = b5.score(b2, b3) * 100
b11 = b8.score(b7, b3) * 100
print(f"Lineer regresyon modeli doÄruluk skoru: %{b10:.2f}")
print(f"Polynomial regresyon modeli doÄruluk skoru: %{b11:.2f}")
a1 = 4.2
b12 = b5.predict([[a1]])[0]
b13 = b8.predict(b6.transform([[a1]]))[0]
print(f"Lineer regresyon tahmini (Kademe {a1}): {b12}")
print(f"Polynomial regresyon tahmini (Kademe {a1}): {b13}")