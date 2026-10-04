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
b4 = np.mean(b2)
b5 = np.mean(b3)
x_xi, b6 = b2 - b4, b3 - b5
b7 = np.sum(x_xi * b6) / np.sum(x_xi ** 2)
b8 = b5 - b7 * b4
b9 = b7 * b2 + b8
plt.plot(b2, b9, b10 = 'red', b15='Initial Regression Line')
plt.legend()
plt.show()
b7 = 0
b8 = 0
a1 = 0.0001
a2 = 1000
b11 = float(len(b2))
for i in range(a2):
    b12 = b7 * b2 + b8
    b13 = (-2 / b11) * sum(b2 * (b3 - b12))
    b14 = (-2 / b11) * sum(b3 - b12)
    b7 = b7 - a1 * b13
    b8 = b8 - a1 * b14
print(f"Final values: b7 = {b7}, b8 = {b8}")
b12 = b7 * b2 + b8
plt.scatter(b2, b3, b15 = 'Data Points')
plt.plot(b2, b12, b10 = 'red', b15='Final Regression Line')
plt.xlabel('b2')
plt.ylabel('b3')
plt.title('Data Points and Final Regression Line')
plt.legend()
plt.show()