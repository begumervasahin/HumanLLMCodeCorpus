import matplotlib.pyplot as plt
import numpy as np
def p2d2cls(data, label, correctData, correctLabel, wrongData, wrongLabel, blk=True):
    fig, ax = plt.subplots()
    datasets = [data, correctData, wrongData]
    labels = [label, correctLabel, wrongLabel]
    colors = ['b', 'g', 'r']
    for dat, lab, clr in zip(datasets, labels, colors):
        true_indices = np.where(lab == 1)[0]
        false_indices = np.where(lab == 0)[0]
        if true_indices.size > 0:
            ax.scatter(dat[true_indices, 0], dat[true_indices, 1], marker='o', c=clr, label=f'True ({clr})')
        if false_indices.size > 0:
            ax.scatter(dat[false_indices, 0], dat[false_indices, 1], marker='x', c=clr, label=f'False ({clr})')
    ax.legend()
    plt.show(block=blk)
