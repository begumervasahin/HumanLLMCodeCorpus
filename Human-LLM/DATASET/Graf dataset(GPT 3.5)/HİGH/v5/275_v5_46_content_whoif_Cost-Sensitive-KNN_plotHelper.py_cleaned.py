import matplotlib.pyplot as plt
import numpy as np
def fonk1(b7, b8, b9, b10, b11, b12, b1 = True):
    fig, b2 = plt.subplots()
    b3 = ['b', 'g', 'r']
    for data_set, lab, color in zip([b7, b9, b11], [b8, b10, b12], b3):
        b4 = np.where(lab == 1)[0]
        b5 = np.where(lab == 0)[0]
        b2.scatter(data_set[b4, 0], data_set[b4, 1], b6 = 'o', c=color, b8='Correct' if color == 'g' else '')
        b2.scatter(data_set[b5, 0], data_set[b5, 1], b6 = 'x', c=color, b8='Wrong' if color == 'r' else '')
    b2.legend()
    plt.show(b1 = b1)
b7 = np.random.rand(100, 2)
b8 = np.random.randint(0, 2, size=100)
b9 = b7[b8 == 1]
b10 = b8[b8 == 1]
b11 = b7[b8 == 0]
b12 = b8[b8 == 0]
fonk1(b7, b8, b9, b10, b11, b12)