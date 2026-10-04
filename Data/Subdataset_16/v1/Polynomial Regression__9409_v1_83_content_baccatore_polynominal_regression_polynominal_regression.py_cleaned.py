import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import metrics
import scipy.optimize
def fonk1(a1, b9):
    b1 = (b9 + 1) ** a1
    b2 = [int(np.base_repr(i, b9 + 1)) for i in range(b1)]
    b2 = ["{:02d}".format(int(v)) for v in b2]
    for i, v in enumerate(b2):
        b2[i] = [int(ei) for ei in list(v)]
    return b2
def fonk2(line):
    return list(map(float, line.strip().split()))
def fonk3(b8):
    with open(b8, 'r') as f:
        b3 = []
        b4 = fonk2(f.readline())
        b5 = fonk2(f.readline())
        for l in f:
            b3.append(fonk2(l))
    b4, b5 = np.array(b4), np.array(b5)
    a1, b6 = b4, b5
    b4, b5 = np.meshgrid(b4, b5)
    b4, b5 = b4.flatten(), b5.flatten()
    b3 = np.array(b3)
    b3 = b3.T
    b3 = b3.flatten()
    return (b4, b5, a1, b6, b3)
if b7 = = '__main__':
    print('Reading input file')
    b8 = input('Please input file name:\b10')
    print('Initializing inputs')
    b4, b5, a1, b6, b3 = fonk3(b8)
    print('Please input the b9 for polynomial regression:')
    b9 = int(input())
    a1 = 2
    b10 = len(b3)
    b1 = (b9 + 1) ** a1
    b11 = np.ones(b10)
    b12 = fonk1(a1, b9)
    for j in range(1, b1):
        ii, b13 = b12[j]
        b11 = np.column_stack((b11, (b4**ii) * (b5**b13)))
    b14 = sm.OLS(b3, b11)
    b15 = b14.fit()
    b16 = b15.b16
    print("\b10 = =======")
    print("Parameters:")
    for i, b in enumerate(b16):
        ii, b13 = b12[i]
        print(f"Beta{i} (x{ii}b21{b13}) = {b}")
    print(b15.summary())
    def fonk4(x):
        b11 = [(x[0]**b12[i][0]) * (x[1]**b12[i][1]) for i in range(b1)]
        b11 = np.array(b11)
        return np.dot(b11, b16)
    b17 = plt.figure()
    b18 = b17.add_subplot(111, projection='3d')
    b18.scatter(b4, b5, b3)
    b19 = np.linspace(b4.min(), b4.max(), 50)
    b20 = np.linspace(b5.min(), b5.max(), 50)
    b19, b20 = np.meshgrid(b19, b20)
    b21 = np.array([[fonk4([x1i, x2i]) for x1i in b19] for x2i in b20])
    b18.plot_surface(b19, b20, b21, b22 = 'viridis', alpha=0.5)
    plt.show()
    b23 = np.array([fonk4([a, b]) for a, b in zip(b4, b5)])
    print("R squared score (No configured): ", metrics.r2_score(b3, b23))
    b24 = np.array([b4[0], b5[0]])
    b25 = [(b4.min(), b4.max()), (b5.min(), b5.max())]
    b26 = scipy.optimize.minimize(F, b24, method='L-BFGS-b5', b25=b25)
    x, b21 = b26.x
    print("Optima point:")
    print("1st b27 = ", x, "; 2nd b27 =", b21)
    b18.scatter(x, b21, fonk4([x, b21]), b28 = 'r', s=100)
    plt.show()