
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.drop(['Position', 'Salary'], axis=1)
y = dataset['Salary']
linear_reg_model = LinearRegression()
linear_reg_model.fit(X, y)
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
poly_reg_model = LinearRegression()
poly_reg_model.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_reg_model.predict(X), color='blue')
plt.title('Linear Regression Predictions')
plt.xlabel('Position Level')
plt.ylabel('Salaries')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, poly_reg_model.predict(X_poly), color='blue')
plt.title('Polynomial Regression Predictions')
plt.xlabel('Position Level')
plt.ylabel('Salaries')
plt.show()
linear_reg_prediction = linear_reg_model.predict([[6.5]])
poly_reg_prediction = poly_reg_model.predict(poly_reg.fit_transform([[6.5]]))
print("Linear Regression Prediction for Position Level 6.5:", linear_reg_prediction)
print("Polynomial Regression Prediction for Position Level 6.5:", poly_reg_prediction)