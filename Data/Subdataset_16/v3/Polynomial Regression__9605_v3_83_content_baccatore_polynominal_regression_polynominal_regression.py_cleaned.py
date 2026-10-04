import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import metrics
import scipy.optimize
def fonk1(a1, b23):
    b1 = (b23 + 1) ** a1
    b2 = [int(np.base_repr(i, b23 + 1)) for i in range(b1)]
    b3 = ["{:02d}".format(int(v)) for v in b2]
    b4 = []
    for combo in b3:
        b4.append([int(digit) for digit in list(combo)])
    return b4
def fonk2(line):
    return list(map(float, line.strip().split()))
def fonk3(b22):
    with open(b22, 'r') as file:
        b5 = fonk2(file.readline())
        b6 = fonk2(file.readline())
        b7 = [fonk2(line) for line in file]
    b5, b6 = np.array(b5), np.array(b6)
    a1, b8 = b5, b6
    b5, b6 = np.meshgrid(b5, b6)
    b5, b6 = b5.flatten(), b6.flatten()
    b7 = np.array(b7).T.flatten()
    return b5, b6, a1, b8, b7
def fonk4(b5, b6, b7, b23):
    a1 = 2
    b9 = len(b7)
    b10 = (b23 + 1) ** a1
    b11 = np.ones((b9, 1))
    b4 = fonk1(a1, b23)
    for j in range(1, b10):
        power_A, b12 = b4[j]
        b11 = np.column_stack((b11, (b5**power_A) * (b6**b12)))
    b13 = sm.OLS(b7, b11)
    b14 = b13.fit()
    return b14, b4
def fonk5(x, b24, b4):
    b15 = [(x[0]**b4[i][0]) * (x[1]**b4[i][1]) for i in range(len(b24))]
    return np.dot(b15, b24)
def fonk6(b5, b6, b7, b26):
    b16 = plt.figure()
    b17 = b16.add_subplot(111, projection='3d')
    b17.scatter(b5, b6, b7)
    b18 = np.linspace(b5.min(), b5.max(), 50)
    b19 = np.linspace(b6.min(), b6.max(), 50)
    b18, b19 = np.meshgrid(b18, b19)
    b20 = np.array([[b26([x1i, x2i]) for x1i in b18] for x2i in b19])
    b17.plot_surface(b18, b19, b20, b21 = 'viridis', alpha=0.5)
    plt.show()
def fonk7():
    print('Reading input file')
    b22 = input('Please input file name:\b25')
    print('Initializing inputs')
    b5, b6, a1, b8, b7 = fonk3(b22)
    print('Please input the b23 for polynomial regression:')
    b23 = int(input())
    b14, b4 = fonk4(b5, b6, b7, b23)
    b24 = b14.b24
    print("\b25 = =======")
    print("Parameters:")
    for i, param in enumerate(b24):
        power_A, b12 = b4[i]
        print(f"Beta{i} (x{power_A}b20{b12}) = {param}")
    print(b14.summary())
    b26 = lambda x: fonk5(x, b24, b4)
    fonk6(b5, b6, b7, b26)
    b27 = np.array([b26([a, b]) for a, b in zip(b5, b6)])
    print("R squared score: ", metrics.r2_score(b7, b27))
    b28 = np.array([b5[0], b6[0]])
    b29 = [(b5.min(), b5.max()), (b6.min(), b6.max())]
    b30 = scipy.optimize.minimize(b26, b28, method='L-BFGS-b6', b29=b29)
    x_opt, b31 = b30.x
    print("Optima point:")
    print("1st b32 = ", x_opt, "; 2nd b32 =", b31)
    b16 = plt.figure()
    b17 = b16.add_subplot(111, projection='3d')
    b17.scatter(b5, b6, b7)
    b17.scatter(x_opt, b31, b26([x_opt, b31]), b33 = 'r', s=100)
    plt.show()
if b34 = = '__main__':
    fonk7()