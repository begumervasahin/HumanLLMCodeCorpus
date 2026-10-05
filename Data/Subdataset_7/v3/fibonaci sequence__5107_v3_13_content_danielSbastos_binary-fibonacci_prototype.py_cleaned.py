import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1):
    b1 = [0, 1]
    for _ in range(2, a1 + 1):
        b1.append(b1[-1] + b1[-2])
    return b1
def fonk2(b1, b2 = 80):
    return [format(number, f'0{b2}b') for number in b1]
def fonk3(b10):
    return np.array([[int(bit) for bit in string] for string in b10])
def fonk4(matrix):
    plt.figure(b3 = (10, 10))
    plt.imshow(matrix, b4 = 'gray', interpolation='nearest')
    plt.title("Fibonacci Sequence in Binary Form")
    plt.xlabel("Bit Position")
    plt.ylabel("Fibonacci Index")
    plt.show()
def fonk5(matrix):
    b5 = np.sum(matrix, axis=1)
    b6 = np.arange(len(b5))
    plt.figure(b3 = (10, 6))
    plt.bar(b6, b5, b7 = 'r', label='1s', alpha=0.6)
    plt.bar(b6, matrix.shape[1] - b5, b8 = b5, b7='y', label='0s', alpha=0.6)
    plt.title("Bit Distribution in the Fibonacci Binary Matrix")
    plt.xlabel("Fibonacci Index")
    plt.ylabel("Count")
    plt.legend()
    plt.show()
if b9 = = "__main__":
    a1 = 100
    b1 = fonk1(a1)
    b10 = fonk2(b1)
    b11 = fonk3(b10)
    fonk4(b11)
    fonk5(b11)