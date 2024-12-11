import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
b1 = pd.read_csv('insurance.csv')
b2 = b1.iloc[:, :-1]
b3 = b1.iloc[:, -1]
b4 = LabelEncoder()
b2['sex'] = b4.fit_transform(b2['sex'])
b2['region'] = b4.fit_transform(b2['region'])
b5 = OneHotEncoder(categories='auto', sparse=False)
b6 = b5.fit_transform(b2)
b6 = b6[:, [1, 3, 4, 5, 6]]
b6 = np.append(arr=np.ones((b6.shape[0], 1)).astype(int), values=b6, axis=1)
b7 = sm.OLS(endog=b3, exog=b6).fit()
print(b7.summary())
X_train, X_test, y_train, b8 = train_test_split(b6, b3, test_size=0.2, random_state=0)
b9 = LinearRegression()
b9.fit(X_train, y_train)
b10 = b9.predict(X_train)
b11 = b9.predict(X_test)
b12 = r2_score(y_train, b10) * 100
b13 = r2_score(b8, b11) * 100
print("R-squared score on training set: {:.2f}%".format(b12))
print("R-squared score on test set: {:.2f}%".format(b13))