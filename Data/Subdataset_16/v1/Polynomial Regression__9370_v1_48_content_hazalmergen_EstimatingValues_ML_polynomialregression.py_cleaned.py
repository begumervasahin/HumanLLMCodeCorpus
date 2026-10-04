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
    b12 = b11.predict(b9.transform(b7))
    b6 += list(b12)
    b5 += list(b8)
plt.scatter(b5, b6)
plt.plot(b5, b5, b13 = "black")
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()
b14 = explained_variance_score(b5, b6)
b15 = mean_absolute_error(b5, b6)
b16 = mean_squared_error(b5, b6)
b17 = r2_score(b5, b6)
print("Explained Variance Score: ", b14)
print("Mean Absolute Error: ", b15)
print("Mean Squared Error: ", b16)
print("R Squared Error: ", b17)