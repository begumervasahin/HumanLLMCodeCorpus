import math
import numpy as np
from matplotlib import pyplot
from collections import Counter
import warnings
def fonk1(data, predict, b1 = 3):
    if len(data) >= b1:
        warnings.warn("b1 is too small")
    b2 = []
    for group in data:
        for features in data[group]:
            b3 = np.linalg.norm(np.array(features) - np.array(predict))
            b2.append([b3, group])
    b4 = [i[1] for i in sorted(b2)]
    b5 = b4[:b1]
    b6 = Counter(b5).most_common(1)[0][0]
    b7 = Counter(b5).most_common(1)[0][1] * 1.0 / b1
    return b6, b7
if b8 = = '__main__':
    b9 = {'black': [[1, 2], [2, 3], [3, 1]], 'red': [[6, 5], [7, 7], [8, 6]]}
    b10 = [3.5, 5.2]
    for i in b9:
        for ii in b9[i]:
            pyplot.scatter(ii[0], ii[1], b11 = 50, color=i)
    which_group, b7 = fonk1(b9, b10, b1=3)
    print(which_group, b7)
    pyplot.scatter(b10[0], b10[1], b11 = 300, color=which_group)
    pyplot.show()