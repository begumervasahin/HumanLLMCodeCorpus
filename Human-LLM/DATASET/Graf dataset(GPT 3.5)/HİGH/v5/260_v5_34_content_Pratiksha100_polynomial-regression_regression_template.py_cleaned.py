
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = regressor.predict(np.array([[6.5]]))
plt.scatter(b2, b3, b5 = 'orange', label='Actual Data')
plt.plot(b2, regressor.predict(b2), b5 = 'blue', label='Regression Line')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b6 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.scatter(b2, b3, b5 = 'orange', label='Actual Data')
plt.plot(b6, regressor.predict(b6), b5 = 'blue', label='Smoothed Regression Line')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()