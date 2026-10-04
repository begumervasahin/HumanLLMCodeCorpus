import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
b1 = pd.read_csv('Data.csv')
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, 1].values
X_train, X_test, y_train, b4 = train_test_split(b2, b3, test_size=1/3, random_state=0)
b5 = LinearRegression()
b5.fit(X_train, y_train)
b6 = b5.predict(X_test)
plt.figure(b7 = (10, 6))
plt.scatter(X_train, y_train, b8 = 'red', label='Actual Data')
plt.plot(X_train, b5.predict(X_train), b8 = 'blue', label='Regression Line')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.figure(b7 = (10, 6))
plt.scatter(X_test, b4, b8 = 'red', label='Actual Data')
plt.plot(X_train, b5.predict(X_train), b8 = 'blue', label='Regression Line')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()