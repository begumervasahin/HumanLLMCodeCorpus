import numpy as np
import joblib
import matplotlib.pyplot as plt
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
b10 = [b7[i] for i in np.argsort(b5)]
b11 = np.sort(b5)
b12 = range(len(b5))
plt.plot(b12, b10, b13 = 'o', b14='Predicted')
plt.plot(b12, b11, 'r', b14 = 'Actual')
plt.text(5, 20, r'R$^2$='+str('%.3f' % b8), b15 = 20)
plt.xlabel('Samples')
plt.ylabel('Values')
plt.legend()
plt.show()
np.savetxt(b3 + 'output_test.txt', (b10, b11), b16 = '%.3f')