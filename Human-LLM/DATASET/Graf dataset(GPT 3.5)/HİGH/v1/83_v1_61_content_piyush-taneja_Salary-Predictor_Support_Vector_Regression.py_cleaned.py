import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values.reshape(-1, 1)
b4 = StandardScaler()
b5 = StandardScaler()
b2 = b4.fit_transform(b2)
b3 = b5.fit_transform(b3)
b6 = SVR(kernel='rbf')
b6.fit(b2, b3)
b7 = b6.predict(b4.transform(np.array([[6.5]])))
b8 = b5.inverse_transform(b7)
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b2, b6.predict(b2), b9 = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
b10 = np.arange(min(b2), max(b2), 0.1)
b10 = b10.reshape(len(b10), 1)
plt.scatter(b2, b3, b9 = 'red')
plt.plot(b10, b6.predict(b10), b9 = 'blue')
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
print("Predicted Salary for Position Level 6.5:", b8[0])