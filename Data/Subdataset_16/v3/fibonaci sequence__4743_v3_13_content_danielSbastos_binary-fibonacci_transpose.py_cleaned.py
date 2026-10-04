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
def fonk4(b9):
    b2 = [[int(bit) for bit in fonk2(num)] for num in b9]
    return np.array(b2)
def fonk5(b10):
    plt.imshow(b10, b3 = 'nearest')
    plt.title("Binary Representation of Fibonacci Numbers")
    plt.xlabel("Bit Position")
    plt.ylabel("Fibonacci Index")
    plt.colorbar(b4 = "Bit Value")
    plt.show()
def fonk6(b10):
    b5 = [sum(row) for row in b10]
    b6 = [b10.shape[1] - sum(row) for row in b10]
    b7 = range(len(b5))
    plt.bar(b7, b5, b8 = 0.6, color='r', b4='Ones')
    plt.bar(b7, b6, b8 = 0.6, color='y', bottom=b5, b4='Zeros')
    plt.xlabel("Fibonacci Sequence Index")
    plt.ylabel("Count")
    plt.title("Histogram of Ones and Zeros in Binary Representation")
    plt.legend()
    plt.show()
def fonk7():
    a1 = 100
    b9 = fonk3(a1)
    b10 = fonk4(b9)
    fonk5(b10)
    fonk6(b10)
if b11 = = '__main__':
    fonk7()