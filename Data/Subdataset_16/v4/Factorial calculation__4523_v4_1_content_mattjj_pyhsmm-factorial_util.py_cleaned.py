from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cbook
def fonk1(b11):
    b1 = sorted(set(cbook.flatten(b11)))
    return [(startpoint, nextstartpoint) for startpoint, nextstartpoint in zip(b1[:-1], b1[1:])]
def fonk2(b7, b9):
    plt.figure()
    plt.plot(b7)
    b2 = plt.axis()
    b3 = [c[1] for c in b9[:-1]]
    plt.vlines(b3, b2[2], b2[3], b4 = 'r', linestyles='dashed')
    plt.axis(b2)
    plt.show()
def fonk3(b8):
    b5 = np.where(np.diff(np.array(b8, dtype=int)) == 1)[0]
    b5 = np.concatenate(([0], b5 + 1, [len(b8)]))
    return [(a, b) for a, b in zip(b5[:-1], b5[1:])]
if b6 = = "__main__":
    b7 = np.random.rand(100)
    b8 = [False, False, True, False, False, False, False, True, False, False, True, False, False, False, True]
    b9 = fonk3(b8)
    fonk2(b7, b9)
    b10 = [(0, 5), (5, 10), (10, 15)]
    b11 = [b9, b10]
    b12 = fonk1(b11)
    print("Unified Changepoints:", b12)