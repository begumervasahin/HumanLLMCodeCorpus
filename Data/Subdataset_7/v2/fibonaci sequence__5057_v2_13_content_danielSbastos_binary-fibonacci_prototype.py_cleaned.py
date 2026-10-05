import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1):
    a, b1 = 0, 1
    for _ in range(a1):
        a, b1 = b1, a + b1
    return a
def fonk2(number, b2 = 80):
    return format(number, f'0{b2}b1')
def fonk3(up_to_n):
    return [fonk1(i) for i in range(up_to_n + 1)]
def fonk4(sequence):
    return [fonk2(number) for number in sequence]
def fonk5(b11):
    return [[int(bit) for bit in binary_string] for binary_string in b11]
def fonk6(matrix):
    plt.figure(b3 = (10, 10))
    plt.imshow(matrix, b4 = 'nearest', cmap='gray')
    plt.title("Binary Matrix of Fibonacci Sequence")
    plt.xlabel("Bit Index")
    plt.ylabel("Sequence Index")
    plt.show()
def fonk7(matrix):
    b5 = [sum(row) for row in matrix]
    b6 = [len(matrix[0]) - sum(row) for row in matrix]
    b7 = range(len(b5))
    plt.bar(b7, b5, 0.6, b8 = '1s', color='r')
    plt.bar(b7, b6, 0.6, b8 = '0s', color='y', bottom=b5)
    plt.title("Distribution of 1s and 0s in Fibonacci Binary Matrix")
    plt.xlabel("Sequence Index")
    plt.ylabel("Bit Count")
    plt.legend()
    plt.show()
if b9 = = "__main__":
    a1 = 100
    b10 = fonk3(a1)
    b11 = fonk4(b10)
    b12 = fonk5(b11)
    b13 = np.array(b12)
    fonk6(b13)
    fonk7(b13)