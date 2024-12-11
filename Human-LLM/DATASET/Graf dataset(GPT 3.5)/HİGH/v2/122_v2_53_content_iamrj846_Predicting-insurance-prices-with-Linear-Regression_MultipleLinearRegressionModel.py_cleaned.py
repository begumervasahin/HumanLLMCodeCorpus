
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
b1 = pd.read_csv('insurance.csv')
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, -1].values
b4 = LabelEncoder()
b2[:, 1] = b4.fit_transform(b2[:, 1])
b2[:, 4] = b4.fit_transform(b2[:, 4])
b5 = OneHotEncoder(categories='auto', sparse=False)
b2 = b5.fit_transform(b2)
b2 = b2[:, [1, 3, 4, 5, 6]]
b2 = np.append(arr=np.ones((b2.shape[0], 1)).astype(int), values=b2, axis=1)
b6 = sm.OLS(endog=b3, exog=b2).fit()
print(b6.summary())
X_train, X_test, y_train, b7 = train_test_split(b2, b3, test_size=0.2, random_state=0)
b8 = LinearRegression()
b8.fit(X_train, y_train)
b9 = b8.predict(X_train)
b10 = b8.predict(X_test)
b11 = r2_score(y_train, b9) * 100
b12 = r2_score(b7, b10) * 100
print("R-squared score on training set: {:.2f}%".format(b11))
print("R-squared score on test set: {:.2f}%".format(b12))