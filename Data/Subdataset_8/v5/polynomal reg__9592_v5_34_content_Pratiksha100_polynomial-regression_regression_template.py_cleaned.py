
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
predicted_salary = regressor.predict(np.array([[6.5]]))
plt.scatter(X, y, color='orange', label='Actual Data')
plt.plot(X, regressor.predict(X), color='blue', label='Regression Line')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
X_grid = np.arange(min(X), max(X), 0.1).reshape(-1, 1)
plt.scatter(X, y, color='orange', label='Actual Data')
plt.plot(X_grid, regressor.predict(X_grid), color='blue', label='Smoothed Regression Line')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()