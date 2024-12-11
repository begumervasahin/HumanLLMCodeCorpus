
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv("datasets/dollar.csv")
b2 = np.array(b1["Day"]).reshape(-1, 1)
b3 = np.array(b1["Price"]).reshape(-1, 1)
plt.figure(b4 = (10, 6))
plt.scatter(b2, b3, b5 = 'blue', label='Actual b1')
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Dollar Price Trend")
a1 = 2
b6 = PolynomialFeatures(a1=a1)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
b9 = b8.predict(b7)
plt.plot(b2, b9, b5 = "red", label="Polynomial Regression")
plt.legend()
plt.show()