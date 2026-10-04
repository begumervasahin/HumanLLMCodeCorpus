
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
plt.figure(b4 = (10, 6))
plt.scatter(b2, b3, b5 = 'red')
plt.title("Veri Setinin DaÄÄ±lÄ±mÄ±")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.axis([0, 11, 0, 1100000])
plt.show()
b6 = LinearRegression()
b6.fit(b2, b3)
b7 = PolynomialFeatures(degree=4)
b8 = b7.fit_transform(b2)
b9 = LinearRegression()
b9.fit(b8, b3)
plt.figure(b4 = (10, 6))
plt.scatter(b2, b3, b5 = 'red')
plt.plot(b2, b6.predict(b2), b5 = 'blue')
plt.title("Lineer Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.figure(b4 = (10, 6))
plt.scatter(b2, b3, b5 = 'red')
plt.plot(b10, b9.predict(b7.fit_transform(b10)), b5 = 'blue')
plt.title("Polynomial Regresyon Modeli")
plt.xlabel("Mesleki Kademe/Derece")
plt.ylabel("YÄ±llÄ±k MaaÅ")
plt.show()
b11 = b6.score(b2, b3) * 100
b12 = b9.score(b7.fit_transform(b2), b3) * 100
print(f"Lineer regresyon modeli doÄruluk skoru: %{b11:.2f}")
print(f"Polynomial regresyon modeli doÄruluk skoru: %{b12:.2f}")
b13 = b6.predict(np.array([[4.2]]))
b14 = b9.predict(b7.fit_transform(np.array([[4.2]])))
print(f"Lineer regresyon tahmini (4.2): {b13[0]:.2f}")
print(f"Polynomial regresyon tahmini (4.2): {b14[0]:.2f}")