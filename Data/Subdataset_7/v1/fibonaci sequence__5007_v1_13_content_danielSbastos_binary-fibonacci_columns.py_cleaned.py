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
b3 = [fonk2(i) for i in b2]
b4 = [[int(bit) for bit in bin_number] for bin_number in b3]
b5 = np.array(b4)
def fonk3(binary_table, column_num):
    b6 = binary_table.shape[1] - 1
    b7 = binary_table[:, b6 - column_num]
    return np.trim_zeros(b7, 'f')
def fonk4(binary_table, column_num):
    b7 = fonk3(binary_table, column_num)
    b8 = 2 ** column_num
    b9 = 3 * b8
    return b7[:b9]
b10 = fonk4(b5, 4)
b11 = np.arange(len(b10))
b12 = b10
plt.bar(b11, b12, b13 = 0.6)
plt.show()