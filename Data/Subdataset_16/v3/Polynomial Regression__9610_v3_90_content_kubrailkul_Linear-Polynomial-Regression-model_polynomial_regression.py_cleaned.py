import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.read_csv("C:/Users/pc/Desktop/kurs/HW1_DATA.csv")
b2 = b1['b2']
b3 = b1['b3']
plt.plot(b2, b3, '.')
plt.title("Original Data")
plt.xlabel("b2")
plt.ylabel("b3")
plt.show()
def fonk1(num):
    return num / len(b2)
b4 = np.sum(b2)
b5 = np.sum(b3)
b6 = b3.dot(b2)
b7 = fonk1(b2.dot(b2)) - fonk1(b4)**2
b8 = (fonk1(b6) - fonk1(b4) * fonk1(b5)) / b7
b9 = (fonk1(b5) * fonk1(b2.dot(b2)) - fonk1(b6) * fonk1(b4)) / b7
b10 = b8 * b2 + b9
plt.plot(b2, b3, '.', b11 = "Original Data")
plt.plot(b2, b10, '.', b11 = "Linear Fit")
plt.title("Linear Regression Fit")
plt.xlabel("b2")
plt.ylabel("b3")
plt.legend()
plt.show()
b12 = np.sum((b3 - b10)**2)
b13 = np.sum((b3 - fonk1(b5))**2)
b14 = 1 - b12 / b13
print(f"R-squared for linear fit: {b14:.4f}")
def fonk2(p, b2):
    b10 = 0
    b15 = len(p) - 1
    for i in range(len(p)):
        b10 += p[i] * b2**(b15 - i)
    return b10
b16 = np.b16(len(b2))
b17 = np.c_[b2, b16]
def fonk3(b2, b3, degree):
    b17 = np.vander(b2, degree + 1)
    b18 = np.linalg.solve(np.transpose(b17).dot(b17), np.transpose(b17).dot(b3))
    return b18
for degree in range(1, 8):
    b18 = fonk3(b2, b3, degree)
    print(f"Coefficients for degree {degree}: {b18}")
b18 = fonk3(b2, b3, 7)
b19 = fonk2(b18, b2)
b20 = rsquare(b19, b3, b13)
plt.plot(b2, b3, '.', b21 = 'b9', b11="Original Data")
plt.plot(b2, b19, '.', b21 = 'g', b11="Polynomial Fit (degree 7)")
plt.title("Polynomial Regression Fit")
plt.xlabel("b2")
plt.ylabel("b3")
plt.legend()
plt.show()
print(f"R-squared for polynomial fit (degree 7): {b20:.4f}")