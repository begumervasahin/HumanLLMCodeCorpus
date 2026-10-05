import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('HORA08_AGU_CO_1998-01-01_1998-12-31_1521371719602.csv')
X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1:2].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)
poly_regressor = LinearRegression()
poly_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_regressor.predict(X), color='blue')
plt.title('Linear Regression')
plt.xlabel('Days of Year 1998')
plt.ylabel('CO Values in AGU')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, poly_regressor.predict(poly_features.transform(X)), color='blue')
plt.title('Polynomial Regression (Degree 2)')
plt.xlabel('Days of Year 1998')
plt.ylabel('CO Values in AGU')
plt.show()