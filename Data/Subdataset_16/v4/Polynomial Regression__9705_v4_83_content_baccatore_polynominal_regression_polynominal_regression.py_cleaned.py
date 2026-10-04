import numpy as np
from statsmodels import api as sm
import scipy.optimize
from sklearn import metrics
from matplotlib import pyplot as plt
def fonk1(a1, b8):
    b1 = (b8 + 1) ** a1
    b2 = [int(np.base_repr(i, b8 + 1)) for i in range(b1)]
    b2 = ["{:02d}".format(int(v)) for v in b2]
    for i, v in enumerate(b2):
        b2[i] = [int(ei) for ei in list(v)]
    return b2
def fonk2(b7):
    with open(b7, 'r') as f:
        b3 = []
        b4 = lm.get_data(f.readline())
        b5 = lm.get_data(f.readline())
        for line in f:
            b3.append(lm.get_data(line))
    b4, b5 = np.array(b4), np.array(b5)
    a1, b6 = b4, b5
    b4, b5 = np.meshgrid(b4, b5)
    b4, b5 = b4.flatten(), b5.flatten()
    b3 = np.array(b3).T.flatten()
    return b4, b5, a1, b6, b3
def fonk3():
    print('Reading input file')
    b7 = input('Please input file name: ')
    print(b7)
    print('Initializing inputs')
    b4, b5, a1, b6, b3 = fonk2(b7)
    print('Please input the b8 for polynomial regression:')
    b8 = int(input())
    a1 = 2
    b9 = len(b3)
    b1 = (b8 + 1) ** a1
    b10 = np.ones(b9)
    b11 = fonk1(a1, b8)
    for j in range(1, b1):
        ii, b12 = b11[j]
        b10 = np.column_stack((b10, (b4**ii) * (b5**b12)))
    b13 = sm.OLS(b3, b10)
    b14 = b13.fit()
    b15 = b14.b15
    print("\b9 = =======")
    print("Parameters: ")
    for i, b in enumerate(b15):
        ii, b12 = b11[i]
        print(f"Beta{i} (x{ii}b20{b12}) = {b}")
    print(b14.summary())
    def fonk4(x):
        b10 = [(x[0]**b11[i][0]) * (x[1]**b11[i][1]) for i in range(b1)]
        b10 = np.array(b10)
        return np.dot(b10, b15)
    b16 = plt.figure()
    b17 = b16.add_subplot(111, projection='3d')
    b17.scatter(b4, b5, b3)
    b18 = np.linspace(b4.min(), b4.max(), 100)
    b19 = np.linspace(b5.min(), b5.max(), 100)
    b18, b19 = np.meshgrid(b18, b19)
    b20 = np.array([[fonk4([x1i, x2i]) for x1i in b18] for x2i in b19])
    b17.plot_surface(b18, b19, b20, b21 = 'viridis')
    b22 = np.array([[fonk4([x1i, x2i]) for x1i in a1] for x2i in b6]).flatten()
    print("R squared score (No configured): ", metrics.r2_score(b3, b22))
    b23 = np.array([b4[1], b5[1]])
    b24 = np.array([[b4.min(), b4.max()], [b5.min(), b5.max()]])
    b25 = scipy.optimize.minimize(F, b23, method='L-BFGS-b5', b24=b24)
    x_opt, b26 = b25.x
    print("Optima point:")
    print(f"1st b27 = {x_opt}; 2nd b27 = {b26}")
    b17.scatter(x_opt, b26, fonk4([x_opt, b26]), b28 = 'r', marker='x')
    plt.show()
if b29 = = '__main__':
    fonk3()