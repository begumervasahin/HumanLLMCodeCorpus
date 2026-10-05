
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('HORA08_AGU_CO_1998-01-01_1998-12-31_1521371719602.csv')
X = dataset['Days of the Year'].values.reshape(-1, 1)
y = dataset['CO Values in AGU'].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
poly_features = PolynomialFeatures(degree=2)
X_poly_train = poly_features.fit_transform(X_train)
polynomial_model = LinearRegression()
polynomial_model.fit(X_poly_train, y_train)
plt.scatter(X_train, y_train, color='red', label='Actual Data')
plt.plot(X_train, linear_model.predict(X_train), color='blue', label='Linear Regression Model')
plt.title('Linear Regression')
plt.xlabel('Days of the Year in 1998')
plt.ylabel('CO Values in AGU')
plt.legend()
plt.show()
plt.scatter(X_train, y_train, color='red', label='Actual Data')
plt.plot(X_train, polynomial_model.predict(X_poly_train), color='blue', label='Polynomial Regression Model')
plt.title('Polynomial Regression')
plt.xlabel('Days of the Year in 1998')
plt.ylabel('CO Values in AGU')
plt.legend()
plt.show()