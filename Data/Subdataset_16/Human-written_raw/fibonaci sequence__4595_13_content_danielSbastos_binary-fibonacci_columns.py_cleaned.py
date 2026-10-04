import numpy as np
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
b3 = [fonk2(i) for i in b2]
b4 = []
for bin_number in b3:
    b5 = []
    for i in bin_number:
        b5.append(int(i))
    b4.append(b5)
b6 = np.array(b4)
def fonk3(binary_table, column_num):
    b7 = binary_table.shape[1] - 1
    b8 = binary_table[:, b7 - column_num]
    return np.trim_zeros(b8, 'f')
def fonk4(binary_table, column_num):
    b8 = fonk3(binary_table, column_num)
    b9 = 2 ** column_num
    b10 = 3 * b9
    return b8[:b10]
b11 = fonk4(b6, 4)
b12 = np.arange(len(b11))
b13 = b11
import matplotlib.pyplot as plt
plt.bar(b12, b13, b14 = 0.6)
plt.show()