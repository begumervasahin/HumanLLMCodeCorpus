import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 5.0)
b1 = pd.read_csv('b1.csv')
b2 = b1.iloc[:, 0]
b3 = b1.iloc[:, 1]
plt.scatter(b2, b3)
b4 = np.mean(b2)
b5 = np.mean(b3)
x_xi, b6 = b2-b4 , b3-b5
x_xi2 , b7 = x_xi * x_xi , b6*b6
b8 = np.sum((x_xi)*(b6))/np.sum(x_xi2)
b9 = b5-b8*b4
for i in b2:
	b10 = []
	b11 = b8*(b2)+b9
	b10.append(b11)
plt.scatter(b2,b10,b9 = 'r')
plt.show()
b8 = 0
b9 = 0
a1 = 0.0001
a2 = 1000
b12 = float(len(b2))
for i in range(a2):
    b13 = b8*b2 + b9
    b14 = (-2/b12) * sum(b2 * (b3 - b13))
    b15 = (-2/b12) * sum(b3 - b13)
    b8 = b8 - a1 * b14
    b9 = b9 - a1 * b15
print (b8, b9)
b13 = b8*b2 + b9
plt.scatter(b2, b3)
plt.plot([min(b2), max(b2)], [min(b13), max(b13)], b16 = 'red')
plt.show()