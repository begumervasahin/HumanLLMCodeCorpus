import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = RandomForestRegressor(n_estimators=300, random_state=0)
b4.fit(b2, b3)
b5 = b4.predict([[6.5]])
print("Predicted Salary:", b5)
b6 = np.arange(min(b2), max(b2), 0.01)
b6 = b6.reshape((len(b6), 1))
plt.scatter(b2, b3, b7 = 'red')
plt.plot(b6, b4.predict(b6), b7 = 'blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()