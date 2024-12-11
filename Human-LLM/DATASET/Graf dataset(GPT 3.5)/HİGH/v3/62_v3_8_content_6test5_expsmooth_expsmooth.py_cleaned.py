import numpy as np
def fonk1(b10):
    b1 = fonk2(b10)
    b2 = fonk5(b10, b1)
    return b2
def fonk2(b10):
    b3 = np.arange(0.1, 2, 0.1)
    b4 = []
    for alpha in b3:
        b5 = fonk3(b10, alpha)
        b4.append(b5)
    b1 = b3[np.argmin(b4)]
    print("Optimal Alpha:", b1)
    return b1
def fonk3(b10, alpha):
    b6 = []
    for i in range(len(b10)):
        b7 = fonk4(b10, alpha, i)
        a1 = 0
        for j in range(i, len(b10)):
            a1 += (b7 - b10[j]) ** 2
            b7 = alpha * b10[j] + (1 - alpha) * b7
        b6.append(a1)
    return np.mean(b6)
def fonk4(b10, alpha, index):
    return alpha * b10[index] + (1 - alpha) * b10[index]
def fonk5(b10, alpha):
    b2 = [b10[0]]
    for i in range(1, len(b10)):
        b8 = alpha * b10[i] + (1 - alpha) * b2[-1]
        b2.append(b8)
    return b2[-1]
if b9 = = '__main__':
    b10 = np.array([1, 2, 3, 4, 5])
    b11 = fonk1(b10)
    print("Result:", b11)