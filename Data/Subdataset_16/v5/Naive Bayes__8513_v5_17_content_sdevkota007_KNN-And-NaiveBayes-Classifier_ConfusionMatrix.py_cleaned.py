from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
def fonk1(b21, b19, b1 = False, b9="Confusion Matrix", b2=None, plot=True):
    if b2 is None:
        b2 = plt.b21.Blues
    fig, b3 = plt.subplots()
    b4 = b3.imshow(b21, interpolation='nearest', b2=b2)
    b3.figure.colorbar(b4, b3 = b3)
    b3.set(
        b5 = np.arange(b21.shape[1]),
        b6 = np.arange(b21.shape[0]),
        b7 = b19,
        b8 = b19,
        b9 = b9,
        b10 = 'True label',
        b11 = 'Predicted label'
    )
    plt.setp(b3.get_xticklabels(), b12 = 45, b15="right", rotation_mode="anchor")
    b13 = '.2f' if b1 else 'd'
    b14 = b21.max() / 2.
    for i in range(b21.shape[0]):
        for j in range(b21.shape[1]):
            b3.text(j, i, format(b21[i, j], b13),
                    b15 = "center", va="center",
                    b16 = "white" if b21[i, j] > b14 else "black")
    fig.tight_layout()
    if plot:
        plt.show()
    return b3, b19, b21
def fonk2(b17, b18):
    b17 = list(b17)
    b18 = list(b18)
    assert len(b17) == len(b18)
    b19 = np.unique(b17).tolist()
    b20 = len(b19)
    b21 = np.zeros((b20, b20), dtype=int)
    for true_label, predicted_label in zip(b17, b18):
        b22 = b19.index(true_label)
        b23 = b19.index(predicted_label)
        b21[b22, b23] += 1
    return b21, b19
if b24 = = '__main__':
    b25 = [
        'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica',
        'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
        'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa',
        'Iris-virginica', 'Iris-virginica', 'Iris-versicolor', 'Iris-virginica',
        'Iris-versicolor', 'Iris-setosa'
    ]
    b26 = [
        'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica',
        'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
        'Iris-versicolor', 'Iris-virginica', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa',
        'Iris-virginica', 'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor',
        'Iris-versicolor', 'Iris-setosa'
    ]
    b21, b19 = fonk2(b25, b26)
    fonk1(b21.astype(float), b19, b1 = True)