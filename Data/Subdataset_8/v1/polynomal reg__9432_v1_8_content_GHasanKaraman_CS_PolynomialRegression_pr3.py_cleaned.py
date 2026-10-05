import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
datas = pd.read_csv("datasets/dollar.csv")
X = np.array(datas["Day"]).reshape(-1, 1)
Y = np.array(datas["Price"]).reshape(-1, 1)
plt.plot(X, Y, "ob")
polynomial_features = PolynomialFeatures(degree=2)
X_poly = polynomial_features.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, Y)
y_poly_pred = model.predict(X_poly)
plt.plot(X, y_poly_pred, color="red")
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Polynomial Regression")
plt.show()