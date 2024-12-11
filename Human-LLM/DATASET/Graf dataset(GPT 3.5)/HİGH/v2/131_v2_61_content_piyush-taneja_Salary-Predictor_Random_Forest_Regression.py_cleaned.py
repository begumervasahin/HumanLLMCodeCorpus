
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = RandomForestRegressor(n_estimators=300, random_state=0)
b4.fit(b2, b3)
a1 = 6.5
b5 = b4.predict([[a1]])
print("Predicted Salary for Position Level {}: ${:,.2f}".format(a1, b5[0]))
b6 = np.arange(min(b2), max(b2), 0.01).reshape(-1, 1)
plt.scatter(b2, b3, b7 = 'red', label='Actual Salaries')
plt.plot(b6, b4.predict(b6), b7 = 'blue', label='Predicted Salaries')
plt.title('Salary Prediction based on Position Level (Random Forest Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.show()