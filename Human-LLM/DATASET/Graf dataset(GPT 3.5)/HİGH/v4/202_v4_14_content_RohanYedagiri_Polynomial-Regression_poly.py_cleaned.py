
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.drop(['Position', 'Salary'], axis=1)
b3 = b1['Salary']
b4 = LinearRegression()
b4.fit(b2, b3)
b5 = PolynomialFeatures(degree=4)
b6 = b5.fit_transform(b2)
b7 = LinearRegression()
b7.fit(b6, b3)
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b4.predict(b2), b8 = 'blue')
plt.title('Linear Regression Predictions')
plt.xlabel('Position Level')
plt.ylabel('Salaries')
plt.show()
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b7.predict(b6), b8 = 'blue')
plt.title('Polynomial Regression Predictions')
plt.xlabel('Position Level')
plt.ylabel('Salaries')
plt.show()
b9 = b4.predict([[6.5]])
b10 = b7.predict(b5.fit_transform([[6.5]]))
print("Linear Regression Prediction for Position Level 6.5:", b9)
print("Polynomial Regression Prediction for Position Level 6.5:", b10)