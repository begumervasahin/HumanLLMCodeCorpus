import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
b1 = pd.read_csv('insurance.csv')
b2 = b1.iloc[:, :5].values
b3 = b1.iloc[:, 6].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
b4 = LabelEncoder()
b2[:, 1] = b4.fit_transform(b2[:, 1])
b2[:, 4] = b4.fit_transform(b2[:, 4])
b5 = OneHotEncoder(categorical_features = [1, 4])
b2 = b5.fit_transform(b2).toarray()
b2 = b2[:, [1, 3, 4, 5, 6]]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, b6 = train_test_split(b2, b3, test_size = 0.2, random_state = 0)
from sklearn.ensemble import RandomForestRegressor
b7 = RandomForestRegressor(n_estimators = 250, random_state = 0)
b7.fit(X_train, y_train)
b8 = b7.predict(X_train)
from sklearn.metrics import r2_score
b9 = r2_score(y_train, b8) * 100
b10 = b7.predict(X_test)
from sklearn.metrics import r2_score
b11 = r2_score(b6, b10) * 100