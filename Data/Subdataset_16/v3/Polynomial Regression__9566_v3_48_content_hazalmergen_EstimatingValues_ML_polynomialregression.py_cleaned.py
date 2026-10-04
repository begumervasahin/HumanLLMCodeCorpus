import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
b1 = pd.read_csv('datas.csv')
b2 = b1.iloc[0:100, 1:6].values
b3 = b1.iloc[0:100, 6].values
b4 = KFold(n_splits=10)
b5 = []
b6 = []
for train_index, test_index in b4.split(b2):
    X_train, b7 = b2[train_index], b2[test_index]
    y_train, b8 = b3[train_index], b3[test_index]
    b9 = PolynomialFeatures(degree=3)
    b10 = b9.fit_transform(X_train)
    b11 = LinearRegression()
    b11.fit(b10, y_train)
    b12 = b9.transform(b7)
    b13 = b11.predict(b12)
    b5.extend(b8)
    b6.extend(b13)
plt.figure(b14 = (10, 6))
plt.scatter(b5, b6, b15 = 0.7)
plt.plot(b5, b5, b16 = "black", linewidth=1)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.title("True Values vs Predictions")
plt.grid(True)
plt.show()
b17 = explained_variance_score(b5, b6)
b18 = mean_absolute_error(b5, b6)
b19 = mean_squared_error(b5, b6)
b20 = r2_score(b5, b6)
print(f"Explained Variance Score: {b17:.4f}")
print(f"Mean Absolute Error: {b18:.4f}")
print(f"Mean Squared Error: {b19:.4f}")
print(f"R Squared Error: {b20:.4f}")