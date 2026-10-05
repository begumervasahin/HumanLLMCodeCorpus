
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values.reshape(-1, 1)
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)
regressor = SVR(kernel='rbf')
regressor.fit(X_scaled, y_scaled)
new_data_point = np.array([[6.5]])
scaled_prediction = regressor.predict(scaler_X.transform(new_data_point))
predicted_salary = scaler_y.inverse_transform(scaled_prediction)
plt.scatter(X_scaled, y_scaled, color='red')
plt.plot(X_scaled, regressor.predict(X_scaled), color='blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.show()
X_grid = np.arange(min(X_scaled), max(X_scaled), 0.1).reshape(-1, 1)
plt.scatter(X_scaled, y_scaled, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.show()
print("Predicted Salary for Position Level 6.5:", predicted_salary[0])