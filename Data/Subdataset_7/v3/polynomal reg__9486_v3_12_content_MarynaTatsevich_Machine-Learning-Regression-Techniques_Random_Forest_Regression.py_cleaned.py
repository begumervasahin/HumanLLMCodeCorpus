
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values
from sklearn.ensemble import RandomForestRegressor
b4 = RandomForestRegressor(n_estimators=10, random_state=0)
b4.fit(b2, b3)
a1 = 6.5
b5 = b4.predict([[a1]])
print(f"Predicted Salary for Level {a1}: {b5[0]}")
b6 = np.arange(min(b2), max(b2), 0.01).reshape(-1, 1)
plt.scatter(b2, b3, b7 = 'red', label='Actual Data')
plt.plot(b6, b4.predict(b6), b7 = 'blue', label='Random Forest Regression')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.legend()
plt.show()