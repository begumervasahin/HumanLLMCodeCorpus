
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
X = dataset.iloc[:, [1, 4, 5, 6, 7]].values
y = dataset.iloc[:, 6].values
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
X[:, 4] = labelencoder_X.fit_transform(X[:, 4])
onehotencoder = OneHotEncoder(categories='auto', drop='first', sparse=False)
X_encoded = onehotencoder.fit_transform(X[:, [1, 4]])
X = np.concatenate((X_encoded, X[:, [0, 2, 3, 5]]), axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X_train, y_train)
y_pred_train = regressor.predict(X_train)
y_pred_test = regressor.predict(X_test)
r2_score_train = r2_score(y_train, y_pred_train) * 100
r2_score_test = r2_score(y_test, y_pred_test) * 100
print("R-squared score on the training set:", r2_score_train)
print("R-squared score on the test set:", r2_score_test)