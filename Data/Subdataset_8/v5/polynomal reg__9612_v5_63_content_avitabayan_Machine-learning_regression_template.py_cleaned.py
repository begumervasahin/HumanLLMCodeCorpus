import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
Y = dataset['Salary'].values
predicted_salary = regressor.predict([[6.5]])
plt.scatter(X, Y, color='red', label='Actual data')
plt.plot(X, regressor.predict(X), color='blue', label='Regression line')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, Y, color='red', label='Actual data')
plt.plot(X_grid, regressor.predict(X_grid), color='blue', label='Regression curve')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()