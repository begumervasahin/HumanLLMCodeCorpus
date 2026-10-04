
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
def fonk1(start, stop, num_points, coeff, b1 = 1, b5 = 1):
    b2 = np.arange(start, stop, (stop - start)/num_points)
    b3 = coeff[0]
    for i in np.arange(1, len(coeff)):
        b3 += coeff[i] * b2 ** i
    if b1 > 0:
        b4 = np.random.normal(-(10 ** b1), 10 ** b1, len(b2)) + b3
    else:
        b4 = b3
    if b5 = = 1:
        plt.figure()
        plt.scatter(b2, b4)
        plt.xlabel('x')
        plt.ylabel('y')
    return b2, b4