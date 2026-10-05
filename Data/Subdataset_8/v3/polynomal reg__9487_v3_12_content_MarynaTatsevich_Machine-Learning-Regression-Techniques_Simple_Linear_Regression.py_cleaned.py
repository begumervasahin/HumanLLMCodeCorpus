import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv('Salary_Data.csv')
features = dataset['YearsExperience'].values.reshape(-1, 1)
salary = dataset['Salary'].values
X_train, X_test, y_train, y_test = train_test_split(features, salary, test_size=0.3, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
predicted_salary = regressor.predict(X_test)
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()