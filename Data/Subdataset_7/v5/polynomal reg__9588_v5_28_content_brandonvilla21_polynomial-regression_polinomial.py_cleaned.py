
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.b5 import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('HORA08_AGU_CO_1998-01-01_1998-12-31_1521371719602.csv')
b2 = b1['Days of the Year'].values.reshape(-1, 1)
b3 = b1['CO Values in AGU'].values.reshape(-1, 1)
X_train, X_test, y_train, b4 = train_test_split(b2, b3, test_size=0.2, random_state=0)
b5 = LinearRegression()
b5.fit(X_train, y_train)
b6 = PolynomialFeatures(degree=2)
b7 = b6.fit_transform(X_train)
b8 = LinearRegression()
b8.fit(b7, y_train)
plt.scatter(X_train, y_train, b9 = 'red', label='Actual Data')
plt.plot(X_train, b5.predict(X_train), b9 = 'blue', label='Linear Regression Model')
plt.title('Linear Regression')
plt.xlabel('Days of the Year in 1998')
plt.ylabel('CO Values in AGU')
plt.legend()
plt.show()
plt.scatter(X_train, y_train, b9 = 'red', label='Actual Data')
plt.plot(X_train, b8.predict(b7), b9 = 'blue', label='Polynomial Regression Model')
plt.title('Polynomial Regression')
plt.xlabel('Days of the Year in 1998')
plt.ylabel('CO Values in AGU')
plt.legend()
plt.show()