import os
import numpy as np
import matplotlib.pyplot as plt
def fonk1(x_data, y_data):
    b1 = list(x_data)
    b2 = list(y_data)
    b3 = plt.gca()
    b4 = max(b1) - min(b1)
    b5 = max(b2) - min(b2)
    b3.set_xlim([min(b1) - (b4
    b3.set_ylim([min(b2) - (b5
    plt.gca().set_autoscale_on(False)
def fonk2(b7, b8, pencil, b6 = 'k', label='f1'):
    b7 = np.array(list(b7))
    b8 = np.array(list(b8))
    if label is None:
        plt.plot(b7, b8, pencil, b6 = b6)
    else:
        plt.plot(b7, b8, pencil, b6 = b6, label=label)
def fonk3(x_data, function, pencil, b6 = 'k', label='f1'):
    b7 = np.linspace(min(x_data) - 10, max(x_data) + 10, 1000)
    if label is None:
        plt.plot(b7, function(b7), pencil, b6 = b6)
    else:
        plt.plot(b7, function(b7), pencil, b6 = b6, label=label)
def fonk4(b9 = 'lower right'):
    plt.legend(b10 = b9)
    plt.show()