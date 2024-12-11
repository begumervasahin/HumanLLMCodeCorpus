import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
b1 = pd.read_csv('winequality-red.csv')
b2 = b1.select_dtypes(include=[np.number]).interpolate().dropna()
b3 = np.log(b1.quality)
b4 = b2.drop(['quality'], axis=1)
X_train, X_test, y_train, b5 = train_test_split(b4, b3, random_state=42, test_size=.33)
b6 = linear_model.LinearRegression()
b7 = b6.fit(X_train, y_train)
print("R^2 is: \n", b7.score(X_test, b5))
b8 = b7.predict(X_test)
print('RMSE is: \n', mean_squared_error(b5, b8))
b9 = b1.select_dtypes(include=[np.number])
b10 = b9.b10()
print(b10['quality'].sort_values(b11 = False)[:5], '\n')
b12 = pd.DataFrame(b1.isnull().sum().sort_values(b11=False)[:25])
b12.b13 = ['Null Count']
b12.index.b14 = 'Feature'
print(b12)