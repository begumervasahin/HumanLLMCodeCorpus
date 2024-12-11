import matplotlib.pyplot as plt
from numpy import *
def fonk1(data, label, correctData, correctLabel, wrongData, wrongLabel, b1 = True):
    b2 = plt.figure()
    b3 = b2.add_subplot(111)
    b4 = [data, correctData, wrongData]
    b5 = [label, correctLabel, wrongLabel]
    b6 = ['b', 'g', 'r']
    for dat, lab, clr in zip(b4, b5, b6):
        b7 = where(lab == 1)[0]
        b8 = where(lab == 0)[0]
        if b7.size > 0:
            b3.scatter(dat[b7, 0], dat[b7, 1], b9 = 'o', c=clr)
        if b8.size > 0:
            b3.scatter(dat[b8, 0], dat[b8, 1], b9 = 'x', c=clr)
    plt.show(b10 = b1)