import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
import numpy as np
b1 = pd.read_csv('datas.csv')
b2 = b1.iloc[0:100, 1:6].values
b3 = b1.iloc[0:100, 6].values
b4 = b1.iloc[100:120, 1:6].values
b5 = KFold(n_splits=10)
b6 = []
b7 = []
b8 = np.array([])
b9 = True
for train_index, test_index in b5.split(b2):
    X_train, b10 = b2[train_index], b2[test_index]
    y_train, b11 = b3[train_index], b3[test_index]
    b12 = RandomForestRegressor(n_estimators=10, random_state=0)
    b12.fit(X_train, y_train)
    b13 = b12.predict(b10)
    b6.extend(b13)
    b7.extend(b11)
    if b9:
        b8 = b12.predict(b4)
        b9 = False
    else:
        b8 = np.vstack([b8, b12.predict(b4)])
print("Final Predictions before averaging:\n", b8)
b8 = np.mean(b8, axis=0)
plt.scatter(b7, b6)
plt.plot(b7, b7, b14 = "black")
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.title("True Values vs Predictions")
plt.show()
b15 = explained_variance_score(b7, b6)
b16 = mean_absolute_error(b7, b6)
b17 = mean_squared_error(b7, b6)
b18 = r2_score(b7, b6)
print(f"Explained Variance Score: {b15:.4f}")
print(f"Mean Absolute Error: {b16:.4f}")
print(f"Mean Squared Error: {b17:.4f}")
print(f"R Squared Error: {b18:.4f}")
print("Final Averaged Predictions:\n", b8)