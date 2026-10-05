
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from random import random, seed
b1 = plt.figure()
b2 = b1.gca(projection='3d')
b3 = np.arange(0, 1, 0.05)
b4 = np.arange(0, 1, 0.05)
b3, b4 = np.meshgrid(b3,b4)
def fonk1(b3,b4):
    b5 = 0.75*np.exp(-(0.25*(9*b3-2)**2) - 0.25*((9*b4-2)**2))
    b6 = 0.75*np.exp(-((9*b3+1)**2)/49.0 - 0.1*(9*b4+1))
    b7 = 0.5*np.exp(-(9*b3-7)**2/4.0 - 0.25*((9*b4-3)**2))
    b8 = -0.2*np.exp(-(9*b3-4)**2 - (9*b4-7)**2)
    return (b5 + b6 + b7 + b8)
b9 = fonk1(b3,b4)
b10 = b2.plot_surface(b3, b4, b9, cmap=cm.coolwarm, linewidth=0, antialiased=False)
b2.set_zlim(-0.10, 1.40)
b2.zaxis.set_major_locator(LinearLocator(10))
b2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
b1.colorbar(b10, b11 = 0.5, aspect=5)
plt.show()