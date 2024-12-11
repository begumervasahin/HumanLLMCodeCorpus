
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1['Level'].values.reshape(-1, 1)
b3 = b1['Salary'].values.reshape(-1, 1)
b4 = StandardScaler()
b5 = StandardScaler()
b6 = b4.fit_transform(b2)
b7 = b5.fit_transform(b3)
b8 = SVR(kernel='rbf')
b8.fit(b6, b7)
b9 = b4.transform([[6.5]])
b10 = b8.predict(b9)
b11 = b5.inverse_transform(b10)
plt.scatter(b6, b7, b12 = 'red')
plt.plot(b6, b8.predict(b6), b12 = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.show()
b13 = np.arange(min(b6), max(b6), 0.1)
b13 = b13.reshape((len(b13), 1))
plt.scatter(b6, b7, b12 = 'red')
plt.plot(b13, b8.predict(b13), b12 = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.show()