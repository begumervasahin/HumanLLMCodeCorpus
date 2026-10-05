import matplotlib.pyplot as plt
from numpy import *
def p2d2cls(data, label, correctData, correctLabel, wrongData, wrongLabel, blk=True):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    dats = [data, correctData, wrongData]
    labs = [label, correctLabel, wrongLabel]
    clrs = ['b', 'g', 'r']
    for dat, lab, clr in zip(dats, labs, clrs):
        tInd = where(lab == 1)[0]
        fInd = where(lab == 0)[0]
        if tInd.size > 0:
            ax.scatter(dat[tInd, 0], dat[tInd, 1], marker='o', c=clr)
        if fInd.size > 0:
            ax.scatter(dat[fInd, 0], dat[fInd, 1], marker='x', c=clr)
    plt.show(block=blk)
data = array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
label = array([1, 0, 1, 0, 1])
correctData = array([[2, 3], [4, 5]])
correctLabel = array([0, 0])
wrongData = array([[1, 2], [3, 4], [5, 6]])
wrongLabel = array([1, 1, 1])
p2d2cls(data, label, correctData, correctLabel, wrongData, wrongLabel)