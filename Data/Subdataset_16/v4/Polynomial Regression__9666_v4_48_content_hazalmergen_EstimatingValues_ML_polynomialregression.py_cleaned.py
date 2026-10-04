import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
b1 = pd.read_csv('datas.csv')
b2 = b1.iloc[0:100, 1:6].values
b3 = b1.iloc[0:100, 6].values
b4 = KFold(n_splits=10, random_state=None, shuffle=False)
b5 = []
b6 = []
for train_index, test_index in b4.split(b2):
    X_train, b7 = b2[train_index], b2[test_index]
    y_train, b8 = b3[train_index], b3[test_index]
    b9 = PolynomialFeatures(degree=3)
    b10 = b9.fit_transform(X_train)
    b11 = b9.transform(b7)
    b12 = LinearRegression()
    b12.fit(b10, y_train)
    b13 = b12.predict(b11)
    b6.extend(b13)
    b5.extend(b8)
plt.scatter(b5, b6, b14 = 'Predictions vs True Values')
plt.plot(b5, b5, b15 = "black", b14='Ideal Prediction')
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.legend()
plt.show()
b16 = explained_variance_score(b5, b6)
b17 = mean_absolute_error(b5, b6)
b18 = mean_squared_error(b5, b6)
b19 = r2_score(b5, b6)
print(f"Explained Variance Score: {b16}")
print(f"Mean Absolute Error: {b17}")
print(f"Mean Squared Error: {b18}")
print(f"R Squared Error: {b19}")