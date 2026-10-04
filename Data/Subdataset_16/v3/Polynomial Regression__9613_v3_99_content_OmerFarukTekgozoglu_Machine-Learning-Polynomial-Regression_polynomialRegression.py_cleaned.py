import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
def fonk1(b2, b3):
    plt.scatter(b2, b3, b4 = 'red')
    plt.title("Veri Setinin DaÄÄ±lÄ±mÄ±")
    plt.xlabel("Mesleki Kademe/Derece")
    plt.ylabel("YÄ±llÄ±k MaaÅ")
    plt.show()
fonk1(b2, b3)
def fonk2(b2, b3):
    b5 = LinearRegression()
    b5.fit(b2, b3)
    return b5
b5 = fonk2(b2, b3)
def fonk3(b2, b3, b5):
    plt.scatter(b2, b3, b4 = 'red')
    plt.plot(b2, b5.predict(b2), b4 = 'blue')
    plt.title("Lineer Regresyon Modeli")
    plt.xlabel("Mesleki Kademe/Derece")
    plt.ylabel("YÄ±llÄ±k MaaÅ")
    plt.show()
fonk3(b2, b3, b5)
def fonk4(b2, b3, b6 = 4):
    b7 = PolynomialFeatures(b6=b6)
    b8 = b7.fit_transform(b2)
    b9 = LinearRegression()
    b9.fit(b8, b3)
    return b7, b9
b7, b9 = fonk4(b2, b3)
def fonk5(b2, b3, b7, b9):
    b10 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
    plt.scatter(b2, b3, b4 = 'red')
    plt.plot(b10, b9.predict(b7.transform(b10)), b4 = 'blue')
    plt.title("Polynomial Regresyon Modeli")
    plt.xlabel("Mesleki Kademe/Derece")
    plt.ylabel("YÄ±llÄ±k MaaÅ")
    plt.show()
fonk5(b2, b3, b7, b9)
def fonk6(b5, b9, b2, b3, b7):
    b11 = b5.score(b2, b3) * 100
    b12 = b9.score(b7.transform(b2), b3) * 100
    print(f"Lineer regresyon modeli doÄruluk skoru: %{b11:.2f}")
    print(f"Polynomial regresyon modeli doÄruluk skoru: %{b12:.2f}")
fonk6(b5, b9, b2, b3, b7)
def fonk7(b5, b9, b7, a1):
    b13 = b5.predict([[a1]])[0]
    b14 = b9.predict(b7.transform([[a1]]))[0]
    print(f"Lineer regresyon tahmini (Kademe {a1}): {b13}")
    print(f"Polynomial regresyon tahmini (Kademe {a1}): {b14}")
a1 = 4.2
fonk7(b5, b9, b7, a1)