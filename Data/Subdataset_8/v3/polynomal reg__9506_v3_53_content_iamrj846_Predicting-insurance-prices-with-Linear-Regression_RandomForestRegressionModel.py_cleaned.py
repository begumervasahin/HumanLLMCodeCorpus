
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
features_indices = [1, 4, 5, 6, 7]
X = dataset.iloc[:, features_indices].values
y_index = 6
y = dataset.iloc[:, y_index].values
labelencoder_X = LabelEncoder()
categorical_indices = [1, 4]
for index in categorical_indices:
    X[:, index] = labelencoder_X.fit_transform(X[:, index])
onehotencoder = OneHotEncoder(categories='auto', drop='first', sparse=False)
X_categorical = onehotencoder.fit_transform(X[:, categorical_indices])
X = np.concatenate((X_categorical, X[:, [i for i in range(X.shape[1]) if i not in categorical_indices]]), axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X_train, y_train)
y_pred_train = regressor.predict(X_train)
y_pred_test = regressor.predict(X_test)
r2_score_train = r2_score(y_train, y_pred_train) * 100
r2_score_test = r2_score(y_test, y_pred_test) * 100
print("R-squared score on the training set:", r2_score_train)
print("R-squared score on the test set:", r2_score_test)