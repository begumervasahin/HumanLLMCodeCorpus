import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset[['Level']]
y = dataset['Salary']
linear_model = LinearRegression()
linear_model.fit(X, y)
polynomial_features = PolynomialFeatures(degree=4)
X_poly = polynomial_features.fit_transform(X)
polynomial_model = LinearRegression()
polynomial_model.fit(X_poly, y)
plt.scatter(X, y, color='red')
plt.plot(X, linear_model.predict(X), color='blue')
plt.title('Linear Regression Predictions')
plt.xlabel('Position level')
plt.ylabel('Salaries')
plt.show()
plt.scatter(X, y, color='red')
plt.plot(X, polynomial_model.predict(X_poly), color='blue')
plt.title('Polynomial Regression Predictions')
plt.xlabel('Position level')
plt.ylabel('Salaries')
plt.show()
position_level = [[6.5]]
linear_prediction = linear_model.predict(position_level)[0]
polynomial_prediction = polynomial_model.predict(polynomial_features.transform(position_level))[0]
print("Linear Regression Prediction for position level 6.5:", linear_prediction)
print("Polynomial Regression Prediction for position level 6.5:", polynomial_prediction)