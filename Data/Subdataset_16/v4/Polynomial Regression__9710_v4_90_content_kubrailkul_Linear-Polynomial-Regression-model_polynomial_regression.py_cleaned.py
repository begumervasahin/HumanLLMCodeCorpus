import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import linalg
b1 = pd.read_csv("C:/Users/pc/Desktop/kurs/HW1_DATA.csv")
b2 = b1['b2'].values
b3 = b1['b3'].values
plt.scatter(b2, b3, b4 = 'b11', b19='Data')
plt.xlabel('b2')
plt.ylabel('b3')
plt.show()
b5 = np.mean(b2)
b6 = np.mean(b3)
b7 = np.mean(b2 * b3)
b8 = np.mean(b2**2)
b9 = b8 - b5**2
b10 = (b7 - b5 * b6) / b9
b11 = (b6 * b8 - b7 * b5) / b9
b12 = b10 * b2 + b11
plt.scatter(b2, b3, b4 = 'b11', b19='Data')
plt.plot(b2, b12, b4 = 'r', b19='Linear Fit')
plt.xlabel('b2')
plt.ylabel('b3')
plt.legend()
plt.show()
b13 = np.sum((b3 - b12)**2)
b14 = np.sum((b3 - b6)**2)
b15 = 1 - b13 / b14
print(f"Linear Fit R-squared: {b15}")
def fonk1(p, b2):
    b12 = np.polyval(p, b2)
    return b12
def fonk2(b12, b3):
    b13 = np.sum((b3 - b12)**2)
    b14 = np.sum((b3 - np.mean(b3))**2)
    return 1 - b13 / b14
for degree in range(1, 8):
    b16 = np.polyfit(b2, b3, degree)
    b17 = fonk1(b16, b2)
    b18 = fonk2(b17, b3)
    print(f"Degree {degree} Polynomial Coefficients: {b16}")
    print(f"Degree {degree} Polynomial R-squared: {b18}")
    plt.scatter(b2, b3, b4 = 'b11', b19='Data')
    plt.plot(b2, b17, b19 = f'Degree {degree} Polynomial Fit')
    plt.xlabel('b2')
    plt.ylabel('b3')
    plt.legend()
    plt.show()