import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_regressor = LinearRegression()
polynomial_regressor.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_regressor.predict(X), color='green')
plt.title('Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, polynomial_regressor.predict(X_poly), color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
new_position_level = 6.5
linear_prediction = linear_regressor.predict([[new_position_level]])
print(f"Linear Regression prediction for position level {new_position_level}: ${linear_prediction[0]:,.2f}")
new_position_level_poly = polynomial_features.transform([[new_position_level]])
polynomial_prediction = polynomial_regressor.predict(new_position_level_poly)
print(f"Polynomial Regression prediction for position level {new_position_level}: ${polynomial_prediction[0]:,.2f}")