import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, metrics
b1 = pd.read_csv('3-Products-Multiple.csv')
b2 = b1.iloc[:, :-1]
b3 = b1.iloc[:, 4]
b4 = pd.get_dummies(b2['Location'], drop_first=True)
b2 = b2.drop('Location', axis=1)
b2 = pd.concat([b2, b4], axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, b5 = train_test_split(b2, b3, test_size=0.2, random_state=0)
from sklearn.linear_model import LinearRegression
b6 = linear_model.LinearRegression()
b6.fit(X_train, y_train)
print('Coefficients: \n', b6.coef_)
print('Variance score: {}'.format(b6.score(X_test, b5)))
b7 = b6.predict(X_test)
print('Prediction: ')
print(b7)
print('Based on the results, product_1 would yield a better profit at a particular city  and overall.')
plt.style.use('fivethirtyeight')
plt.scatter(b6.predict(X_train), b6.predict(X_train) - y_train,
            b8 = "green", s=10, label='Train data')
plt.scatter(b6.predict(X_test), b6.predict(X_test) - b5,
            b8 = "blue", s=10, label='Test data')
plt.hlines(b3 = 0, xmin=-1000, xmax=200000, linewidth=2)
plt.legend(b9 = 'upper right')
plt.title("Residual errors")
plt.show()