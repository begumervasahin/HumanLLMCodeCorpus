
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values
scaler_X = StandardScaler()
scaler_Y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
Y_scaled = scaler_Y.fit_transform(Y.reshape(-1, 1))
regressor = SVR(kernel='rbf')
regressor.fit(X_scaled, Y_scaled)
scaled_prediction = regressor.predict(scaler_X.transform(np.array([[6.5]])))
predicted_salary = scaler_Y.inverse_transform(scaled_prediction)
plt.scatter(X_scaled, Y_scaled, color='red')
plt.plot(X_scaled, regressor.predict(X_scaled), color='blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
X_grid = np.arange(min(X_scaled), max(X_scaled), 0.01).reshape(-1, 1)
plt.scatter(X_scaled, Y_scaled, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Truth or Bluff (SVR with smoother curve)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
print("Predicted salary for position level 6.5:", predicted_salary)