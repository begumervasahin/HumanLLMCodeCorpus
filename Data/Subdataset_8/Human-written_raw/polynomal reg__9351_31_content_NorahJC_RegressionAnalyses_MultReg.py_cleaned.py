import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, metrics
dataset = pd.read_csv('3-Products-Multiple.csv')
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 4]
cities = pd.get_dummies(X['Location'], drop_first=True)
X = X.drop('Location', axis=1)
X = pd.concat([X, cities], axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
from sklearn.linear_model import LinearRegression
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
print('Coefficients: \n', reg.coef_)
print('Variance score: {}'.format(reg.score(X_test, y_test)))
y_pred = reg.predict(X_test)
print('Prediction: ')
print(y_pred)
print('Based on the results, product_1 would yield a better profit at a particular city  and overall.')
plt.style.use('fivethirtyeight')
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train,
            color="green", s=10, label='Train data')
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test,
            color="blue", s=10, label='Test data')
plt.hlines(y=0, xmin=-1000, xmax=200000, linewidth=2)
plt.legend(loc='upper right')
plt.title("Residual errors")
plt.show()