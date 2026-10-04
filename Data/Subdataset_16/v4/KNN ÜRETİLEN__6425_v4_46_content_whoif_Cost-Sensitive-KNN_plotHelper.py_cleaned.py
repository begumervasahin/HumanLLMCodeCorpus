import matplotlib.pyplot as plt
import numpy as np
def fonk1(data, label, correctData, correctLabel, wrongData, wrongLabel, b1 = True):
    fig, b2 = plt.subplots()
    b3 = [data, correctData, wrongData]
    b4 = [label, correctLabel, wrongLabel]
    b5 = ['b', 'g', 'r']
    for dat, lab, clr in zip(b3, b4, b5):
        b6 = np.where(lab == 1)[0]
        b7 = np.where(lab == 0)[0]
        if b6.size > 0:
            b2.scatter(dat[b6, 0], dat[b6, 1], b8 = 'o', c=clr, label=f'True ({clr})')
        if b7.size > 0:
            b2.scatter(dat[b7, 0], dat[b7, 1], b8 = 'x', c=clr, label=f'False ({clr})')
    b2.legend()
    plt.show(b9 = b1)
