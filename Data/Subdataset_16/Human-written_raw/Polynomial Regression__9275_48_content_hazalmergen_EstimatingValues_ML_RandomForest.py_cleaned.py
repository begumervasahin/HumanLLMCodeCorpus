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
b5 = KFold(b6=10)
KFold(b6 = 10, random_state=None, shuffle=False)
b7 = []
b8 = []
b9 = np.array([])
a1 = 0
for train_index, test_index in b5.split(b2):
    X_train, b10 = b2[train_index], b2[test_index]
    y_train, b11 = b3[train_index], b3[test_index]
    b12 = RandomForestRegressor(n_estimators=10, random_state=0)
    b12.fit(X_train, y_train)
    b13 = b12.predict(b10)
    b7 += list(b13)
    b8 += list(b11)
    if a1 = =0:
        b9 = b12.predict(b4)
        a1 = 1
    else:
        b9 = np.vstack([b9, b12.predict(b4)])
print(b9)
b9 = np.mean(b9, axis=0)
plt.scatter(b8, b7)
plt.plot(b8, b8, b14 = "black")
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()
b15 = explained_variance_score(b8, b7)
b16 = mean_absolute_error(b8, b7)
b17 = mean_squared_error(b8, b7)
b18 = r2_score(b8, b7)
print("Explained Variance Score: "+str(b15))
print("Mean Absolute Error "+str(b16))
print("Mean Squared Error "+str(b17))
print("R Squared Error "+str(b18))
print(b9)