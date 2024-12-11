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
b5 = b3.drop(columns=['quality'])
X_train, X_test, y_train, b6 = train_test_split(b5, b4, test_size=0.33, random_state=42)
b7 = LinearRegression()
b7.fit(X_train, y_train)
b8 = b7.score(X_test, b6)
print("R-squared:", b8)
b9 = b7.predict(X_test)
b10 = mean_squared_error(b6, b9, squared=False)
print('RMSE:', b10)
b11 = b2.corr()['quality'].sort_values(ascending=False)[:5]
print("Top 5 features with highest b11 to quality:")
print(b11, '\n')
b12 = b1.isnull().sum().sort_values(ascending=False)[:25]
b13 = pd.DataFrame({'Feature': b12.index, 'Null Count': b12.values})
print("Top 25 features with null values:")
print(b13)