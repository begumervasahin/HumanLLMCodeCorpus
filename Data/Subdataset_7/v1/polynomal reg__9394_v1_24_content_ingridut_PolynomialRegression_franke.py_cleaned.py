from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
def fonk1(b5, b6):
    b1 = 0.75 * np.exp(-(0.25 * (9 * b5 - 2) ** 2) - 0.25 * ((9 * b6 - 2) ** 2))
    b2 = 0.75 * np.exp(-((9 * b5 + 1) ** 2) / 49.0 - 0.1 * (9 * b6 + 1))
    b3 = 0.5 * np.exp(-(9 * b5 - 7) ** 2 / 4.0 - 0.25 * ((9 * b6 - 3) ** 2))
    b4 = -0.2 * np.exp(-(9 * b5 - 4) ** 2 - (9 * b6 - 7) ** 2)
    return b1 + b2 + b3 + b4
b5 = np.arange(0, 1, 0.05)
b6 = np.arange(0, 1, 0.05)
b5, b6 = np.meshgrid(b5, b6)
b7 = fonk1(b5, b6)
b8 = plt.figure()
b9 = b8.gca(projection='3d')
b10 = b9.plot_surface(b5, b6, b7, cmap=cm.coolwarm, linewidth=0, antialiased=False)
b9.set_zlim(-0.10, 1.40)
b9.zaxis.set_major_locator(LinearLocator(10))
b9.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
b8.colorbar(b10, b11 = 0.5, aspect=5)
plt.show()