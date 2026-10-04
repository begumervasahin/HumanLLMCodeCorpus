import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
b1 = './model/'
b2 = './input/'
b3 = './output/'
with open(b2 + 'linkages.txt') as file:
    b4 = np.array([[float(value) for value in line.split()] for line in file])
b5 = np.genfromtxt(b2 + 'y.txt')
b6 = joblib.load(b1 + 'b6.sav')
b7 = b6.predict(b4)
b8 = r2_score(b5, b7)
print(f'R^2 Score: {b8:.3f}')
b9 = np.argsort(b5)
b10 = b5[b9]
b11 = b7[b9]
plt.figure(b12 = (10, 6))
plt.plot(b9, b11, b13 = 'o', linestyle='-', label='Predicted Values')
plt.plot(b9, b10, b14 = 'red', linestyle='-', label='Actual Values')
plt.text(5, 20, f'R$^2$ = {b8:.3f}', b15 = 20)
plt.legend()
plt.title('Predicted vs Actual Values')
plt.xlabel('Sample Index')
plt.ylabel('Values')
plt.grid(True)
plt.show()
b16 = np.column_stack((b11, b10))
np.savetxt(b3 + 'output_test.txt', b16, b17 = '%.3f')