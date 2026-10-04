import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import KFold
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
b1 = pd.read_csv('datas.csv')
b2 = b1.iloc[0:100, 1:6].values
b3 = b1.iloc[0:100, 6].values
b4 = KFold(b5=10)
KFold(b5 = 10, random_state=None, shuffle=False)
b6 = []
b7 = []
for train_index, test_index in b4.split(b2):
        X_train, b8 = b2[train_index], b2[test_index]
        y_train, b9 = b3[train_index], b3[test_index]
        b10 = PolynomialFeatures(degree = 3)
        b11 = b10.fit_transform(X_train)
        b12 = LinearRegression()
        b12.fit(b11, y_train)
        b13 = b12.predict(b10.fit_transform(b8))
        b7 += list(b13)
        b6 += list(b9)
plt.scatter(b6, b7)
plt.plot(b6, b6, b14 = "black")
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()
b15 = explained_variance_score(b6, b7)
b16 = mean_absolute_error(b6, b7)
b17 = mean_squared_error(b6, b7)
b18 = r2_score(b6, b7)
print("Explained Variance Score: "+str(b15))
print("Mean Absolute Error "+str(b16))
print("Mean Squared Error "+str(b17))
print("R Squared Error "+str(b18))