import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Position_Salaries.csv')
b2 = b1.iloc[:, 1:2].values
b3 = b1.iloc[:, 2].values
from sklearn.preprocessing import StandardScaler
b4 = StandardScaler()
b5 = StandardScaler()
b2 = b4.fit_transform(b2)
b3 = b5.fit_transform(b3.reshape(-1,1))
from sklearn.svm import SVR
b6 = SVR(kernel = 'rbf')
b6.fit(b2, b3)
b7 = b5.inverse_transform(b6.predict(b4.transform(np.array([[6.5]]))))
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b2, b6.predict(b2), b8 = 'blue')
plt.title('Truth or Bluff(SVR)')
plt.xlabel('position label')
plt.ylabel('salary')
plt.show()
b9 = np.arange(min(b2), max(b2), 0.1)
b9 = b9.reshape((len(b9), 1))
plt.scatter(b2, b3, b8 = 'red')
plt.plot(b9, b6.predict(b9), b8 = 'blue')
plt.title('Truth or Bluff(Regression Model)')
plt.xlabel('position label')
plt.ylabel('salary')
plt.show()