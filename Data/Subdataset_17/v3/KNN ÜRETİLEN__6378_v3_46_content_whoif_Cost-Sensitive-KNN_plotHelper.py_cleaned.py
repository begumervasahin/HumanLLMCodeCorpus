import matplotlib.pyplot as plt
import numpy as np
def plot_2d_classification(data, labels, correct_data, correct_labels, wrong_data, wrong_labels, block=True):
    fig, ax = plt.subplots()
    datasets = [
        (data, labels, 'b', 'Main'),
        (correct_data, correct_labels, 'g', 'Correct'),
        (wrong_data, wrong_labels, 'r', 'Wrong')
    ]
    markers = ['o', 'x']
    for dataset, label_set, color, label_prefix in datasets:
        for label, marker in zip([1, 0], markers):
            indices = np.where(label_set == label)[0]
            if indices.size > 0:
                ax.scatter(
                    dataset[indices, 0], dataset[indices, 1],
                    marker=marker, c=color,
                    label=f'{label_prefix} {"Positive" if label == 1 else "Negative"}'
                )
    ax.legend()
    plt.show(block=block)
if __name__ == "__main__":
    data = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    labels = np.array([1, 0, 1, 0])
    correct_data = np.array([[1, 2], [3, 4]])
    correct_labels = np.array([1, 1])
    wrong_data = np.array([[2, 3], [4, 5]])
    wrong_labels = np.array([0, 0])
    plot_2d_classification(data, labels, correct_data, correct_labels, wrong_data, wrong_labels)