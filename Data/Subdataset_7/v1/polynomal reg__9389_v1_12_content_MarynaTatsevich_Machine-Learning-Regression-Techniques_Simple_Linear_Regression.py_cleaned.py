import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
b1 = pd.read_csv('Salary_Data.csv')
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, 1].values
X_train, X_test, y_train, b4 = train_test_split(b2, b3, test_size=0.3, random_state=0)
b5 = LinearRegression()
b5.fit(X_train, y_train)
b6 = b5.predict(X_test)
plt.scatter(X_train, y_train, b7 = 'red')
plt.plot(X_train, b5.predict(X_train), b7 = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
plt.scatter(X_test, b4, b7 = 'red')
plt.plot(X_train, b5.predict(X_train), b7 = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()