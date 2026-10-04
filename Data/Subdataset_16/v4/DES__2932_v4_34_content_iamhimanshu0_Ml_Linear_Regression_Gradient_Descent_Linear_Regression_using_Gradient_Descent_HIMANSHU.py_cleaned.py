import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 5.0)
b1 = pd.read_csv('b1.csv')
b2 = b1.iloc[:, 0]
b3 = b1.iloc[:, 1]
plt.scatter(b2, b3)
plt.xlabel('b2')
plt.ylabel('b3')
plt.title('Data Points')
plt.show()
b4 = np.mean(b2)
b5 = np.mean(b3)
b6 = b2 - b4
b7 = b3 - b5
b8 = np.sum(b6 * b7) / np.sum(b6 ** 2)
b9 = b5 - b8 * b4
b10 = b8 * b2 + b9
plt.scatter(b2, b3, b11 = 'Data Points')
plt.plot(b2, b10, b12 = 'red', b11='Initial Regression Line')
plt.xlabel('b2')
plt.ylabel('b3')
plt.title('Data Points with Initial Regression Line')
plt.legend()
plt.show()
a1 = 0
a2 = 0
a3 = 0.0001
a4 = 1000
b13 = float(len(b2))
for _ in range(a4):
    b14 = a1 * b2 + a2
    b15 = (-2 / b13) * sum(b2 * (b3 - b14))
    b16 = (-2 / b13) * sum(b3 - b14)
    a1 = a1 - a3 * b15
    a2 = a2 - a3 * b16
print(f"Final values: a1 = {a1}, a2 = {a2}")
b17 = a1 * b2 + a2
plt.scatter(b2, b3, b11 = 'Data Points')
plt.plot(b2, b17, b12 = 'red', b11='Final Regression Line')
plt.xlabel('b2')
plt.ylabel('b3')
plt.title('Data Points with Final Regression Line')
plt.legend()
plt.show()