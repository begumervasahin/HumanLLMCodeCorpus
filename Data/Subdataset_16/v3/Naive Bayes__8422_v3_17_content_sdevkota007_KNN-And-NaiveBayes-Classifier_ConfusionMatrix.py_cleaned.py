import numpy as np
import matplotlib.pyplot as plt
def fonk1(b20, b18, b1 = False, b8="Confusion Matrix", cmap=plt.b20.Blues, plot=True):
    fig, b2 = plt.subplots()
    b3 = b2.imshow(b20, interpolation='nearest', cmap=cmap)
    b2.figure.colorbar(b3, b2 = b2)
    b2.set(
        b4 = np.arange(b20.shape[1]),
        b5 = np.arange(b20.shape[0]),
        b6 = b18,
        b7 = b18,
        b8 = b8,
        b9 = 'True Label',
        b10 = 'Predicted Label'
    )
    plt.setp(b2.get_xticklabels(), b11 = 45, b14="right", rotation_mode="anchor")
    b12 = '.2f' if b1 else 'd'
    b13 = b20.max() / 2.0
    for i in range(b20.shape[0]):
        for j in range(b20.shape[1]):
            b2.text(
                j, i, format(b20[i, j], b12),
                b14 = "center", va="center",
                b15 = "white" if b20[i, j] > b13 else "black"
            )
    fig.tight_layout()
    if plot:
        plt.show()
    return b2, b18, b20
def fonk2(b16, b17):
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
        'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor',
        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-setosa',
        'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa',
        'Iris-setosa', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica',
        'Iris-virginica', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa'
    ]
    b25 = [
        'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-versicolor',
        'Iris-versicolor', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-setosa',
        'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-setosa',
        'Iris-setosa', 'Iris-virginica', 'Iris-versicolor', 'Iris-setosa', 'Iris-setosa',
        'Iris-virginica', 'Iris-setosa', 'Iris-virginica', 'Iris-setosa', 'Iris-virginica',
        'Iris-virginica', 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa'
    ]
    b20, b18 = fonk2(b24, b25)
    fonk1(b20.astype(float), b18, b1 = True)