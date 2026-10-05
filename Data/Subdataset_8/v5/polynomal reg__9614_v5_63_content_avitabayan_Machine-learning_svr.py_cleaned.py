
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset['Level'].values.reshape(-1, 1)
Y = dataset['Salary'].values.reshape(-1, 1)
scaler_X = StandardScaler()
scaler_Y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
Y_scaled = scaler_Y.fit_transform(Y)
regressor = SVR(kernel='rbf')
regressor.fit(X_scaled, Y_scaled)
scaled_input = scaler_X.transform([[6.5]])
scaled_prediction = regressor.predict(scaled_input)
Y_pred = scaler_Y.inverse_transform(scaled_prediction)
plt.scatter(X_scaled, Y_scaled, color='red')
plt.plot(X_scaled, regressor.predict(X_scaled), color='blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.show()
X_grid = np.arange(min(X_scaled), max(X_scaled), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_scaled, Y_scaled, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.show()