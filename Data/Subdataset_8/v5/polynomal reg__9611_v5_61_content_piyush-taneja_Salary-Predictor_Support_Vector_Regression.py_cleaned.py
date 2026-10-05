
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
y = dataset['Salary'].values
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).flatten()
regressor = SVR(kernel='rbf')
regressor.fit(X_scaled, y_scaled)
new_X = np.array([[6.5]])
scaled_new_X = scaler_X.transform(new_X)
predicted_salary_scaled = regressor.predict(scaled_new_X)
predicted_salary = scaler_y.inverse_transform(predicted_salary_scaled.reshape(1, -1))
plt.scatter(X_scaled, y_scaled, color='red', label='Actual Data')
plt.plot(X_scaled, regressor.predict(X_scaled), color='blue', label='SVR Prediction')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.legend()
plt.show()
X_grid = np.arange(min(X_scaled), max(X_scaled), 0.01).reshape(-1, 1)
plt.scatter(X_scaled, y_scaled, color='red', label='Actual Data')
plt.plot(X_grid, regressor.predict(X_grid), color='blue', label='SVR Prediction')
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.legend()
plt.show()