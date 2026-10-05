import matplotlib.pyplot as plt
import numpy as np
def plot_2d_data_classification(data, label, correct_data, correct_label, wrong_data, wrong_label, block=True):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    data_sets = [data, correct_data, wrong_data]
    labels = [label, correct_label, wrong_label]
    colors = ['b', 'g', 'r']
    for data_set, lab, color in zip(data_sets, labels, colors):
        true_indices = np.where(lab == 1)[0]
        false_indices = np.where(lab == 0)[0]
        if true_indices.size > 0:
            ax.scatter(data_set[true_indices, 0], data_set[true_indices, 1], marker='o', c=color)
        if false_indices.size > 0:
            ax.scatter(data_set[false_indices, 0], data_set[false_indices, 1], marker='x', c=color)
    plt.show(block=block)
data = np.random.rand(100, 2)
label = np.random.randint(0, 2, size=100)
correct_data = data[label == 1]
correct_label = label[label == 1]
wrong_data = data[label == 0]
wrong_label = label[label == 0]
plot_2d_data_classification(data, label, correct_data, correct_label, wrong_data, wrong_label)