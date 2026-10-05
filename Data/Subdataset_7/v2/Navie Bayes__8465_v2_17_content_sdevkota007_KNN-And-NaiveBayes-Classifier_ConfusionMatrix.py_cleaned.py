from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
def fonk1(confusion_matrix, b19, b1 = False, b9="Confusion Matrix", b2=None, plot=True):
    '''
    Plots the given confusion matrix.
    :param confusion_matrix: Confusion matrix
    :param b19: List of unique b19
    :param b1: True if elements in confusion_matrix are of float type
    :param b9: Title of the plot
    :param b2: Color map
    :param plot: True if a plot is to be generated
    :return: Axis, b19, confusion_matrix
    '''
    try:
        if b2 is None:
            b2 = plt.b21.Blues
        fig, b3 = plt.subplots()
        b4 = b3.imshow(confusion_matrix, interpolation='nearest', b2=b2)
        b3.figure.colorbar(b4, b3 = b3)
        b3.set(
            b5 = np.arange(confusion_matrix.shape[1]),
            b6 = np.arange(confusion_matrix.shape[0]),
            b7 = b19,
            b8 = b19,
            b9 = b9,
            b10 = 'True label',
            b11 = 'Predicted label'
        )
        plt.setp(b3.get_xticklabels(), b12 = 45, b15="right", rotation_mode="anchor")
        b13 = '.2f' if b1 else 'd'
        b14 = confusion_matrix.max() / 2.
        for i in range(confusion_matrix.shape[0]):
            for j in range(confusion_matrix.shape[1]):
                b3.text(j, i, format(confusion_matrix[i, j], b13), b15 = "center", va="center",
                        b16 = "white" if confusion_matrix[i, j] > b14 else "black")
        fig.tight_layout()
        if plot:
            plt.show()
    except Exception as e:
        print("Could not generate graphical plot, continuing anyway!", e)
        return None, b19, confusion_matrix
    return b3, b19, confusion_matrix
def fonk2(b17, b18):
    '''
    Calculates the confusion matrix from true labels and b18 labels.
    :param b17: True labels
    :param b18: Predicted labels
    :return: Confusion matrix, b19
    '''
    b17 = list(b17)
    b18 = list(b18)
    assert len(b17) == len(b18)
    b19 = np.unique(b17).tolist()
    b20 = len(b19)
    b21 = np.zeros((b20, b20), dtype=int)
    for i in range(len(b18)):
        b22 = b19.index(b17[i])
        b23 = b19.index(b18[i])
        b21[b22][b23] += 1
    return b21, b19
if b24 = = '__main__':
    b25 = ['Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
                     'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica',
                     'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-virginica',
                     'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa']
    b26 = ['Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
                        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica',
                        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-virginica',
                        'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa']
    b21, b19 = fonk2(b25, b26)
    fonk1(b21.astype(float), b19, b1 = True)