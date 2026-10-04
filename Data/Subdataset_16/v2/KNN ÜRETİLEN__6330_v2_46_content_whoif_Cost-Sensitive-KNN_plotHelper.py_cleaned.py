import matplotlib.pyplot as plt
import numpy as np
def fonk1(b8, b9, b10, b11, b12, b13, b1 = True):
    fig, b2 = plt.subplots()
    b3 = [(b8, b9, 'b'), (b10, b11, 'g'), (b12, b13, 'r')]
    b4 = ['o', 'x']
    for dataset, label_set, color in b3:
        for label, b6 in zip([1, 0], b4):
            b5 = np.where(label_set == label)[0]
            if b5.size > 0:
                b2.scatter(dataset[b5, 0], dataset[b5, 1], b6 = b6, c=color, label=f'{color} {"true" if label == 1 else "false"}')
    b2.legend()
    plt.show(b1 = b1)
if b7 = = "__main__":
    b8 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b9 = np.array([1, 0, 1, 0])
    b10 = np.array([[1, 2], [3, 4]])
    b11 = np.array([1, 1])
    b12 = np.array([[2, 3], [4, 5]])
    b13 = np.array([0, 0])
    fonk1(b8, b9, b10, b11, b12, b13)