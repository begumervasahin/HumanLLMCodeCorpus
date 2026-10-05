from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
def plot_confusion_matrix(cm, classes, normalize=False, title="Confusion Matrix", cmap=None, plot=True):
    '''
    Plots the given confusion matrix
    :param cm: Confusion matrix
    :param classes: List of unique classes
    :param normalize: True if elements in cm are of float type
    :param title: Title of the plot
    :param cmap:
    :param plot: True if a plot is to be generated
    :return:
    '''
    try:
        if cmap is None:
            cmap = plt.cm.Blues
        fig, ax = plt.subplots()
        im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
        ax.figure.colorbar(im, ax=ax)
        ax.set(
            xticks=np.arange(cm.shape[1]),
            yticks=np.arange(cm.shape[0]),
            xticklabels=classes,
            yticklabels=classes,
            title=title,
            ylabel='True label',
            xlabel='Predicted label'
        )
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], fmt), ha="center", va="center",
                        color="white" if cm[i, j] > thresh else "black")
        fig.tight_layout()
        if plot:
            plt.show()
    except Exception as e:
        print("Could not generate graphical plot, continuing anyway!", e)
        return None, classes, cm
    return ax, classes, cm
def confusion_matrix(actual, predicted):
    '''
    Calculates the confusion matrix from true labels and predicted labels
    :param actual: True labels
    :param predicted: Predicted labels
    :return: Confusion matrix
    '''
    actual = list(actual)
    predicted = list(predicted)
    assert len(actual) == len(predicted)
    classes = np.unique(actual).tolist()
    num_classes = len(classes)
    cm = np.zeros((num_classes, num_classes), dtype=int)
    for i in range(len(predicted)):
        x = classes.index(actual[i])
        y = classes.index(predicted[i])
        cm[x][y] += 1
    return cm, classes
if __name__ == '__main__':
    actual_labels = ['Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
                     'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica',
                     'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-virginica',
                     'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa']
    predicted_labels = ['Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
                        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica',
                        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-virginica',
                        'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa']
    cm, classes = confusion_matrix(actual_labels, predicted_labels)
    plot_confusion_matrix(cm.astype(float), classes, normalize=True)