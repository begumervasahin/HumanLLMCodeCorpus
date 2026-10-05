import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv('3-Products-Multiple.csv')
features = dataset.iloc[:, :-1]
target = dataset.iloc[:, 4]
city_dummies = pd.get_dummies(features['Location'], drop_first=True)
features = features.drop('Location', axis=1)
features = pd.concat([features, city_dummies], axis=1)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)
print('Coefficients:')
print(linear_reg.coef_)
variance_score = linear_reg.score(X_test, y_test)
print('Variance score:', variance_score)
predictions = linear_reg.predict(X_test)
print('Predictions:')
print(predictions)
plt.style.use('fivethirtyeight')
plt.scatter(linear_reg.predict(X_train), linear_reg.predict(X_train) - y_train,
            color="green", s=10, label='Training data')
plt.scatter(linear_reg.predict(X_test), linear_reg.predict(X_test) - y_test,
            color="blue", s=10, label='Test data')
plt.hlines(y=0, xmin=-1000, xmax=200000, linewidth=2)
plt.legend(loc='upper right')
plt.title("Residual Errors")
plt.show()