import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
b1 = pd.read_csv('winequality-red.csv')
b2 = b1.select_dtypes(include=[np.number])
b3 = b2.interpolate().dropna()
b4 = np.log(b1.quality)
b5 = b3.drop(['quality'], axis=1)
X_train, X_test, y_train, b6 = train_test_split(b5, b4, random_state=42, test_size=.33)
b7 = linear_model.LinearRegression()
b8 = b7.fit(X_train, y_train)
print("R-squared:", b8.score(X_test, b6))
b9 = b8.predict(X_test)
print('RMSE:', mean_squared_error(b6, b9))
b10 = b2.corr()['quality'].sort_values(ascending=False)[:5]
print("Top 5 features with highest b10 to quality:")
print(b10, '\n')
b11 = b1.isnull().sum().sort_values(ascending=False)[:25]
b12 = pd.DataFrame({'Feature': b11.index, 'Null Count': b11.values})
print("Top 25 features with null values:")
print(b12)