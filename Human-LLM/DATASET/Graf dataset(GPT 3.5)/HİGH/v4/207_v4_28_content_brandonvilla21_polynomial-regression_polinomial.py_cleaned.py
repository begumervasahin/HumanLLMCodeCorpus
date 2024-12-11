
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('HORA08_AGU_CO_1998-01-01_1998-12-31_1521371719602.csv')
b2 = b1.iloc[:, 0:1].values
b3 = b1.iloc[:, 1:2].values
X_train, X_test, y_train, b4 = train_test_split(b2, b3, test_size=0.2, random_state=0)
b5 = LinearRegression()
b5.fit(b2, b3)
b6 = PolynomialFeatures(degree=2)
b7 = b6.fit_transform(b2)
b8 = LinearRegression()
b8.fit(b7, b3)
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b5.predict(b2), b9 = 'blue')
plt.title('Linear Regression')
plt.xlabel('Days of the Year in 1998')
plt.ylabel('CO Values in AGU')
plt.show()
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b8.predict(b6.fit_transform(b2)), b9 = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Days of the Year in 1998')
plt.ylabel('CO Values in AGU')
plt.show()