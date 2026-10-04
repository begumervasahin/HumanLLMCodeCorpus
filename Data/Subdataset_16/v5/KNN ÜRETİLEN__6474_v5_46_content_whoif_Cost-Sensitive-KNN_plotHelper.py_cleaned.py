import matplotlib.pyplot as plt
import numpy as np
def fonk1(data, labels, correct_data, correct_labels, wrong_data, wrong_labels, b1 = True):
    fig, b2 = plt.subplots()
    b3 = [data, correct_data, wrong_data]
    b4 = [labels, correct_labels, wrong_labels]
    b5 = ['b', 'g', 'r']
    b6 = ['o', 'o', 'x']
    b7 = ['Data', 'Correct', 'Wrong']
    for dat, lab, clr, mkr, desc in zip(b3, b4, b5, b6, b7):
        b8 = np.where(lab == 1)[0]
        b9 = np.where(lab == 0)[0]
        if b8.size > 0:
            b2.scatter(dat[b8, 0], dat[b8, 1], b10 = mkr, c=clr, label=f'{desc} True ({clr})')
        if b9.size > 0:
            b2.scatter(dat[b9, 0], dat[b9, 1], b10 = mkr, c=clr, label=f'{desc} False ({clr})')
    b2.legend()
    plt.show(b1 = b1)
