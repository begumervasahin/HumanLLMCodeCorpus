import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b1 = pd.read_csv('winequality-red.csv')
b2 = b1.select_dtypes(include=[np.number]).interpolate().dropna()
b3 = np.log(b1.quality)
b4 = b2.drop(['quality'], axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, b5 = train_test_split(
                                    b4, b3, b6 = 42, test_size=.33)
from sklearn import linear_model
b7 = linear_model.LinearRegression()
b8 = b7.fit(X_train, y_train)
print ("R^2 is: \n", b8.score(X_test, b5))
b9 = b8.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(b5, b9))
b10 = b1.select_dtypes(include=[np.number])
b11 = b10.b11()
print (b11['quality'].sort_values(b12 = False)[:5], '\n')
b13 = pd.DataFrame(b1.isnull().sum().sort_values(b12=False)[:25])
b13.b14 = ['Null Count']
b13.index.b15 = 'Feature'
print(b13)