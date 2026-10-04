import numpy as np
from statsmodels import api as sm
import scipy.optimize
from sklearn import metrics
from matplotlib import pyplot as plt
def fonk1(a1, b18):
    b1 = (b18 + 1) ** a1
    b2 = [int(np.base_repr(i, b18 + 1)) for i in range(b1)]
    b2 = ["{:02d}".format(int(v)) for v in b2]
    for i, v in enumerate(b2):
        b2[i] = [int(ei) for ei in list(v)]
    return b2
def fonk2(b17):
    with open(b17, 'r') as f:
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
def fonk3(b4, b5, b3, b18):
    a1 = 2
    b7 = len(b3)
    b1 = (b18 + 1) ** a1
    b8 = np.ones(b7)
    b9 = fonk1(a1, b18)
    for j in range(1, b1):
        ii, b10 = b9[j]
        b8 = np.column_stack((b8, (b4**ii) * (b5**b10)))
    b11 = sm.OLS(b3, b8)
    b12 = b11.fit()
    return b12, b9
def fonk4(F, a1, b6):
    return np.array([[fonk7([x1i, x2i]) for x1i in a1] for x2i in b6]).flatten()
def fonk5(b21, b4, b5, b3, F):
    b13 = np.linspace(b4.min(), b4.max(), 100)
    b14 = np.linspace(b5.min(), b5.max(), 100)
    b13, b14 = np.meshgrid(b13, b14)
    b15 = np.array([[fonk7([x1i, x2i]) for x1i in b13] for x2i in b14])
    b21.fonk5(b13, b14, b15, b16 = 'viridis')
    b21.scatter(b4, b5, b3)
def fonk6():
    print('Reading input file')
    b17 = input('Please input file name: ')
    print(b17)
    print('Initializing inputs')
    b4, b5, a1, b6, b3 = fonk2(b17)
    print('Please input the b18 for polynomial regression:')
    b18 = int(input())
    b12, b9 = fonk3(b4, b5, b3, b18)
    b19 = b12.b19
    print("\b7 = =======")
    print("Parameters: ")
    for i, b in enumerate(b19):
        ii, b10 = b9[i]
        print(f"Beta{i} (x{ii}b15{b10}) = {b}")
    print(b12.summary())
    def fonk7(x):
        b8 = [(x[0]**b9[i][0]) * (x[1]**b9[i][1]) for i in range(len(b19))]
        b8 = np.array(b8)
        return np.dot(b8, b19)
    b20 = plt.figure()
    b21 = b20.add_subplot(111, projection='3d')
    fonk5(b21, b4, b5, b3, F)
    b22 = fonk4(F, a1, b6)
    print("R squared score: ", metrics.r2_score(b3, b22))
    b23 = np.array([b4[1], b5[1]])
    b24 = np.array([[b4.min(), b4.max()], [b5.min(), b5.max()]])
    b25 = scipy.optimize.minimize(F, b23, method='L-BFGS-b5', b24=b24)
    x_opt, b26 = b25.x
    print("Optima point:")
    print(f"1st b27 = {x_opt}; 2nd b27 = {b26}")
    b21.scatter(x_opt, b26, fonk7([x_opt, b26]), b28 = 'r', marker='x')
    plt.show()
if b29 = = '__main__':
    fonk6()