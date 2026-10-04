import matplotlib.pyplot as plt
import numpy as np
def p2d2cls(data, label, correctData, correctLabel, wrongData, wrongLabel, blk=True):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    dats = [data, correctData, wrongData]
    labs = [label, correctLabel, wrongLabel]
    clrs = ['b', 'g', 'r']
    for dat, lab, clr in zip(dats, labs, clrs):
        tInd = np.where(lab == 1)[0]
        fInd = np.where(lab == 0)[0]
        if tInd.size > 0:
            ax.scatter(dat[tInd, 0], dat[tInd, 1], marker='o', c=clr, label=f'{clr} true')
        if fInd.size > 0:
            ax.scatter(dat[fInd, 0], dat[fInd, 1], marker='x', c=clr, label=f'{clr} false')
    ax.legend()
    plt.show(block=blk)
if __name__ == "__main__":
    data = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    label = np.array([1, 0, 1, 0])
    correctData = np.array([[1, 2], [3, 4]])
    correctLabel = np.array([1, 1])
    wrongData = np.array([[2, 3], [4, 5]])
    wrongLabel = np.array([0, 0])
    p2d2cls(data, label, correctData, correctLabel, wrongData, wrongLabel)