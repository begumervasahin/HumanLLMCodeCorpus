import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import copy
import glob
import sys
import numpy.linalg as LA
import IPython
def fonk1(b11, b12):
    b1 = list(b11)
    b2 = list(b12)
    b3 = plt.gca()
    b4 = max(b1) - min(b1)
    b5 = max(b2) - min(b2)
    b3.set_xlim([min(b1) - (b4
    b3.set_ylim([min(b2) - (b5
    plt.gca().set_autoscale_on(False)
def fonk2(b7, b8, pencil, b6 = 'k', b13='f1'):
    b7 = np.array(list(b7))
    b8 = np.array(list(b8))
    if b13 is None:
        plt.plot(b7, b8, pencil, b6 = b6)
    else:
        plt.plot(b7, b8, pencil, b6 = b6, b13=b13)
def fonk3(b11, function, pencil, b6 = 'k', b13='f1'):
    b7 = np.linspace(min(b11) - 10, max(b11) + 10, 1000)
    if b13 is None:
        plt.plot(b7, function(b7), pencil, b6 = b6)
    else:
        plt.plot(b7, function(b7), pencil, b6 = b6, b13=b13)
def fonk4(b9 = 'lower right'):
    plt.legend(b10 = b9)
    plt.show()
b11 = np.linspace(0, 10, 100)
b12 = np.sin(b11)
fonk2(b11, b12, 'o', b13 = 'Data Points')
def fonk5(x):
    return x**2 - 5*x + 6
fonk3(b11, quadratic_function, '-', b13 = 'Quadratic Function')
fonk1(b11, b12)
fonk4()