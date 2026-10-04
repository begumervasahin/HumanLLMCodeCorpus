import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
b1 = pd.read_csv('50_Startups.csv')
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, 4].values
b4 = LabelEncoder()
b2[:, 3] = b4.fit_transform(b2[:, 3])
b5 = OneHotEncoder()
b2 = b5.fit_transform(b2).toarray()
b2 = b2[:, 1:]
X_train, X_test, y_train, b6 = train_test_split(b2, b3, test_size=0.2, random_state=0)
b7 = LinearRegression()
b7.fit(X_train, y_train)
b8 = b7.predict(X_test)
b2 = np.append(arr=np.ones((50, 1)).astype(int), values=b1.iloc[:, :-1].values, axis=1)
b2[:, 4] = b4.transform(b2[:, 4])
b2 = b5.fit_transform(b2).toarray()
b2 = b2[:, 1:]
b2 = np.append(arr=np.ones((50, 1)).astype(int), values=b1.iloc[:, :-1].values, axis=1)
b2[:, 3] = b4.transform(b2[:, 3])
b2 = b5.fit_transform(b2).toarray()
b2 = b2[:, 1:]
b9 = b2[:, [0, 1, 2, 3, 4, 5]]
b10 = sm.OLS(endog=b3, exog=b9).fit()
print(b10.summary())
b9 = b2[:, [0, 1, 3, 4, 5]]
b10 = sm.OLS(endog=b3, exog=b9).fit()
print(b10.summary())
b9 = b2[:, [0, 3, 4, 5]]
b10 = sm.OLS(endog=b3, exog=b9).fit()
print(b10.summary())
b9 = b2[:, [0, 3, 5]]
b10 = sm.OLS(endog=b3, exog=b9).fit()
print(b10.summary())
b9 = b2[:, [0, 3]]
b10 = sm.OLS(endog=b3, exog=b9).fit()
print(b10.summary())