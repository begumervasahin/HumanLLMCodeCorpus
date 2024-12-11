
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = StandardScaler()
b5 = StandardScaler()
b6 = b4.fit_transform(b2)
b7 = b5.fit_transform(b3.reshape(-1, 1)).flatten()
b8 = SVR(kernel='rbf')
b8.fit(b6, b7)
b9 = np.array([[6.5]])
b10 = b4.transform(b9)
b11 = b8.predict(b10)
b12 = b5.inverse_transform(b11.reshape(1, -1))
plt.scatter(b6, b7, b13 = 'red', label='Actual Data')
plt.plot(b6, b8.predict(b6), b13 = 'blue', label='SVR Prediction')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.legend()
plt.show()
b14 = np.arange(min(b6), max(b6), 0.01).reshape(-1, 1)
plt.scatter(b6, b7, b13 = 'red', label='Actual Data')
plt.plot(b14, b8.predict(b14), b13 = 'blue', label='SVR Prediction')
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.legend()
plt.show()