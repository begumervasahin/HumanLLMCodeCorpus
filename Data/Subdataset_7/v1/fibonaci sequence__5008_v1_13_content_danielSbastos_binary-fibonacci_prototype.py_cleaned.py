import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1):
    a, b1 = 0, 1
    for _ in range(a1):
        a, b1 = b1, a + b1
    return a
def fonk2(number, b2 = 80):
    return format(number, f'0{b2}b1')
def fonk3(a1):
    return [fonk1(i) for i in range(a1 + 1)]
def fonk4(b11):
    return [fonk2(num) for num in b11]
def fonk5(b12):
    return [[int(bit) for bit in num] for num in b12]
def fonk6(binary_matrix):
    plt.figure(b3 = (10, 10))
    plt.imshow(binary_matrix, b4 = 'nearest', cmap='gray')
    plt.title("Binary Representation of Fibonacci Sequence")
    plt.xlabel("Bit Position")
    plt.ylabel("Fibonacci Index")
    plt.show()
def fonk7(binary_matrix):
    b5 = [sum(row) for row in binary_matrix]
    b6 = [len(binary_matrix[0]) - sum(row) for row in binary_matrix]
    b7 = list(range(len(b5)))
    plt.bar(b7, b5, 0.6, b8 = 'Ones', color='r')
    plt.bar(b7, b6, 0.6, b8 = 'Zeros', color='y', bottom=b5)
    plt.title("Bit Distribution in Fibonacci Binary Representation")
    plt.xlabel("Fibonacci Index")
    plt.ylabel("Count")
    plt.legend(b9 = "upper left")
    plt.show()
if b10 = = "__main__":
    a1 = 100
    b11 = fonk3(a1)
    b12 = fonk4(b11)
    b13 = fonk5(b12)
    b14 = np.array(b13)
    fonk6(b14)
    fonk7(b14)