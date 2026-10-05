import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.drop(['Position', 'Salary'], axis=1)
y = dataset['Salary']
linreg = LinearRegression()
linreg.fit(X, y)
polyreg = PolynomialFeatures(degree=4)
X_poly = polyreg.fit_transform(X)
linreg2 = LinearRegression()
linreg2.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linreg.predict(X), color='blue')
plt.title('Linear Regression Predictions')
plt.xlabel('Position level')
plt.ylabel('Salaries')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, linreg2.predict(X_poly), color='blue')
plt.title('Polynomial Regression Predictions')
plt.xlabel('Position level')
plt.ylabel('Salaries')
plt.show()
position_level = [[6.5]]
linear_prediction = linreg.predict(position_level)[0]
polynomial_prediction = linreg2.predict(polyreg.fit_transform(position_level))[0]
print("Linear Regression Prediction for position level 6.5:", linear_prediction)
print("Polynomial Regression Prediction for position level 6.5:", polynomial_prediction)