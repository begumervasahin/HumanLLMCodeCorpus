import matplotlib.pyplot as plt
from numpy import *
def fonk1(b11, b12, b13, b14, b15, b16, b1 = True):
    b2 = plt.figure()
    b3 = b2.add_subplot(111)
    b4 = [b11, b13, b15]
    b5 = [b12, b14, b16]
    b6 = ['b', 'g', 'r']
    for dat, lab, clr in zip(b4, b5, b6):
        b7 = where(lab == 1)[0]
        b8 = where(lab == 0)[0]
        if b7.size > 0:
            b3.scatter(dat[b7, 0], dat[b7, 1], b9 = 'o', c=clr)
        if b8.size > 0:
            b3.scatter(dat[b8, 0], dat[b8, 1], b9 = 'x', c=clr)
    plt.show(b10 = b1)
b11 = array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
b12 = array([1, 0, 1, 0, 1])
b13 = array([[2, 3], [4, 5]])
b14 = array([0, 0])
b15 = array([[1, 2], [3, 4], [5, 6]])
b16 = array([1, 1, 1])
fonk1(b11, b12, b13, b14, b15, b16)