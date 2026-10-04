import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
dataset = pd.read_csv('datas.csv')
X = dataset.iloc[0:100, 1:6].values
y = dataset.iloc[0:100, 6].values
kf = KFold(n_splits=10)
y_tests = []
y_preds = []
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    poly_reg = PolynomialFeatures(degree=3)
    X_poly_train = poly_reg.fit_transform(X_train)
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly_train, y_train)
    X_poly_test = poly_reg.transform(X_test)
    y_pred = lin_reg.predict(X_poly_test)
    y_tests.extend(y_test)
    y_preds.extend(y_pred)
plt.figure(figsize=(10, 6))
plt.scatter(y_tests, y_preds, alpha=0.7)
plt.plot(y_tests, y_tests, color="black", linewidth=1)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.title("True Values vs Predictions")
plt.grid(True)
plt.show()
explained_variance = explained_variance_score(y_tests, y_preds)
mean_absolute = mean_absolute_error(y_tests, y_preds)
mean_squared = mean_squared_error(y_tests, y_preds)
r2 = r2_score(y_tests, y_preds)
print(f"Explained Variance Score: {explained_variance:.4f}")
print(f"Mean Absolute Error: {mean_absolute:.4f}")
print(f"Mean Squared Error: {mean_squared:.4f}")
print(f"R Squared Error: {r2:.4f}")