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
    b2 = []
    for num in b7:
        b3 = fonk2(num)
        b4 = [int(bit) for bit in b3]
        b2.append(b4)
    return np.array(b2)
def fonk5(b8):
    plt.imshow(b8, b5 = 'nearest')
    plt.title("Binary Representation of Fibonacci Numbers (Transposed)")
    plt.xlabel("Fibonacci Sequence Index")
    plt.ylabel("Bit Position")
    plt.colorbar(b6 = "Bit Value")
    plt.show()
def fonk6():
    a1 = 100
    b7 = fonk3(a1)
    b8 = fonk4(b7)
    b9 = np.transpose(b8)
    fonk5(b9)
if b10 = = '__main__':
    fonk6()