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
b5 = KFold(n_splits=10, shuffle=False, random_state=None)
b6 = []
b7 = []
b8 = []
for train_index, test_index in b5.split(b2):
    X_train, b9 = b2[train_index], b2[test_index]
    y_train, b10 = b3[train_index], b3[test_index]
    b11 = RandomForestRegressor(n_estimators=10, random_state=0)
    b11.fit(X_train, y_train)
    b12 = b11.predict(b9)
    b6.extend(b12)
    b7.extend(b10)
    b13 = b11.predict(b4)
    b8.append(b13)
b8 = np.array(b8)
b14 = np.mean(b8, axis=0)
plt.scatter(b7, b6)
plt.plot(b7, b7, b15 = "black")
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.title("True vs Predicted Values")
plt.show()
b16 = explained_variance_score(b7, b6)
b17 = mean_absolute_error(b7, b6)
b18 = mean_squared_error(b7, b6)
b19 = r2_score(b7, b6)
print("Explained Variance Score:", b16)
print("Mean Absolute Error:", b17)
print("Mean Squared Error:", b18)
print("R Squared Error:", b19)
print("Final Averaged Predictions:", b14)