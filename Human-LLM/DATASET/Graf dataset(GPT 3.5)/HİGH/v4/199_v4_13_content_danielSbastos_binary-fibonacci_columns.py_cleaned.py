import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1):
    a, b1 = 0, 1
    while a1 > 0:
        a, b1 = b1, a + b1
        a1 -= 1
    return a
def fonk2(number):
    return format(number, '080b')
a1 = 100
b2 = [fonk1(i) for i in range(a1 + 1)]
b3 = [fonk2(num) for num in b2]
b4 = np.array([[int(bit) for bit in binary_num] for binary_num in b3])
def fonk3(b4, column_number):
    b5 = b4.shape[1] - 1
    b6 = b4[:, b5 - column_number]
    return np.trim_zeros(b6, 'f')
def fonk4(b4, column_number):
    b6 = fonk3(b4, column_number)
    b7 = 2 ** column_number
    b8 = 3 * b7
    return b6[:b8]
b9 = fonk4(b4, 4)
b10 = np.arange(len(b9))
b11 = b9
plt.bar(b10, b11, b12 = 0.6)
plt.show()