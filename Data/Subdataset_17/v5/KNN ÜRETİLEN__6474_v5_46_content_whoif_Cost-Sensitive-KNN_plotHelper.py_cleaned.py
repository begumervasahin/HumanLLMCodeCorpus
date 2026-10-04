import matplotlib.pyplot as plt
import numpy as np
def plot_2d_classification(data, labels, correct_data, correct_labels, wrong_data, wrong_labels, block=True):
    fig, ax = plt.subplots()
    datasets = [data, correct_data, wrong_data]
    labels_list = [labels, correct_labels, wrong_labels]
    colors = ['b', 'g', 'r']
    markers = ['o', 'o', 'x']
    descriptions = ['Data', 'Correct', 'Wrong']
    for dat, lab, clr, mkr, desc in zip(datasets, labels_list, colors, markers, descriptions):
        true_indices = np.where(lab == 1)[0]
        false_indices = np.where(lab == 0)[0]
        if true_indices.size > 0:
            ax.scatter(dat[true_indices, 0], dat[true_indices, 1], marker=mkr, c=clr, label=f'{desc} True ({clr})')
        if false_indices.size > 0:
            ax.scatter(dat[false_indices, 0], dat[false_indices, 1], marker=mkr, c=clr, label=f'{desc} False ({clr})')
    ax.legend()
    plt.show(block=block)
