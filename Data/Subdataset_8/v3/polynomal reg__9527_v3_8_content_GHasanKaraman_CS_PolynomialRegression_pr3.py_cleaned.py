
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv("datasets/dollar.csv")
X = np.array(data["Day"]).reshape(-1, 1)
y = np.array(data["Price"]).reshape(-1, 1)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual data')
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Dollar Price Trend")
degree = 2
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)
plt.plot(X, y_pred, color="red", label="Polynomial Regression")
plt.legend()
plt.show()