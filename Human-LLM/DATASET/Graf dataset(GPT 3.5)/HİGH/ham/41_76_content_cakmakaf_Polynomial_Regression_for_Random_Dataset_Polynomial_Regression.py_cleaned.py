
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
np.random.seed(2)
b1 = np.random.normal(3.0, 1.0, 100)
b2 = np.random.normal(50.0, 30.0, 100) / b1
scatter(b1, b2)
b3 = b1[:80]
b4 = b1[80:]
b5 = b2[:80]
b6 = b2[80:]
scatter(b3, b5)
scatter(b4, b6)
b7 = np.array(b3)
b8 = np.array(b5)
b9 = np.poly1d(np.polyfit(b7, b8, 7))
b10 = np.linspace(0, 7, 100)
b11 = plt.b11()
b11.set_xlim([0,7])
b11.set_ylim([0, 200])
plt.scatter(b7, b8)
plt.plot(b10, b9(b10), b12 = 'b')
plt.show()
b13 = np.array(b4)
b14 = np.array(b6)
b11 = plt.b11()
b11.set_xlim([0,7])
b11.set_ylim([0, 200])
plt.scatter(b13, b14)
plt.plot(b10, b9(b10), b12 = 'b')
plt.show()
from sklearn.metrics import r2_score
b15 = r2_score(b14, b9(b13))
print(b15)
from sklearn.metrics import r2_score
b15 = r2_score(np.array(b5), b9(np.array(b3)))
print(b15)