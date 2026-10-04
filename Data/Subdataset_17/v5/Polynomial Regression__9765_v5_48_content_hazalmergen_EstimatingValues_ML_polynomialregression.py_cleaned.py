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
kf = KFold(n_splits=10, shuffle=False)
y_tests = []
y_preds = []
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    poly_features = PolynomialFeatures(degree=3)
    X_poly_train = poly_features.fit_transform(X_train)
    X_poly_test = poly_features.transform(X_test)
    model = LinearRegression()
    model.fit(X_poly_train, y_train)
    y_pred = model.predict(X_poly_test)
    y_preds.extend(y_pred)
    y_tests.extend(y_test)
plt.figure(figsize=(10, 6))
plt.scatter(y_tests, y_preds, alpha=0.6, edgecolors='w', label='Predictions vs True Values')
plt.plot(y_tests, y_tests, color="black", linewidth=2, label='Ideal Prediction')
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.title("True Values vs Predictions")
plt.legend()
plt.show()
ex_var_score = explained_variance_score(y_tests, y_preds)
mae = mean_absolute_error(y_tests, y_preds)
mse = mean_squared_error(y_tests, y_preds)
r2 = r2_score(y_tests, y_preds)
print(f"Explained Variance Score: {ex_var_score:.4f}")
print(f"Mean Absolute Error: {mae:.4f}")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R Squared Error: {r2:.4f}")