import numpy as np
import itertools
from statistics import mean
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def fonk1(seq):
    return [float(v) for v in seq.split(',')]
def fonk2(dim, b33):
    b1 = (b33 + 1) ** dim
    b2 = [np.base_repr(i, 3) for i in range(b1)]
    b2 = ["{:02d}".format(int(v)) for v in b2]
    for i, v in enumerate(b2):
        ii, b3 = list(v)
        b2[i] = (int(ii), int(b3))
    return b2[1:]
def fonk3(b16, f):
    b4 = mean(f)
    b5 = sum((fi - b4) ** 2 for fi in f)
    b6 = sum((yi - b20) ** 2 for yi in b16)
    b7 = sum((yi - fi) ** 2 for yi, fi in zip(b16, f))
    b8 = b5 / b6
    print((b5 + b7) / b6)
    return b8
def fonk4(file_path):
    with open(file_path, 'r') as f:
        b9 = fonk1(f.readline())
        b10 = fonk1(f.readline())
        b11 = [fonk1(line) for line in f]
    b11 = np.array(b11).T.flatten()
    return b9, b10, b11
def fonk5(b9, b10, b11, dim, b33):
    b1, b12 = (b33 + 1) ** dim - 1, len(b9) * len(b10)
    b13 = np.zeros((b1, b1))
    b14 = np.zeros(b1)
    b15 = np.zeros((b12, b1))
    b16 = np.array(b11)
    b17 = np.array([(b22, b) for b22, b in itertools.product(b9, b10)])
    b18 = fonk2(dim, b33)
    for i in range(b12):
        for j in range(b1):
            ii, b3 = b18[j]
            b15[i][j] = (b17[i][0] ** ii) * (b17[i][1] ** b3)
    b19 = np.mean(b15, axis=0)
    b20 = mean(b16)
    for j, k in itertools.product(range(b1), b21 = 2):
        b13[j][k] = sum((b15[i][j] - b19[j]) * (b15[i][k] - b19[k]) for i in range(b12))
    for j in range(b1):
        b14[j] = sum((b15[i][j] - b19[j]) * (b16[i] - b20) for i in range(b12))
    b22 = np.dot(np.linalg.inv(b13), b14)
    b23 = b20 - np.dot(b22, b19)
    return b22, b23, b18, b15, b16, b19, b20
def fonk6(b15, b22, b23, b18):
    b24 = [(b15[0] ** b18[i][0]) * (b15[1] ** b18[i][1]) for i in range(len(b22))]
    return np.dot(b24, b22) + b23
def fonk7(b22, b23, b18, b16):
    b25 = np.linspace(14500., 15500.)
    b26 = np.linspace(28., 33.)
    b27 = np.array([[fonk6([x1i, x2i], b22, b23, b18) for x1i in b25] for x2i in b26])
    b28 = plt.figure()
    b29 = b28.gca(projection='3d')
    b25, b26 = np.meshgrid(b25, b26)
    b29.plot_surface(b25, b26, b27, b30 = 1, cstride=1, cmap='viridis', linewidth=0.3)
    b25 = np.linspace(14500, 15500, 6)
    b26 = np.linspace(28, 33, 6)
    b25, b26 = np.meshgrid(b25, b26)
    b29.scatter(b25, b26, b16, b31 = 'r')
    plt.show()
if b32 = = '__main__':
    print('Reading input data')
    b9, b10, b11 = fonk4('aaa.csv')
    print('Constructing Simultaneous Linear Equations')
    dim, b33 = 2, 2
    b22, b23, b18, b15, b16, b19, b20 = fonk5(b9, b10, b11, dim, b33)
    print(f'b23: {b23:>10e}')
    for i, ai in enumerate(b22):
        print(f'b22{i + 1}: {ai:>10e}')
    print('Computing Coefficient of Determination')
    b25 = np.linspace(14500., 15500.)
    b26 = np.linspace(28., 33.)
    b27 = np.array([[fonk6([x1i, x2i], b22, b23, b18) for x1i in b25] for x2i in b26])
    b8 = fonk3(b16, b27.flatten())
    print(f'R2: {b8}')
    print('Plotting Response Surface')
    fonk7(b22, b23, b18, b16)