import numpy as np
import itertools
from statistics import mean
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def fonk1(seq):
    return [float(v) for v in seq.split(',')]
def fonk2(a1, a2):
    b1 = (a2+1)**a1
    b2 = [int(np.base_repr(i, 3)) for i in range(b1)]
    b2 = ["{:02d}".format(int(v)) for v in b2]
    for i, v in enumerate(b2):
        ii, b3 = list(v)
        b2[i] = (int(ii), int(b3))
    return b2[1:]
def fonk3(b17, f):
    b4 = mean(f)
    b5 = sum([(fi - b4)**2 for fi in f])
    b6 = sum([(yi - b21)**2 for yi in b17])
    b7 = sum([(yi - fi)**2 for yi, fi in zip(f, b17)])
    b8 = b5 / b6
    print((b5 + b7) / b6)
    return b8
if b9 = = '__main__':
    print('Reading input data')
    with open('aaa.csv', 'r') as f:
        b10 = []
        b11 = fonk1(f.readline())
        b12 = fonk1(f.readline())
        for l in f:
            b10.append(fonk1(l))
    b10 = np.array(b10).T.flatten()
    print('Constructing Simultaneous Linear Equations')
    a1 = 2
    a2 = 2
    b1, b13 = (a2 + 1) ** a1 - 1, 6 * 6
    b14 = np.zeros([b1, b1])
    b15 = M = np.zeros([b1])
    b16 = np.zeros([b13, b1])
    b17 = np.zeros([b13])
    b18 = [(b15, b19) for b15, b19 in itertools.product(b11, b12)]
    b18 = np.array(b18)
    b19 = fonk2(a1, a2)
    for i in range(b13):
        for j in range(b1):
            ii, b3 = b19[j]
            b16[i][j] = (b18[i][0]**ii) * (b18[i][1]**b3)
    b17 = np.array(b10)
    b20 = [mean(b16[:, j]) for j in range(b1)]
    b21 = mean(b17)
    print('Computing Variance-Covariance Matrix Sjk')
    for j, k in itertools.product(range(b1), b22 = 2):
        b14[j][k] = sum([(b16[i][j] - b20[j]) * (b16[i][k] - b20[k]) for i in range(b13)])
    print('Computing Sum of Deviation Vector M')
    for j in range(b1):
        M[j] = sum([(b16[i][j] - b20[j]) * (b17[i] - b21) for i in range(b13)])
    print('Computing Coefficient Vector b15')
    b15 = np.dot(np.linalg.inv(b14), M)
    print('Generating Polynomial Function F')
    b23 = [(14500.**b19[i][0]) * (28.**b19[i][1]) for i in range(b1)]
    b23 = np.array(b23)
    b24 = b21 - np.dot(b15, b20)
    print('b24: {:> 10e}'.format(b24))
    for i, ai in enumerate(b15):
        print('b15{:}: {:> 10e}'.format(i + 1, ai))
    def fonk4(b16):
        b23 = [(b16[0]**b19[i][0]) * (b16[1]**b19[i][1]) for i in range(b1)]
        b23 = np.array(b23)
        return np.dot(b23, b15) + b24
    print('Computing Coefficient of Determination')
    b25 = np.linspace(14500., 15500.)
    b26 = np.linspace(28., 33.)
    b27 = [[fonk4([x1i, x2i]) for x1i in b25] for x2i in b26]
    b27 = np.array(b27)
    print('R2: {}'.format(fonk3(b17.flatten(), b27.flatten())))
    print('Plotting Response Surface')
    b28 = plt.figure()
    b29 = b28.gca(projection='3d')
    b25, b26 = np.meshgrid(b25, b26)
    b29.plot_surface(b25, b26, b27, b30 = 1, cstride=1, cmap='viridis', linewidth=0.3)
    b25 = np.linspace(14500, 15500, 6)
    b26 = np.linspace(28, 33, 6)
    b25, b26 = np.meshgrid(b25, b26)
    b29.scatter(b25, b26, b17, b31 = 'r')
    plt.show()