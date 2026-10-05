
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
b1 = pd.read_csv('insurance.csv')
b2 = b1.iloc[:, :5].values
b3 = b1.iloc[:, 6].values
b4 = LabelEncoder()
b2[:, 1] = b4.fit_transform(b2[:, 1])
b2[:, 4] = b4.fit_transform(b2[:, 4])
b5 = OneHotEncoder(categories='auto', drop='first')
b6 = b5.fit_transform(b2).toarray()
b7 = b6[:, [1, 3, 4, 5, 6]]
b8 = np.append(arr=np.ones((len(b1), 1)).astype(int), values=b7, axis=1)
b9 = b8[:, [0, 2, 3, 4]]
b10 = sm.OLS(endog=b3, exog=b9).fit()
print(b10.summary())
X_train, X_test, y_train, b11 = train_test_split(b9, b3, test_size=0.2, random_state=0)
b12 = LinearRegression()
b12.fit(X_train, y_train)
b13 = b12.predict(X_train)
b14 = r2_score(y_train, b13) * 100
b15 = b12.predict(X_test)
b16 = r2_score(b11, b15) * 100