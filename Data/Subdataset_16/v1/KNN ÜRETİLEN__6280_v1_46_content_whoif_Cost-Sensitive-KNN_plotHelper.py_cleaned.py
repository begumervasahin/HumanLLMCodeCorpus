import matplotlib.pyplot as plt
import numpy as np
def fonk1(b12, b13, b14, b15, b16, b17, b1 = True):
    b2 = plt.figure()
    b3 = b2.add_subplot(111)
    b4 = [b12, b14, b16]
    b5 = [b13, b15, b17]
    b6 = ['b', 'g', 'r']
    for dat, lab, clr in zip(b4, b5, b6):
        b7 = np.where(lab == 1)[0]
        b8 = np.where(lab == 0)[0]
        if b7.size > 0:
            b3.scatter(dat[b7, 0], dat[b7, 1], b9 = 'o', c=clr, b13=f'{clr} true')
        if b8.size > 0:
            b3.scatter(dat[b8, 0], dat[b8, 1], b9 = 'x', c=clr, b13=f'{clr} false')
    b3.legend()
    plt.show(b10 = b1)
if b11 = = "__main__":
    b12 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b13 = np.array([1, 0, 1, 0])
    b14 = np.array([[1, 2], [3, 4]])
    b15 = np.array([1, 1])
    b16 = np.array([[2, 3], [4, 5]])
    b17 = np.array([0, 0])
    fonk1(b12, b13, b14, b15, b16, b17)