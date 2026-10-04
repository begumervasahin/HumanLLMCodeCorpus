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
def fonk4(b5):
    b2 = [[int(bit) for bit in fonk2(num)] for num in b5]
    return np.array(b2)
def fonk5(b6):
    plt.imshow(b6, b3 = 'nearest')
    plt.title("Binary Representation of Fibonacci Numbers (Transposed)")
    plt.xlabel("Fibonacci Sequence Index")
    plt.ylabel("Bit Position")
    plt.colorbar(b4 = "Bit Value")
    plt.show()
def fonk6():
    a1 = 100
    b5 = fonk3(a1)
    b6 = fonk4(b5)
    b7 = np.transpose(b6)
    fonk5(b7)
if b8 = = '__main__':
    fonk6()