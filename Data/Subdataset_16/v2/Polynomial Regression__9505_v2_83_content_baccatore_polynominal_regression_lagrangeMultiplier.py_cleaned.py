import numpy as np
import itertools
from statistics import mean
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def fonk1(seq):
    return [float(v) for v in seq.split(',')]
def fonk2(a1, a2):
    b1 = (a2 + 1) ** a1
    b2 = [int(np.base_repr(i, base=3)) for i in range(b1)]
    b3 = ["{:02d}".format(int(v)) for v in b2]
    for i, v in enumerate(b3):
        ii, b4 = list(v)
        b3[i] = (int(ii), int(b4))
    return b3[1:]
def fonk3(b18, f):
    b5 = mean(f)
    b6 = sum([(fi - b5)**2 for fi in f])
    b7 = sum([(yi - b22)**2 for yi in b18])
    b8 = sum([(yi - fi)**2 for yi, fi in zip(f, b18)])
    b9 = b6 / b7
    print((b6 + b8) / b7)
    return b9
if b10 = = '__main__':
    print('Reading input data')
    with open('aaa.csv', 'r') as f:
        b11 = []
        b12 = fonk1(f.readline())
        b13 = fonk1(f.readline())
        for line in f:
            b11.append(fonk1(line))
    b11 = np.array(b11).T.flatten()
    print('Constructing Simultaneous Linear Equations')
    a1 = 2
    a2 = 2
    p, b14 = (a2 + 1) ** a1 - 1, 6 * 6
    b15 = np.zeros([p, p])
    b16 = M = np.zeros([p])
    b17 = np.zeros([b14, p])
    b18 = np.zeros([b14])
    b19 = [(b16, b) for b16, b in itertools.product(b12, b13)]
    b19 = np.array(b19)
    b20 = fonk2(a1, a2)
    for i in range(b14):
        for j in range(p):
            ii, b4 = b20[j]
            b17[i][j] = (b19[i][0] ** ii) * (b19[i][1] ** b4)
    b18 = np.array(b11)
    b21 = [mean(b17[:, j]) for j in range(p)]
    b22 = mean(b18)
    print('Computing Variance-Covariance Matrix Sjk')
    for j, k in itertools.product(range(p), b23 = 2):
        b15[j][k] = sum([(b17[i][j] - b21[j]) * (b17[i][k] - b21[k]) for i in range(b14)])
    print('Computing Sum of Deviation Vector M')
    for j in range(p):
        M[j] = sum([(b17[i][j] - b21[j]) * (b18[i] - b22) for i in range(b14)])
    print('Computing Coefficient Vector b16')
    b16 = np.dot(np.linalg.inv(b15), M)
    print('Generating Polynomial Function F')
    b24 = [(14500. ** b20[i][0]) * (28. ** b20[i][1]) for i in range(p)]
    b24 = np.array(b24)
    b25 = b22 - np.dot(b16, b21)
    print(f'b25: {b25:> 10e}')
    for i, ai in enumerate(b16):
        print(f'b16{i + 1}: {ai:> 10e}')
    def fonk4(b17):
        b24 = [(b17[0] ** b20[i][0]) * (b17[1] ** b20[i][1]) for i in range(p)]
        b24 = np.array(b24)
        return np.dot(b24, b16) + b25
    print('Computing Coefficient of Determination')
    b26 = np.linspace(14500., 15500.)
    b27 = np.linspace(28., 33.)
    b28 = [[fonk4([x1i, x2i]) for x1i in b26] for x2i in b27]
    b28 = np.array(b28)
    print(f'R2: {fonk3(b18.flatten(), b28.flatten())}')
    print('Plotting Response Surface')
    b29 = plt.figure()
    b30 = b29.add_subplot(111, projection='3d')
    b26, b27 = np.meshgrid(b26, b27)
    b30.plot_surface(b26, b27, b28, b31 = 1, cstride=1, cmap='viridis', linewidth=0.3)
    b26 = np.linspace(14500, 15500, 6)
    b27 = np.linspace(28, 33, 6)
    b26, b27 = np.meshgrid(b26, b27)
    b30.scatter(b26, b27, b18, b32 = 'r')
    plt.show()