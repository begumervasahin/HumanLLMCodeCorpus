import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVR
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = SVR(kernel='rbf')
b4.fit(b2, b3)
b5 = b4.predict([[6.5]])
print("Predicted Salary for Position Level 6.5:", b5)
plt.scatter(b2, b3, b6 = 'red', label='Actual Data')
plt.plot(b2, b4.predict(b2), b6 = 'blue', label='SVR Model')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b7 = np.arange(min(b2), max(b2), 0.01)
b7 = b7.reshape((len(b7), 1))
plt.scatter(b2, b3, b6 = 'red', label='Actual Data')
plt.plot(b7, b4.predict(b7), b6 = 'blue', label='SVR Model')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()