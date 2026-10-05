import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = RandomForestRegressor(n_estimators=10, random_state=0)
b4.fit(b2, b3)
b5 = b4.predict([[6.5]])
print("Predicted Salary for 6.5 years of experience:", b5)
plt.scatter(b2, b3, b6 = 'red')
plt.plot(b2, b4.predict(b2), b6 = 'blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
b7 = np.arange(min(b2), max(b2), 0.01)
b7 = b7.reshape((len(b7), 1))
plt.scatter(b2, b3, b6 = 'red')
plt.plot(b7, b4.predict(b7), b6 = 'blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()