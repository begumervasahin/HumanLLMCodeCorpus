from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cbook
def fonk1(b10):
    b1 = sorted(set(cbook.flatten(b10)))
    return [(startpoint, nextstartpoint) for startpoint, nextstartpoint in zip(b1[:-1], b1[1:])]
def fonk2(b6, b8):
    plt.figure()
    plt.plot(b6)
    b2 = plt.axis()
    b3 = [c[1] for c in b8[:-1]]
    plt.vlines(b3, b2[2], b2[3], b4 = 'r', linestyles='dashed')
    plt.axis(b2)
    plt.show()
def fonk3(b7):
    b5 = np.where(np.diff(np.array(b7, dtype=int)) == 1)[0]
    b5 = np.concatenate(([0], b5 + 1, [len(b7)]))
    return [(a, b) for a, b in zip(b5[:-1], b5[1:])]
def fonk4():
    b6 = np.random.rand(100)
    b7 = [False, False, True, False, False, False, False, True, False, False, True, False, False, False, True]
    b8 = fonk3(b7)
    fonk2(b6, b8)
    b9 = [(0, 5), (5, 10), (10, 15)]
    b10 = [b8, b9]
    b11 = fonk1(b10)
    print("Unified Changepoints:", b11)
if b12 = = "__main__":
    fonk4()