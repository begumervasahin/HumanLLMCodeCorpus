import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
b1 = pd.read_csv('winequality-red.csv')
b2 = b1.select_dtypes(include=[np.number])
b3 = b2.interpolate().dropna()
b4 = np.log(b1['quality'])
b5 = b3.drop(['quality'], axis=1)
X_train, X_test, y_train, b6 = train_test_split(b5, b4, random_state=42, test_size=0.33)
b7 = LinearRegression()
b8 = b7.fit(X_train, y_train)
b9 = b8.score(X_test, b6)
print("R-squared:", b9)
b10 = b8.predict(X_test)
b11 = mean_squared_error(b6, b10)
print('RMSE:', b11)
b12 = b2.b12()['quality'].sort_values(ascending=False)[:5]
print("Top 5 features with highest correlation to quality:")
print(b12, '\n')
b13 = b1.isnull().sum().sort_values(ascending=False)[:25]
b14 = pd.DataFrame({'Feature': b13.index, 'Null Count': b13.values})
b14.b15 = ['Null Count']
b14.index.b16 = 'Feature'
print("Top 25 features with null values:")
print(b14)