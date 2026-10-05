
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, y)
predicted_salary = regressor.predict([[6.5]])
X_grid = np.arange(min(X), max(X), 0.01).reshape(-1, 1)
plt.scatter(X, y, color='red', label='Actual data')
plt.plot(X_grid, regressor.predict(X_grid), color='blue', label='Predicted curve')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()