
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
b1 = dataset.iloc[:, [1, 4, 5, 6, 7]].values
b2 = dataset.iloc[:, 6].values
b3 = LabelEncoder()
b1[:, 1] = b3.fit_transform(b1[:, 1])
b1[:, 4] = b3.fit_transform(b1[:, 4])
b4 = OneHotEncoder(categories='auto', drop='first', sparse=False)
b5 = b4.fit_transform(b1[:, [1, 4]])
b1 = np.concatenate((b5, b1[:, [0, 2, 3, 5]]), axis=1)
X_train, X_test, y_train, b6 = train_test_split(b1, b2, test_size=0.2, random_state=0)
b7 = RandomForestRegressor(n_estimators=10, random_state=0)
b7.fit(X_train, y_train)
b8 = b7.predict(X_train)
b9 = b7.predict(X_test)
b10 = r2_score(y_train, b8) * 100
b11 = r2_score(b6, b9) * 100
print("R-squared score on the training set:", b10)
print("R-squared score on the test set:", b11)