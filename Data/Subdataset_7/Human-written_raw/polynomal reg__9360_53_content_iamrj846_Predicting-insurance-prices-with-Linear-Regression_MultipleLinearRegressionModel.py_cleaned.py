import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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
import statsmodels.formula.api as sm
b2 = np.append(arr = np.ones((1338, 1)).astype(int), values = b2, axis = 1)
b6 = b2[:, [0, 2, 3, 4]]
b7 = sm.OLS(endog = b3, exog = b6).fit()
b7.summary()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, b8 = train_test_split(b6, b3, test_size = 0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
b9 = LinearRegression()
b9.fit(X_train, y_train)
b10 = b9.predict(X_train)
from sklearn.metrics import r2_score
b11 = r2_score(y_train, b10) * 100
b12 = b9.predict(X_test)
from sklearn.metrics import r2_score
b13 = r2_score(b8, b12) * 100