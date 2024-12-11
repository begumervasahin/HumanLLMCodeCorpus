
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
b1 = [1, 4, 5, 6, 7]
b2 = dataset.iloc[:, b1].values
a1 = 6
b3 = dataset.iloc[:, a1].values
b4 = LabelEncoder()
b5 = [1, 4]
for index in b5:
    b2[:, index] = b4.fit_transform(b2[:, index])
b6 = OneHotEncoder(categories='auto', drop='first', sparse=False)
b7 = b6.fit_transform(b2[:, b5])
b2 = np.concatenate((b7, b2[:, [i for i in range(b2.shape[1]) if i not in b5]]), axis=1)
X_train, X_test, y_train, b8 = train_test_split(b2, b3, test_size=0.2, random_state=0)
b9 = RandomForestRegressor(n_estimators=10, random_state=0)
b9.fit(X_train, y_train)
b10 = b9.predict(X_train)
b11 = b9.predict(X_test)
b12 = r2_score(y_train, b10) * 100
b13 = r2_score(b8, b11) * 100
print("R-squared score on the training set:", b12)
print("R-squared score on the test set:", b13)