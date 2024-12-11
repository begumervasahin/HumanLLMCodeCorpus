import matplotlib.pyplot as plt
import numpy as np
def fonk1(b10, b11, b12, b13, b14, b15, b1 = True):
    b2 = plt.figure()
    b3 = b2.add_subplot(111)
    b4 = [b10, b12, b14]
    b5 = [b11, b13, b15]
    b6 = ['b', 'g', 'r']
    for data_set, lab, color in zip(b4, b5, b6):
        b7 = np.where(lab == 1)[0]
        b8 = np.where(lab == 0)[0]
        if b7.size > 0:
            b3.scatter(data_set[b7, 0], data_set[b7, 1], b9 = 'o', c=color)
        if b8.size > 0:
            b3.scatter(data_set[b8, 0], data_set[b8, 1], b9 = 'x', c=color)
    plt.show(b1 = b1)
b10 = np.random.rand(100, 2)
b11 = np.random.randint(0, 2, size=100)
b12 = b10[b11 == 1]
b13 = b11[b11 == 1]
b14 = b10[b11 == 0]
b15 = b11[b11 == 0]
fonk1(b10, b11, b12, b13, b14, b15)