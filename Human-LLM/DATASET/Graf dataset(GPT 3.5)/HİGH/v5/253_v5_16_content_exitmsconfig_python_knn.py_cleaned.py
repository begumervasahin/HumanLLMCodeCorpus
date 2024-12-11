import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import warnings
def fonk1(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))
def fonk2(data, predict, b1 = 3):
    if len(data) >= b1:
        warnings.warn("b1 is too small")
    b2 = [(group, fonk1(features, predict))
                 for group, features_list in data.items()
                 for features in features_list]
    b3 = sorted(b2, key=lambda x: x[1])
    b4 = [group for group, _ in b3[:b1]]
    b5 = Counter(b4).most_common(1)[0][0]
    b6 = Counter(b4).most_common(1)[0][1] * 1.0 / b1
    return b5, b6
if b7 = = '__main__':
    b8 = {'black': [[1, 2], [2, 3], [3, 1]], 'red': [[6, 5], [7, 7], [8, 6]]}
    b9 = [3.5, 5.2]
    for group, features_list in b8.items():
        for features in features_list:
            plt.scatter(features[0], features[1], b10 = 50, color=group)
    which_group, b6 = fonk2(b8, b9, b1=3)
    print(f"Predicted group: {which_group}, Confidence: {b6}")
    plt.scatter(b9[0], b9[1], b10 = 300, color=which_group)
    plt.show()