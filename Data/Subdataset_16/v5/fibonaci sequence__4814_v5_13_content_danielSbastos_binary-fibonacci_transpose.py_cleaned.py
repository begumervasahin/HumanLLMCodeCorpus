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
def fonk4(b4):
    return np.array([[int(bit) for bit in fonk2(num)] for num in b4])
def fonk5(b5):
    plt.imshow(b5, b2 = 'nearest', cmap='viridis')
    plt.title("Binary Representation of Fibonacci Numbers (Transposed)")
    plt.xlabel("Fibonacci Sequence Index")
    plt.ylabel("Bit Position")
    plt.colorbar(b3 = "Bit Value")
    plt.show()
def fonk6():
    a1 = 100
    b4 = fonk3(a1)
    b5 = fonk4(b4)
    b6 = np.transpose(b5)
    fonk5(b6)
if b7 = = '__main__':
    fonk6()