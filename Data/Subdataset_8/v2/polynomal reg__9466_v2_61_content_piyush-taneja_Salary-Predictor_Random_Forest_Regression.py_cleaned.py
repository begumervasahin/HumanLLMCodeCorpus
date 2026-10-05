
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
regressor = RandomForestRegressor(n_estimators=300, random_state=0)
regressor.fit(X, y)
new_position_level = 6.5
predicted_salary = regressor.predict([[new_position_level]])
print("Predicted Salary for Position Level {}: ${:,.2f}".format(new_position_level, predicted_salary[0]))
X_grid = np.arange(min(X), max(X), 0.01).reshape(-1, 1)
plt.scatter(X, y, color='red', label='Actual Salaries')
plt.plot(X_grid, regressor.predict(X_grid), color='blue', label='Predicted Salaries')
plt.title('Salary Prediction based on Position Level (Random Forest Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()