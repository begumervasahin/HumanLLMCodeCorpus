
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, y)
new_position_level = 6.5
predicted_salary = regressor.predict([[new_position_level]])
print(f"Predicted Salary for Level {new_position_level}: {predicted_salary[0]}")
X_smooth = np.arange(min(X), max(X), 0.01).reshape(-1, 1)
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X_smooth, regressor.predict(X_smooth), color='blue', label='Random Forest Regression')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.legend()
plt.show()