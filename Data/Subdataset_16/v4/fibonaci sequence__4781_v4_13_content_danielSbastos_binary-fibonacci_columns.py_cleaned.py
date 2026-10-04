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
def fonk4(b8):
    return np.array([[int(bit) for bit in fonk2(num)] for num in b8])
def fonk5(b9, column_num):
    b2 = b9.shape[1] - 1
    b3 = b9[:, b2 - column_num]
    return np.trim_zeros(b3, 'f')
def fonk6(b9, column_num):
    b3 = fonk5(b9, column_num)
    b4 = 2 ** column_num
    b5 = 3 * b4
    return b3[:b5]
def fonk7(data):
    b6 = np.arange(len(data))
    plt.bar(b6, data, b7 = 0.6)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("First Digits from the Specified Column of the Binary Table")
    plt.show()
def fonk8():
    a1 = 100
    b8 = fonk3(a1)
    b9 = fonk4(b8)
    b10 = fonk6(b9, 4)
    fonk7(b10)
if b11 = = '__main__':
    fonk8()