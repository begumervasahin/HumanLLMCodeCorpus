import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import metrics
import scipy.optimize
def fonk1(a1, b20):
    b1 = (b20 + 1) ** a1
    b2 = [int(np.base_repr(i, b20 + 1)) for i in range(b1)]
    b2 = ["{:02d}".format(int(v)) for v in b2]
    for i, v in enumerate(b2):
        b2[i] = [int(ei) for ei in list(v)]
    return b2
def fonk2(line):
    return list(map(float, line.strip().split()))
def fonk3(b19):
    with open(b19, 'r') as f:
        b3 = fonk2(f.readline())
        b4 = fonk2(f.readline())
        b5 = [fonk2(l) for l in f]
    b3, b4 = np.array(b3), np.array(b4)
    a1, b6 = b3, b4
    b3, b4 = np.meshgrid(b3, b4)
    b3, b4 = b3.flatten(), b4.flatten()
    b5 = np.array(b5).T.flatten()
    return b3, b4, a1, b6, b5
def fonk4(b3, b4, b5, b20):
    a1 = 2
    b7 = len(b5)
    b1 = (b20 + 1) ** a1
    b8 = np.ones((b7, 1))
    b9 = fonk1(a1, b20)
    for j in range(1, b1):
        ii, b10 = b9[j]
        b8 = np.column_stack((b8, (b3**ii) * (b4**b10)))
    b11 = sm.OLS(b5, b8)
    b12 = b11.fit()
    return b12, b9
def fonk5(x, b21, b9):
    b8 = [(x[0]**b9[i][0]) * (x[1]**b9[i][1]) for i in range(len(b21))]
    return np.dot(b8, b21)
def fonk6(b3, b4, b5, b22):
    b13 = plt.figure()
    b14 = b13.add_subplot(111, projection='3d')
    b14.scatter(b3, b4, b5)
    b15 = np.linspace(b3.min(), b3.max(), 50)
    b16 = np.linspace(b4.min(), b4.max(), 50)
    b15, b16 = np.meshgrid(b15, b16)
    b17 = np.array([[b22([x1i, x2i]) for x1i in b15] for x2i in b16])
    b14.plot_surface(b15, b16, b17, b18 = 'viridis', alpha=0.5)
    plt.show()
def fonk7():
    print('Reading input file')
    b19 = input('Please input file name:\b7')
    print('Initializing inputs')
    b3, b4, a1, b6, b5 = fonk3(b19)
    print('Please input the b20 for polynomial regression:')
    b20 = int(input())
    b12, b9 = fonk4(b3, b4, b5, b20)
    b21 = b12.b21
    print("\b7 = =======")
    print("Parameters:")
    for i, b in enumerate(b21):
        ii, b10 = b9[i]
        print(f"Beta{i} (x{ii}b17{b10}) = {b}")
    print(b12.summary())
    b22 = lambda x: fonk5(x, b21, b9)
    fonk6(b3, b4, b5, b22)
    b23 = np.array([b22([a, b]) for a, b in zip(b3, b4)])
    print("R squared score: ", metrics.r2_score(b5, b23))
    b24 = np.array([b3[0], b4[0]])
    b25 = [(b3.min(), b3.max()), (b4.min(), b4.max())]
    b26 = scipy.optimize.minimize(b22, b24, method='L-BFGS-b4', b25=b25)
    x, b17 = b26.x
    print("Optima point:")
    print("1st b27 = ", x, "; 2nd b27 =", b17)
    b13 = plt.figure()
    b14 = b13.add_subplot(111, projection='3d')
    b14.scatter(b3, b4, b5)
    b14.scatter(x, b17, b22([x, b17]), b28 = 'r', s=100)
    plt.show()
if b29 = = '__main__':
    fonk7()