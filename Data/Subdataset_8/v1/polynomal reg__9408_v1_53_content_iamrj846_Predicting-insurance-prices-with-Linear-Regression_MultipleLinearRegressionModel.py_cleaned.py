import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
dataset = pd.read_csv('insurance.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
X[:, 4] = labelencoder_X.fit_transform(X[:, 4])
onehotencoder = OneHotEncoder(categories='auto', sparse=False)
X = onehotencoder.fit_transform(X)
X = X[:, [1, 3, 4, 5, 6]]
X = np.append(arr=np.ones((X.shape[0], 1)).astype(int), values=X, axis=1)
regressor_OLS = sm.OLS(endog=y, exog=X).fit()
print(regressor_OLS.summary())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred_train = regressor.predict(X_train)
y_pred_test = regressor.predict(X_test)
r2_score_train = r2_score(y_train, y_pred_train) * 100
r2_score_test = r2_score(y_test, y_pred_test) * 100
print("R-squared score on training set: {:.2f}%".format(r2_score_train))
print("R-squared score on test set: {:.2f}%".format(r2_score_test))