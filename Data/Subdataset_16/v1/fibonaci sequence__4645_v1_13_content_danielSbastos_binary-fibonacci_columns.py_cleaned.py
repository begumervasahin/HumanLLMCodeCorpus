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
def fonk3(a1):
    return [fonk1(i) for i in range(a1 + 1)]
def fonk4(b12):
    b2 = [fonk2(i) for i in b12]
    b3 = []
    for bin_number in b2:
        b4 = [int(bit) for bit in bin_number]
        b3.append(b4)
    return np.array(b3)
def fonk5(binary_table, column_num):
    b5 = binary_table.shape[1] - 1
    b6 = binary_table[:, b5 - column_num]
    return np.trim_zeros(b6, 'f')
def fonk6(binary_table, column_num):
    b6 = fonk5(binary_table, column_num)
    b7 = 2 ** column_num
    b8 = 3 * b7
    return b6[:b8]
def fonk7(data):
    b9 = np.arange(len(data))
    b10 = data
    plt.bar(b9, b10, b11 = 0.6)
    plt.show()
def fonk8():
    a1 = 100
    b12 = fonk3(a1)
    b13 = fonk4(b12)
    b14 = fonk6(b13, 4)
    fonk7(b14)
if b15 = = '__main__':
    fonk8()