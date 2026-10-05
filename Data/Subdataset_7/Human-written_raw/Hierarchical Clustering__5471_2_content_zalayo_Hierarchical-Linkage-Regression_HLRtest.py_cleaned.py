import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score as r2
b1 = './model/'
b2 = './input/'
b3 = './output/'
with open(b2 + 'linkages.txt') as file:
        b4 = np.array([[float(digit) for digit in line.split()] for line in file])
b5 = np.genfromtxt(b2 + 'b5.txt')
b6 = joblib.load(b1 + 'b6.sav')
b7 = b6.predict(b4)
b8 = r2(b5, b7)
print('R^2: b9 = %.3f' % b8)
b10 = list()
b11 = np.argsort(b5, axis=-1)
b12 = np.sort(b5, axis=-1)
for i in b11:
    b10.append(b7[i])
b13 = range(len(b11))
plt.plot(b13, b10, b14 = 'o')
plt.plot(b13, b12, 'r')
plt.text(5, 20, r'R$^2$='+str('%.3f' % b8), b15 = 20)
plt.show()
np.savetxt(b3 + 'output_test.txt', (b10, b12), b16 = '%.3f')