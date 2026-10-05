import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
b4 = StandardScaler()
b5 = StandardScaler()
b6 = b4.fit_transform(b2)
b7 = b5.fit_transform(b3.reshape(-1, 1)).reshape(-1)
b8 = SVR(kernel='rbf')
b8.fit(b6, b7)
b9 = b8.predict(b4.transform(np.array([[6.5]])))
b10 = b5.inverse_transform(b9.reshape(-1, 1))[0][0]
print("Predicted salary for level 6.5:", b10)
plt.scatter(b6, b7, b11 = 'red', label='Data Points')
plt.plot(b6, b8.predict(b6), b11 = 'blue', label='SVR Regression Line')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.legend()
plt.show()
b12 = np.arange(min(b6), max(b6), 0.01).reshape(-1, 1)
plt.scatter(b6, b7, b11 = 'red', label='Data Points')
plt.plot(b12, b8.predict(b12), b11 = 'blue', label='SVR Regression Curve')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level (Scaled)')
plt.ylabel('Salary (Scaled)')
plt.legend()
plt.show()