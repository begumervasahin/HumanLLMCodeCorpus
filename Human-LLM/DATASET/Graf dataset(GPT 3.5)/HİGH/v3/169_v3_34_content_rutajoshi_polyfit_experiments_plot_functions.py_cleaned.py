import numpy as np
import matplotlib.pyplot as plt
def fonk1(b15, b16):
    b1 = list(b15)
    b2 = list(b16)
    b3 = plt.gca()
    b4 = max(b1) - min(b1)
    b5 = max(b2) - min(b2)
    b6 = 1/3
    b7 = b4 * b6
    b8 = b5 * b6
    b3.set_xlim([min(b1) - b7, max(b1) + b7])
    b3.set_ylim([min(b2) - b8, max(b2) + b8])
    plt.gca().set_autoscale_on(False)
def fonk2(b12, y_range, b9 = 'o', b10='k', label='Data Points'):
    plt.plot(b12, y_range, b9, b10 = b10, label=label)
def fonk3(b15, function, b11 = '-', b10='k', label='Function'):
    b12 = np.linspace(min(b15) - 10, max(b15) + 10, 1000)
    plt.plot(b12, function(b12), b11, b10 = b10, label=label)
def fonk4(b13 = 'lower right'):
    plt.legend(b14 = b13)
    plt.show()
b15 = np.linspace(0, 10, 100)
b16 = np.sin(b15)
fonk2(b15, b16, b9 = 'o', b10='blue', label='Data Points')
def fonk5(x):
    return x**2 - 5*x + 6
fonk3(b15, quadratic_function, b11 = '-', b10='red', label='Quadratic Function')
fonk1(b15, b16)
fonk4()