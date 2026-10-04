from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
def plotConfusionMatrix(cm, classes, normalize=False, title="Confusion Matrix", cmap=None, plot=True):
    '''
    Plots the given confusion matrix
    :param cm: confusion matrix
    :param classes: list of unique classes
    :param normalize: True if elements in cm are of float type
    :param title: Title of the plot
    :param cmap: Colormap
    :param plot: True if a plot is to be generated
    :return: Axes object, classes, confusion matrix
    '''
    if cmap is None:
        cmap = plt.cm.Blues
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    if plot:
        plt.show()
    return ax, classes, cm
def confusionMatrix(actual, predicted):
    '''
    Calculates the confusion matrix from true labels and predicted labels
    :param actual: true labels
    :param predicted: predicted labels
    :return: confusion matrix and list of classes
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
    A = ['Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-virginica', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa']
    P = ['Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa']
    cm, classes = confusionMatrix(A, P)
    plotConfusionMatrix(cm.astype(float), classes, normalize=True)