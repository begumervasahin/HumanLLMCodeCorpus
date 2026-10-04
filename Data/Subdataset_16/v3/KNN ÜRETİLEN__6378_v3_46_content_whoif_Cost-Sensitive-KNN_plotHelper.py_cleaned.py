import matplotlib.pyplot as plt
import numpy as np
def fonk1(b9, b10, b11, b12, b13, b14, b1 = True):
    fig, b2 = plt.subplots()
    b3 = [
        (b9, b10, 'b', 'Main'),
        (b11, b12, 'g', 'Correct'),
        (b13, b14, 'r', 'Wrong')
    ]
    b4 = ['o', 'x']
    for dataset, label_set, color, label_prefix in b3:
        for b7, b6 in zip([1, 0], b4):
            b5 = np.where(label_set == b7)[0]
            if b5.size > 0:
                b2.scatter(
                    dataset[b5, 0], dataset[b5, 1],
                    b6 = b6, c=color,
                    b7 = f'{label_prefix} {"Positive" if b7 == 1 else "Negative"}'
                )
    b2.legend()
    plt.show(b1 = b1)
if b8 = = "__main__":
    b9 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b10 = np.array([1, 0, 1, 0])
    b11 = np.array([[1, 2], [3, 4]])
    b12 = np.array([1, 1])
    b13 = np.array([[2, 3], [4, 5]])
    b14 = np.array([0, 0])
    fonk1(b9, b10, b11, b12, b13, b14)