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
def fonk4(b7):
    return np.array([[int(bit) for bit in fonk2(num)] for num in b7])
def fonk5(b8):
    plt.imshow(b8, b2 = 'nearest')
    plt.title("Binary Representation of Fibonacci Numbers")
    plt.show()
def fonk6(b8):
    b3 = [sum(row) for row in b8]
    b4 = [b8.shape[1] - sum(row) for row in b8]
    b5 = list(range(len(b3)))
    plt.bar(b5, b3, b6 = 0.6, color='r', label='Ones')
    plt.bar(b5, b4, b6 = 0.6, color='y', bottom=b3, label='Zeros')
    plt.xlabel("Fibonacci Sequence Index")
    plt.ylabel("Count")
    plt.title("Histogram of Ones and Zeros in Binary Representation")
    plt.legend()
    plt.show()
def fonk7():
    a1 = 100
    b7 = fonk3(a1)
    b8 = fonk4(b7)
    fonk5(b8)
    fonk6(b8)
if b9 = = '__main__':
    fonk7()