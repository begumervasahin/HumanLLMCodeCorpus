import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv("datasets/dollar.csv")
X = data["Day"].values.reshape(-1, 1)
Y = data["Price"].values.reshape(-1, 1)
plt.plot(X, Y, "ob", label="Original Data")
polynomial_converter = PolynomialFeatures(degree=2)
X_transformed = polynomial_converter.fit_transform(X)
model = LinearRegression()
model.fit(X_transformed, Y)
predicted_values = model.predict(X_transformed)
plt.plot(X, predicted_values, color="red", label="Polynomial Regression")
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Polynomial Regression")
plt.legend()
plt.show()