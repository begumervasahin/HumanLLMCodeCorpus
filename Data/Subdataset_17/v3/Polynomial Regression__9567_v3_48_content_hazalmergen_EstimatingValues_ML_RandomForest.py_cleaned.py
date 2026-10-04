import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
import numpy as np
dataset = pd.read_csv('datas.csv')
X = dataset.iloc[0:100, 1:6].values
y = dataset.iloc[0:100, 6].values
X_Pred = dataset.iloc[100:120, 1:6].values
kf = KFold(n_splits=10)
y_preds = []
y_tests = []
Y_final_pred = np.array([])
first_iteration = True
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    regressor = RandomForestRegressor(n_estimators=10, random_state=0)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    y_preds.extend(y_pred)
    y_tests.extend(y_test)
    if first_iteration:
        Y_final_pred = regressor.predict(X_Pred)
        first_iteration = False
    else:
        Y_final_pred = np.vstack([Y_final_pred, regressor.predict(X_Pred)])
print("Final Predictions before averaging:\n", Y_final_pred)
Y_final_pred = np.mean(Y_final_pred, axis=0)
plt.scatter(y_tests, y_preds)
plt.plot(y_tests, y_tests, color="black")
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.title("True Values vs Predictions")
plt.show()
ex_var_score = explained_variance_score(y_tests, y_preds)
m_absolute_error = mean_absolute_error(y_tests, y_preds)
m_squared_error = mean_squared_error(y_tests, y_preds)
r_2_score = r2_score(y_tests, y_preds)
print(f"Explained Variance Score: {ex_var_score:.4f}")
print(f"Mean Absolute Error: {m_absolute_error:.4f}")
print(f"Mean Squared Error: {m_squared_error:.4f}")
print(f"R Squared Error: {r_2_score:.4f}")
print("Final Averaged Predictions:\n", Y_final_pred)