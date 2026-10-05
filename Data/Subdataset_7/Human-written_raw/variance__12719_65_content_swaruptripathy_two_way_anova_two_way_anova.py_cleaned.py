get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)
b7 = pd.read_csv('/Users/swaruptripathy/Desktop/Data Science/headbrain.csv')
print(b7.shape)
b7.head()
b2 = b7['Head Size(cm^3)'].values
b3 = b7['Brain Weight(grams)'].values
b4 = np.mean(b2)
b5 = np.mean(b3)
b6 = len(b2)
a1 = 0
a2 = 0
for i in range(b6):
    a1 += (b2[i] - b4) * (b3[i] - b5)
    a2 += (b2[i] - b4) ** 2
b7 = a1 / a2
b8 = b5 - (b7 * b4)
print(b7, b8)
b9 = np.max(b2) + 100
b10 = np.min(b2) - 100
b11 = np.linspace(b10, b9, 1000)
b12 = b8 + b7 * b11
plt.plot(b11, b12, b13 = '
plt.scatter(b2, b3, b14 = '
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
a3 = 0
for i in range(b6):
    b15 = b8 + b7 * b2[i]
    a3 += (b3[i] - b15) ** 2
a3 = np.sqrt(a3/b6)
print(a3)
a4 = 0
a5 = 0
for i in range(b6):
    b15 = b8 + b7 * b2[i]
    a4 += (b3[i] - b5) ** 2
    a5 += (b3[i] - b15) ** 2
b16 = 1 - (a5/a4)
print(b16)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
b2 = b2.reshape((b6, 1))
b17 = LinearRegression()
b17 = b17.fit(b2, b3)
b18 = b17.predict(b2)
b19 = mean_squared_error(b3, b18)
a3 = np.sqrt(b19)
b20 = b17.score(b2, b3)
print(np.sqrt(b19))
print(b20)