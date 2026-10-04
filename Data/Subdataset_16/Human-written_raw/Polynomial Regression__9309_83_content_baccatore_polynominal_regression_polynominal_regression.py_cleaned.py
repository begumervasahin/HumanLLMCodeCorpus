import lagrangeMultiplier as lm
from matplotlib import pyplot as plt
from statsmodels import api as sm
import scipy
import numpy as np
from sklearn import metrics
import glob
import sys
def fonk1(b10, b9):
    b1 = (b9+1)**b10
    b2 = [ int(np.base_repr(i,b9+1)) for i in range(b1) ]
    b2 = [ "{:02d}".format(int(v)) for v in b2 ]
    for i, v in enumerate(b2):
        b2[i] = [ int(ei) for ei in list(v) ]
    return b2
def fonk2(b8):
    with open(b8, 'r') as f:
        b3 = []
        b4 = lm.get_data(f.readline())
        b5 = lm.get_data(f.readline())
        for l in f:
            b3.append(lm.get_data(l))
    b4, b5 = np.array(b4), np.array(b5)
    a1, b6 = b4, b5
    b4, b5 = np.meshgrid(b4,b5)
    b4, b5 = b4.flatten(), b5.flatten()
    b3 = np.array(b3)
    b3 = b3.T
    b3 = b3.flatten()
    return (b4, b5,a1,b6, b3)
if b7 = = '__main__':
    print('Reading input file')
    print('Please input file name:')
    print('[NOTE] The prorgram check only the same location as '\
            'this source code locates.')
    b8 = input()
    print(b8)
    print('Initializing inputs')
    b4, b5, a1,b6, b3 = fonk2(b8)
    print()
    print('Please input the b9 for polynominal regression:')
    b9 = input()
    b10 = b9 = 2
    b11 = len(b3)
    b1 = (b9+1)**b10
    b12 = np.repeat(1, b11)
    b13 = fonk1(b10, b9)
    for j in range(1,b1):
        ii, b14 = b13[j]
        b12 = np.column_stack((b12,(b4**ii)*(b5**b14)))
    b15 = sm.OLS(b3,b12)
    b16 = b15.fit()
    b17 = b16.b17
    print("\b11 = =======")
    print("Parameter: ")
    for i, b in enumerate(b17):
        ii, b14 = b13[i]
        print("Beta{} (x{}b21{}) = {}".format(i,ii,b14,b))
    print(b16.summary())
    def fonk3(x):
        b12 = [(x[0]**b13[i][0])*(x[1]**b13[i][1]) for i in range(b1)]
        b12 = np.array(b12)
        return np.dot(b12,b17)
    b18 = plt.figure().gca(projection='3d')
    b18.scatter(b4,b5,b3)
    b19 = np.linspace(b4[0],b4[-1])
    b20 = np.linspace(b5[0],b5[-1])
    b21 = np.array([[ fonk3([x1i,x2i]) for x1i in b19] for x2i in b20])
    b19, b20 = np.meshgrid(b19,b20)
    b18.plot_surface(b19, b20, b21, b22 = 'viridis')
    b23 = np.array([[ fonk3([x1i,x2i]) for x1i in a1] for x2i in b6])
    b23 = b23.flatten()
    print("R squared score (No configured): ", metrics.r2_score(b3,b23))
    b24 = np.array([b4[1],b5[1]])
    b25 = np.array([[b4[0],b4[-1]], [b5[0],b5[-1]]])
    b26 = scipy.optimize.minimize(F, b24, method = 'L-BFGS-b5', b25=b25)
    x, b21 = b26.x
    print("Optima point:")
    print("1st b27 = ", x, "; 2nd b27 =", b21)
    b18.scatter(x,b21,fonk3([x,b21]))
    plt.show()