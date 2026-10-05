import matplotlib.pyplot as plt
import numpy as np
def plot_2d_classification(data, label, correct_data, correct_label, wrong_data, wrong_label, block=True):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    datasets = [data, correct_data, wrong_data]
    labels = [label, correct_label, wrong_label]
    colors = ['b', 'g', 'r']
    for dataset, labels, color in zip(datasets, labels, colors):
        true_indices = np.where(labels == 1)[0]
        false_indices = np.where(labels == 0)[0]
        if true_indices.size > 0:
            ax.scatter(dataset[true_indices, 0], dataset[true_indices, 1], marker='o', c=color)
        if false_indices.size > 0:
            ax.scatter(dataset[false_indices, 0], dataset[false_indices, 1], marker='x', c=color)
    plt.show(block=block)
data = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
label = np.array([1, 0, 1, 0, 1])
correct_data = np.array([[2, 3], [4, 5]])
correct_label = np.array([0, 0])
wrong_data = np.array([[1, 2], [3, 4], [5, 6]])
wrong_label = np.array([1, 1, 1])
plot_2d_classification(data, label, correct_data, correct_label, wrong_data, wrong_label)