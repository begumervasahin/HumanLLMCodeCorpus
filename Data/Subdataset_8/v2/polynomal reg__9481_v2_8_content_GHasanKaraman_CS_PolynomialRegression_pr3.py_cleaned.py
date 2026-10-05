
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv("datasets/dollar.csv")
days = np.array(data["Day"]).reshape(-1, 1)
prices = np.array(data["Price"]).reshape(-1, 1)
plt.figure(figsize=(10, 6))
plt.scatter(days, prices, color='blue', label='Actual data')
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Dollar Price Trend")
degree_of_polynomial = 2
poly_features = PolynomialFeatures(degree=degree_of_polynomial)
days_poly = poly_features.fit_transform(days)
linear_regression_model = LinearRegression()
linear_regression_model.fit(days_poly, prices)
prices_predicted = linear_regression_model.predict(days_poly)
plt.plot(days, prices_predicted, color="red", label="Polynomial Regression")
plt.legend()
plt.show()