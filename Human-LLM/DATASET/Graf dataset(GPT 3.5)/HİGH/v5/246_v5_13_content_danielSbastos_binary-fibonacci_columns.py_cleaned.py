import numpy as np
import matplotlib.pyplot as plt
def fonk1(n):
    a, b1 = 0, 1
    for _ in range(n):
        a, b1 = b1, a + b1
    return a
def fonk2(number):
    return format(number, '080b')
a1 = 100
b2 = [fonk1(i) for i in range(a1 + 1)]
b3 = [fonk2(num) for num in b2]
b4 = np.array([[int(bit) for bit in binary] for binary in b3])
def fonk3(b4, column_number):
    b5 = b4.shape[1] - column_number - 1
    b6 = b4[:, b5]
    return np.trim_zeros(b6, 'f')
def fonk4(b4, column_number):
    b6 = fonk3(b4, column_number)
    b7 = 3 * (2 ** column_number)
    return b6[:b7]
b8 = fonk4(b4, 4)
b9 = np.arange(len(b8))
b10 = b8
plt.bar(b9, b10, b11 = 0.6)
plt.show()