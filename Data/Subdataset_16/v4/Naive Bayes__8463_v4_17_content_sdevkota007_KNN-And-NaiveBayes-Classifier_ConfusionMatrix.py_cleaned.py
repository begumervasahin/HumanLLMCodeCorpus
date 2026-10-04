from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
def fonk1(b20, b18, b1 = False, b8="Confusion Matrix", b2=None, plot=True):
    '''
    Plots the given confusion matrix.
    :param b20: Confusion matrix
    :param b18: List of unique b18
    :param b1: True if elements in b20 are of float type
    :param b8: Title of the plot
    :param b2: Colormap
    :param plot: True if a plot is to be generated
    :return: Axes object, b18, and confusion matrix
    '''
    try:
        if b2 is None:
            b2 = plt.b20.Blues
        fig, b3 = plt.subplots()
        b4 = b3.imshow(b20, interpolation='nearest', b2=b2)
        b3.figure.colorbar(b4, b3 = b3)
        b3.set(
            b5 = np.arange(b20.shape[1]),
            b6 = np.arange(b20.shape[0]),
            b7 = b18, yticklabels=b18,
            b8 = b8,
            b9 = 'True label',
            b10 = 'Predicted label'
        )
        plt.setp(b3.get_xticklabels(), b11 = 45, b14="right", rotation_mode="anchor")
        b12 = '.2f' if b1 else 'd'
        b13 = b20.max() / 2.
        for i in range(b20.shape[0]):
            for j in range(b20.shape[1]):
                b3.text(j, i, format(b20[i, j], b12),
                        b14 = "center", va="center",
                        b15 = "white" if b20[i, j] > b13 else "black")
        fig.tight_layout()
        if plot:
            plt.show()
    except Exception as e:
        print("Could not generate graphical plot, continuing anyway!", e)
        return None, b18, b20
    return b3, b18, b20
def fonk2(b16, b17):
    '''
    Calculates the confusion matrix from true labels and b17 labels.
    :param b16: True labels
    :param b17: Predicted labels
    :return: Confusion matrix and b18
    '''
    b16 = list(b16)
    b17 = list(b17)
    assert len(b16) == len(b17)
    b18 = np.unique(b16).tolist()
    b19 = len(b18)
    b20 = np.zeros((b19, b19), dtype=int)
    for i in range(len(b17)):
        b21 = b18.index(b16[i])
        b22 = b18.index(b17[i])
        b20[b21][b22] += 1
    return b20, b18
if b23 = = '__main__':
    b24 = [
        'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica',
        'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
        'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa',
        'Iris-virginica', 'Iris-virginica', 'Iris-versicolor', 'Iris-virginica',
        'Iris-versicolor', 'Iris-setosa'
    ]
    b25 = [
        'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica',
        'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
        'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa',
        'Iris-virginica', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor',
        'Iris-versicolor', 'Iris-setosa'
    ]
    b20, b18 = fonk2(b24, b25)
    fonk1(b20.astype(float), b18, b1 = True)