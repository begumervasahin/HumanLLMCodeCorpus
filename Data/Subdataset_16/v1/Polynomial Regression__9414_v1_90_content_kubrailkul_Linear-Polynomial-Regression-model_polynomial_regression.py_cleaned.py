import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = pd.read_csv("C:/Users/pc/Desktop/kurs/HW1_DATA.csv")
b2 = b1['b2']
b3 = b1['b3']
plt.plot(b2, b3, '.')
plt.show()
b4 = np.sum(b2)
b5 = np.sum(b3)
b6 = b3.dot(b2)
def fonk1(num):
    return num / 1000
b7 = fonk1(b2.dot(b2)) - fonk1(b4)**2
b8 = fonk1(b6) - fonk1(b4) * fonk1(b5)
b8 = b8 / b7
b9 = fonk1(b5) * fonk1(b2.dot(b2)) - fonk1(b6) * fonk1(b4)
b9 = b9 / b7
b10 = b8 * b2 + b9
plt.plot(b2, b3, '.')
plt.plot(b2, b10, '.')
plt.show()
b11 = np.sum((b3 - b10)**2)
b12 = np.sum((b3 - fonk1(b5))**2)
b13 = 1 - b11 / b12
def fonk2(p, b2):
    b10 = 0
    b14 = len(p) - 1
    for i in range(len(p)):
        b10 = b10 + p[i] * b2**(b14 - i)
    return b10
def fonk3(b10, b3, b12):
    b11 = np.sum((b3 - b10)**2)
    return 1 - b11 / b12
b15 = np.b15(1000)
b16 = np.c_[b2, b15]
b17 = np.linalg.solve(np.transpose(b16).dot(b16), np.transpose(b16).dot(b3))
print(b17)
for degree in range(2, 8):
    b16 = np.c_[b2**degree, b16]
    b17 = np.linalg.solve(np.transpose(b16).dot(b16), np.transpose(b16).dot(b3))
    print(b17)
b18 = fonk2(b17, b2)
b19 = fonk3(b18, b3, b12)
plt.plot(b2, b3, '.', b20 = 'b9')
plt.plot(b2, b18, '.', b20 = 'g')
plt.show()