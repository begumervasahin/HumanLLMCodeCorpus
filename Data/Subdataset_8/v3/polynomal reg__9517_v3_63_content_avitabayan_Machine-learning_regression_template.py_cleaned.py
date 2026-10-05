import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVR
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
Y = dataset['Salary'].values
regressor = SVR(kernel='rbf')
regressor.fit(X, Y)
new_position_level = [[6.5]]
predicted_salary = regressor.predict(new_position_level)
print("Predicted Salary for Position Level 6.5:", predicted_salary)
plt.scatter(X, Y, color='red', label='Actual Data')
plt.plot(X, regressor.predict(X), color='blue', label='SVR Model')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
X_grid = np.arange(min(X), max(X), 0.01).reshape(-1, 1)
plt.scatter(X, Y, color='red', label='Actual Data')
plt.plot(X_grid, regressor.predict(X_grid), color='blue', label='SVR Model')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()