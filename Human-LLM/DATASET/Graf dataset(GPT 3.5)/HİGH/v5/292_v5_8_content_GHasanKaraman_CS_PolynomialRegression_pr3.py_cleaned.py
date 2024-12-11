import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv("datasets/dollar.csv")
b2 = b1["Day"].values.reshape(-1, 1)
b3 = b1["Price"].values.reshape(-1, 1)
plt.plot(b2, b3, "ob", b4 = "Original Data")
b5 = PolynomialFeatures(degree=2)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
b8 = b7.predict(b6)
plt.plot(b2, b8, b9 = "red", b4="Polynomial Regression")
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Polynomial Regression")
plt.legend()
plt.show()