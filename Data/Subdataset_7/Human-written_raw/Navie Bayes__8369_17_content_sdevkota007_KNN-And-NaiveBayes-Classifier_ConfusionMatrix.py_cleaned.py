from __future__ import division
import numpy as np
try:
    import matplotlib.pyplot as plt
except Exception as e:
    print("Could Not import matplotlib")
def fonk1(b22, b20,
                        b1 = False,
                        b2 = "Confusion Matrix",
                        b3 = None,
                        b4 = True):
    '''
    plots the given confusion matrix
    :param b22: confusion matrix
    :param b20: list of unique b20
    :param b1: True if elements in b22 are of float type
    :param b2: Title of the b4
    :param b3:
    :param b4: True if a b4 is to be generated
    :return:
    '''
    try:
        if b3 is None:
            b3 = plt.b22.Blues
        fig, b5 = plt.subplots()
        b6 = b5.imshow(b22, interpolation='nearest', b3=b3)
        b5.figure.colorbar(b6, b5 = b5)
        b5.set(b7 = np.arange(b22.shape[1]),
               b8 = np.arange(b22.shape[0]),
               b9 = b20, yticklabels=b20,
               b2 = b2,
               b10 = 'True label',
               b11 = 'Predicted label')
        plt.setp(b5.get_xticklabels(), b12 = 45, b16="right",
                 b13 = "anchor")
        b14 = '.2f' if b1 else 'd'
        b15 = b22.max() / 2.
        for i in range(b22.shape[0]):
            for j in range(b22.shape[1]):
                b5.text(j, i, format(b22[i, j], b14),
                        b16 = "center", va="center",
                        b17 = "white" if b22[i, j] > b15 else "black")
        fig.tight_layout()
        if b4:
            plt.show()
    except Exception as e:
        print("Could not generate graphical b4, continuing anyway!", e)
        return None,b20, b22
    return b5,b20, b22
def fonk2(b18, b19):
    '''
    calculates the confusion matrix from true labels and b19 labels
    :param b18: true labels
    :param b19: true labels
    :return: confusion matrix
    '''
    b18 = list(b18)
    b19 = list(b19)
    assert len(b18)==len(b19)
    b20 = np.unique(b18).tolist()
    b21 = len(b20)
    b22 = np.zeros((b21,b21), dtype=int)
    for i in range(len(b19)):
        b23 = b20.index(b18[i])
        b24 = b20.index(b19[i])
        b22[b23][b24] +=1
    return b22, b20
if b25 = = '__main__':
    b26 = ['Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-virginica', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa']
    b27 = ['Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa']
    b22, b20 = fonk2(b26, b27)
    fonk1(b22.astype(float), b20, b1 = True)