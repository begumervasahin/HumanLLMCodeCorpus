
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
dataset = pd.read_csv('Position_Salaries.csv')
years_experience = dataset['Level'].values.reshape(-1, 1)
salary = dataset['Salary'].values
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(years_experience, salary)
predicted_salary = regressor.predict([[6.5]])
print("Predicted Salary for 6.5 years of experience:", predicted_salary)
plt.scatter(years_experience, salary, color='red', label='Actual')
plt.plot(years_experience, regressor.predict(years_experience), color='blue', label='Predicted')
plt.title('Salary Prediction using Random Forest Regression')
plt.xlabel('Years of Experience (Level)')
plt.ylabel('Salary')
plt.legend()
plt.show()
x_values = np.arange(min(years_experience), max(years_experience), 0.01).reshape(-1, 1)
plt.scatter(years_experience, salary, color='red', label='Actual')
plt.plot(x_values, regressor.predict(x_values), color='blue', label='Predicted')
plt.title('Salary Prediction using Random Forest Regression (Higher Resolution)')
plt.xlabel('Years of Experience (Level)')
plt.ylabel('Salary')
plt.legend()
plt.show()