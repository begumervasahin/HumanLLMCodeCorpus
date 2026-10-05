
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVR
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values
regressor = SVR(kernel='rbf')
regressor.fit(X, Y)
predicted_salary = regressor.predict([[6.5]])
print("Predicted Salary for Position Level 6.5:", predicted_salary)
plt.scatter(X, Y, color='red', label='Actual Data')
plt.plot(X, regressor.predict(X), color='blue', label='SVR Model')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color='red', label='Actual Data')
plt.plot(X_grid, regressor.predict(X_grid), color='blue', label='SVR Model')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()