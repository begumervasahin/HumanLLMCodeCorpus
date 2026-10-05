
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
dataset = pd.read_csv('insurance.csv')
X = dataset.iloc[:, :5].values
y = dataset.iloc[:, 6].values
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
X[:, 4] = labelencoder_X.fit_transform(X[:, 4])
onehotencoder = OneHotEncoder(categories='auto', sparse=False, drop='first')
X = onehotencoder.fit_transform(X)
X = X[:, [1, 3, 4, 5, 6]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = RandomForestRegressor(n_estimators=250, random_state=0)
regressor.fit(X_train, y_train)
y_predTrain = regressor.predict(X_train)
r2_Score_Train = r2_score(y_train, y_predTrain) * 100
y_predTest = regressor.predict(X_test)
r2_Score_Test = r2_score(y_test, y_predTest) * 100