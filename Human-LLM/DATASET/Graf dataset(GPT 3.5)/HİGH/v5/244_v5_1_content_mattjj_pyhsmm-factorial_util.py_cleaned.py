from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
def fonk1(all_changepoints):
    b1 = sorted(set(cbook.flatten(all_changepoints)))
    return [(start, next_start) for start, next_start in zip(b1[:-1], b1[1:])]
def fonk2(b7, b9):
    plt.figure()
    plt.plot(b7)
    b2 = plt.axis()
    plt.vlines([c[1] for c in b9[:-1]], b2[2], b2[3], b3 = 'r', linestyles='dashed')
    plt.axis(b2)
    plt.show()
def fonk3(b8):
    b5, = np.where(np.diff(np.array(b8, b4 = int)) == 1)
    b5 = np.concatenate(([0], b5 + 1, [len(b8)]))
    return [(a, b) for a, b in zip(b5[:-1], b5[1:])]
if b6 = = "__main__":
    b7 = np.random.rand(100)
    b8 = np.random.choice([False, True], size=100)
    b9 = fonk3(b8)
    fonk2(b7, b9)