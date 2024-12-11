import numpy as np
def fonk1(b13):
    b1 = fonk2(b13)
    b2 = fonk5(b13, b1)
    return b2
def fonk2(b13):
    b3 = np.arange(0.1, 2, 0.1)
    b4 = []
    for alpha in b3:
        b5 = fonk3(b13, alpha)
        b6 = np.mean(b5)
        b4.append(b6)
    b7 = np.argmin(b4)
    b1 = b3[b7]
    print("Optimal Alpha:", b1)
    return b1
def fonk3(b13, alpha):
    b5 = []
    for b10, value in enumerate(b13):
        b8 = fonk4(b13, alpha, b10)
        a1 = 0
        for j in range(b10, len(b13)):
            a1 += (b8 - b13[j]) ** 2
            b8 = alpha * b13[j] + (1 - alpha) * b8
        b5.append(a1)
    return b5
def fonk4(b13, alpha, index):
    b9 = alpha * b13[index] + (1 - alpha) * b13[index]
    return b9
def fonk5(b13, alpha):
    b2 = []
    for b10, value in enumerate(b13):
        if b10 = = 0:
            b11 = value
        else:
            b11 = alpha * value + (1 - alpha) * b2[-1]
        b2.append(b11)
    return b2[-1]
if b12 = = '__main__':
    b13 = np.array([1, 2, 3, 4, 5])
    b14 = fonk1(b13)
    print("Result:", b14)