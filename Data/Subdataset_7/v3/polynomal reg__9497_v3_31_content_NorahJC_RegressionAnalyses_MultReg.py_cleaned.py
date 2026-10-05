import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
b1 = pd.read_csv('3-Products-Multiple.csv')
b2 = b1.drop(columns=['Location', 'Profit'], axis=1)
b3 = b1['Profit']
b4 = pd.get_dummies(b1['Location'], drop_first=True)
b2 = pd.concat([b2, b4], axis=1)
X_train, X_test, y_train, b5 = train_test_split(b2, b3, test_size=0.2, random_state=0)
b6 = LinearRegression()
b6.fit(X_train, y_train)
print('Coefficients:')
print(b6.coef_)
b7 = b6.score(X_test, b5)
print('Variance score:', b7)
b8 = b6.predict(X_test)
print('Predictions:')
print(b8)
plt.style.use('fivethirtyeight')
plt.scatter(b6.predict(X_train), b6.predict(X_train) - y_train,
            b9 = "green", s=10, label='Training data')
plt.scatter(b6.predict(X_test), b6.predict(X_test) - b5,
            b9 = "blue", s=10, label='Test data')
plt.hlines(b10 = 0, xmin=-1000, xmax=200000, linewidth=2)
plt.legend(b11 = 'upper right')
plt.title("Residual Errors")
plt.show()