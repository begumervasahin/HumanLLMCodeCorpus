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
def fonk4(filename):
    with open(filename, 'r') as f:
        b10 = []
        b11 = fonk1(f.readline())
        b12 = fonk1(f.readline())
        for line in f:
            b10.append(fonk1(line))
    b10 = np.array(b10).T.flatten()
    return b11, b12, b10
def fonk5(b11, b12, b10, a1, a2):
    b13 = (a2 + 1) ** a1 - 1
    b14 = len(b11) * len(b12)
    b15 = np.zeros([b13, b13])
    b16 = np.zeros([b13])
    b17 = np.zeros([b14, b13])
    b18 = np.zeros([b14])
    b19 = [(b16, b) for b16, b in itertools.product(b11, b12)]
    b19 = np.array(b19)
    b20 = fonk2(a1, a2)
    for i in range(b14):
        for j in range(b13):
            ii, b4 = b20[j]
            b17[i][j] = (b19[i][0] ** ii) * (b19[i][1] ** b4)
    b18 = np.array(b10)
    return b17, b18, b15, b16, b13
def fonk6(b17, b18, b15, b13):
    b21 = [mean(b17[:, j]) for j in range(b13)]
    b22 = mean(b18)
    for j, k in itertools.product(range(b13), b23 = 2):
        b15[j][k] = sum([(b17[i][j] - b21[j]) * (b17[i][k] - b21[k]) for i in range(len(b18))])
    b24 = np.zeros([b13])
    for j in range(b13):
        b24[j] = sum([(b17[i][j] - b21[j]) * (b18[i] - b22) for i in range(len(b18))])
    return b15, b24, b21, b22
def fonk7(b15, b24, b21, b22):
    b16 = np.dot(np.linalg.inv(b15), b24)
    b25 = b22 - np.dot(b16, b21)
    return b16, b25
def fonk8(b16, b25, b20):
    def fonk9(b17):
        b26 = [(b17[0] ** b20[i][0]) * (b17[1] ** b20[i][1]) for i in range(len(b16))]
        b26 = np.array(b26)
        return np.dot(b26, b16) + b25
    return b35
def fonk10(b35, b18):
    b27 = np.linspace(14500., 15500.)
    b28 = np.linspace(28., 33.)
    b29 = [[fonk9([x1i, x2i]) for x1i in b27] for x2i in b28]
    b29 = np.array(b29)
    b30 = plt.figure()
    b31 = b30.add_subplot(111, projection='3d')
    b27, b28 = np.meshgrid(b27, b28)
    b31.plot_surface(b27, b28, b29, b32 = 1, cstride=1, cmap='viridis', linewidth=0.3)
    b27 = np.linspace(14500, 15500, 6)
    b28 = np.linspace(28, 33, 6)
    b27, b28 = np.meshgrid(b27, b28)
    b31.scatter(b27, b28, b18, b33 = 'r')
    plt.show()
if b34 = = '__main__':
    print('Reading input data')
    b11, b12, b10 = fonk4('aaa.csv')
    print('Constructing Simultaneous Linear Equations')
    a1 = 2
    a2 = 2
    b17, b18, b15, b16, b13 = fonk5(b11, b12, b10, a1, a2)
    print('Computing Variance-Covariance Matrix Sjk and Sum of Deviation Vector b24')
    b15, b24, b21, b22 = fonk6(b17, b18, b15, b13)
    print('Computing Coefficient Vector b16')
    b16, b25 = fonk7(b15, b24, b21, b22)
    print('Generating Polynomial Function b35')
    b20 = fonk2(a1, a2)
    b35 = fonk8(b16, b25, b20)
    print(f'b25: {b25:> 10e}')
    for i, ai in enumerate(b16):
        print(f'b16{i + 1}: {ai:> 10e}')
    print('Computing Coefficient of Determination')
    fonk3(b18, [fonk9([b27, b28]) for b27, b28 in itertools.product(b11, b12)])
    print('Plotting Response Surface')
    fonk10(b35, b18)