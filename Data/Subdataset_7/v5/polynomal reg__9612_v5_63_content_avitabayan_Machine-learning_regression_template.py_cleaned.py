import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
b4 = regressor.predict([[6.5]])
plt.scatter(b2, b3, b5 = 'red', label='Actual data')
plt.plot(b2, regressor.predict(b2), b5 = 'blue', label='Regression line')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()
b6 = np.arange(min(b2), max(b2), 0.1).reshape(-1, 1)
plt.scatter(b2, b3, b5 = 'red', label='Actual data')
plt.plot(b6, regressor.predict(b6), b5 = 'blue', label='Regression curve')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()