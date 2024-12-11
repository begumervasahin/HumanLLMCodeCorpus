import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVR
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = SVR(kernel='rbf')
b4.fit(b2, b3)
b5 = [[6.5]]
b6 = b4.predict(b5)
print("Predicted Salary for Position Level 6.5:", b6)
plt.scatter(b2, b3, b7 = 'red', label='Actual Data')
plt.plot(b2, b4.predict(b2), b7 = 'blue', label='SVR Model')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b8 = np.arange(min(b2), max(b2), 0.01).reshape(-1, 1)
plt.scatter(b2, b3, b7 = 'red', label='Actual Data')
plt.plot(b8, b4.predict(b8), b7 = 'blue', label='SVR Model')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()