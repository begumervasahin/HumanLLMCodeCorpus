import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import b8 as r2
b1 = './model/'
b2 = './input/'
b3 = './output/'
with open(b2 + 'b4.txt') as file:
    b4 = np.array([[float(digit) for digit in line.split()] for line in file])
b5 = np.genfromtxt(b2 + 'y.txt')
b6 = joblib.load(b1 + 'b6.sav')
b7 = b6.predict(b4)
b8 = r2(b5, b7)
print(f'R^2: b9 = {b8:.3f}')
b10 = np.argsort(b5)
b11 = [b7[i] for i in b10]
b12 = np.sort(b5)
b13 = range(len(b5))
plt.plot(b13, b11, b14 = 'o', b15='Predicted')
plt.plot(b13, b12, 'r', b15 = 'Actual')
plt.text(5, 20, f'R$^2$={b8:.3f}', b16 = 20)
plt.xlabel('Samples')
plt.ylabel('Values')
plt.legend()
plt.show()
np.savetxt(b3 + 'output_test.txt', (b11, b12), b17 = '%.3f')