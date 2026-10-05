
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = regressor.predict(np.array(6.5).reshape(1, 1))
plt.scatter(b2, b3, b5 = 'orange')
plt.plot(b2, regressor.predict(b2), b5 = 'blue')
plt.title('Truth or Bluff(Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
b6 = np.arange(min(b2), max(b2), 0.1)
b6 = b6.reshape(len(b6), 1)
plt.scatter(b2, b3, b5 = 'orange')
plt.plot(b6, regressor.predict(b6), b5 = 'blue')
plt.title('Truth or Bluff(Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()