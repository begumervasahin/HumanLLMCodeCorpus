import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
b1 = './model/'
b2 = './input/'
b3 = './output/'
with open(b2 + 'linkages.txt') as file:
    b4 = np.array([[float(digit) for digit in line.split()] for line in file])
b5 = np.genfromtxt(b2 + 'b5.txt')
b6 = joblib.load(b1 + 'b6.sav')
b7 = b6.predict(b4)
b8 = r2_score(b5, b7)
print(f'R^2: b9 = {b8:.3f}')
b10 = np.argsort(b5)
b11 = np.sort(b5)
b12 = b7[b10]
b13 = range(len(b10))
plt.plot(b13, b12, b14 = 'o', b15='Predicted')
plt.plot(b13, b11, 'r', b15 = 'Actual')
plt.text(5, 20, f'R$^2$={b8:.3f}', b16 = 20)
plt.legend()
plt.show()
b17 = np.vstack((b12, b11)).T
np.savetxt(b3 + 'output_test.txt', b17, b18 = '%.3f')