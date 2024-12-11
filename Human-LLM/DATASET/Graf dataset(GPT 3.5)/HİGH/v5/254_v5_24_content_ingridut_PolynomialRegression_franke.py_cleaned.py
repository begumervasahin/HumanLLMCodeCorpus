import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
def fonk1(x, y):
    b1 = 0.75 * np.exp(-(0.25 * (9*x - 2)**2) - 0.25 * ((9*y - 2)**2))
    b2 = 0.75 * np.exp(-((9*x + 1)**2) / 49.0 - 0.1 * (9*y + 1))
    b3 = 0.5 * np.exp(-(9*x - 7)**2 / 4.0 - 0.25 * ((9*y - 3)**2))
    b4 = -0.2 * np.exp(-(9*x - 4)**2 - (9*y - 7)**2)
    return b1 + b2 + b3 + b4
b5 = np.arange(0, 1, 0.05)
b6 = np.arange(0, 1, 0.05)
x_mesh, b7 = np.meshgrid(b5, b6)
b8 = fonk1(x_mesh, b7)
b9 = plt.figure()
b10 = b9.gca(projection='3d')
b11 = b10.plot_surface(x_mesh, b7, b8, cmap=cm.coolwarm, linewidth=0, antialiased=False)
b10.set_zlim(-0.10, 1.40)
b10.zaxis.set_major_locator(LinearLocator(10))
b10.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
b9.colorbar(b11, b12 = 0.5, aspect=5)
plt.show()