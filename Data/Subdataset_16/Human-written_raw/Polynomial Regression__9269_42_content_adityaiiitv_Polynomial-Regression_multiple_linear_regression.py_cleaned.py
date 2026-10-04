import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('50_Startups.csv')
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, 4].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
b4 = LabelEncoder()
b2[:, 3] = b4.fit_transform(b2[:, 3])
b5 = OneHotEncoder(categorical_features = [3])
b2 = b5.fit_transform(b2).toarray()
b2 = b2[:,1:]
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, b6 = train_test_split(b2, b3, test_size = 0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
b7 = LinearRegression()
b7.fit(X_train,y_train)
b8 = b7.predict(X_test)
import statsmodels.formula.api as sm
b2 = np.append(arr = np.ones((50,1)).astype(int), values = b2,axis=1)
b9 = b2[:,[0,1,2,3,4,5]]
b10 = sm.OLS(endog=b3,exog=b9).fit()
b10.summary()
b9 = b2[:,[0,1,3,4,5]]
b10 = sm.OLS(endog=b3,exog=b9).fit()
b10.summary()
b9 = b2[:,[0,3,4,5]]
b10 = sm.OLS(endog=b3,exog=b9).fit()
b10.summary()
b9 = b2[:,[0,3,5]]
b10 = sm.OLS(endog=b3,exog=b9).fit()
b10.summary()
b9 = b2[:,[0,3]]
b10 = sm.OLS(endog=b3,exog=b9).fit()
b10.summary()