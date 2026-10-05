import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import warnings
def fonk1(data, predict, b1 = 3):
    if len(data) < b1:
        warnings.warn("The b9 size is smaller than the specified b1 value.")
    b2 = []
    for group, features_list in data.items():
        for features in features_list:
            b3 = np.linalg.norm(np.array(features) - np.array(predict))
            b2.append([b3, group])
    b4 = [i[1] for i in sorted(b2)]
    b5 = b4[:b1]
    b6 = Counter(b5).most_common(1)[0][0]
    b7 = Counter(b5).most_common(1)[0][1] / b1
    return b6, b7
if b8 = = '__main__':
    b9 = {
        'black': [[1, 2], [2, 3], [3, 1]],
        'red': [[6, 5], [7, 7], [8, 6]]
    }
    b10 = [3.5, 5.2]
    for group, points in b9.items():
        for point in points:
            plt.scatter(point[0], point[1], b11 = 50, color=group)
    which_group, b7 = fonk1(b9, b10, b1=3)
    print("Predicted Group:", which_group)
    print("Confidence:", b7)
    plt.scatter(b10[0], b10[1], b11 = 300, color=which_group)
    plt.show()