import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1):
    a, b1 = 0, 1
    for _ in range(a1):
        a, b1 = b1, a + b1
    return a
def fonk2(number):
    return format(number, '080b')
def fonk3(a1):
    return [fonk1(i) for i in range(a1 + 1)]
def fonk4(b8):
    return np.array([[int(bit) for bit in fonk2(num)] for num in b8])
def fonk5(b9):
    plt.imshow(b9, b2 = 'nearest')
    plt.title("Binary Representation of Fibonacci Numbers")
    plt.xlabel("Bit Position")
    plt.ylabel("Fibonacci Index")
    plt.colorbar(b3 = "Bit Value")
    plt.show()
def fonk6(b9):
    b4 = [sum(row) for row in b9]
    b5 = [b9.shape[1] - sum(row) for row in b9]
    b6 = range(len(b4))
    plt.bar(b6, b4, b7 = 0.6, color='r', b3='Ones')
    plt.bar(b6, b5, b7 = 0.6, color='y', bottom=b4, b3='Zeros')
    plt.xlabel("Fibonacci Sequence Index")
    plt.ylabel("Count")
    plt.title("Histogram of Ones and Zeros in Binary Representation")
    plt.legend()
    plt.show()
def fonk7():
    a1 = 100
    b8 = fonk3(a1)
    b9 = fonk4(b8)
    fonk5(b9)
    fonk6(b9)
if b10 = = '__main__':
    fonk7()