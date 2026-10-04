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
b6 = b2 - b4
b7 = b3 - b5
b8 = np.sum(b6 * b7) / np.sum(b6 ** 2)
b9 = b5 - b8 * b4
b10 = b8 * b2 + b9
plt.plot(b2, b10, b11 = 'red', b12='Initial Regression Line')
plt.scatter(b2, b3, b12 = 'Data Points')
plt.xlabel('b2')
plt.ylabel('b3')
plt.title('Data Points with Initial Regression Line')
plt.legend()
plt.show()
b8 = 0
b9 = 0
a1 = 0.0001
a2 = 1000
b13 = float(len(b2))
for _ in range(a2):
    b14 = b8 * b2 + b9
    b15 = (-2 / b13) * sum(b2 * (b3 - b14))
    b16 = (-2 / b13) * sum(b3 - b14)
    b8 = b8 - a1 * b15
    b9 = b9 - a1 * b16
print(f"Final values: b8 = {b8}, b9 = {b9}")
b14 = b8 * b2 + b9
plt.scatter(b2, b3, b12 = 'Data Points')
plt.plot(b2, b14, b11 = 'red', b12='Final Regression Line')
plt.xlabel('b2')
plt.ylabel('b3')
plt.title('Data Points with Final Regression Line')
plt.legend()
plt.show()