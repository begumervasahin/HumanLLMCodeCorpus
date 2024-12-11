import numpy as np
import pandas as pd
from random import random, seed
def fonk1(b23, Ypred):
    b1 = np.sqrt(sum((b23 - Ypred) ** 2) / len(b23))
    return b1
def fonk2(b23, b18):
    b2 = np.mean(b23)
    b3 = sum((b23 - b2) ** 2)
    b4 = sum((b23 - b18) ** 2)
    b5 = 1 - (b4 / b3)
    return b5
def fonk3(b22, b23, b15):
    b6 = len(b23)
    b7 = np.sum((b22.dot(b15) - b23) ** 2)/(2 * b6);
    return b7
def fonk4(b22, b23, b15, b24, b8 = 10000):
    b6 = len(b23)
    b9 = [];
    b10 = [];
    b11 = 0;
    while b11 <b8:
        b12 = b22.dot(b15)
        b13 = b12 - b23
        b14 = b22.T.dot(b13) / b6
        b15 = b15 - b24 * b14
        b16 = fonk3(b22, b23, b15);
        b9.append(b16);
        b11 = b11+1;
        b10.append(b15);
    return b15, b9,b10
def fonk5(b22,b23,b15,newW,b9,b8,b10):
    b17 = fonk3(b22, b23, b15);
    b18 = b22.dot(newW)
    b19 = '=' * 80;
    print(b19)
    print("MULTI LINEAR REGRESSION USING GRADIENT DESCENT TERMINATION RESULTS")
    print(b19)
    print("Initial Weights were:    {:>12.1f}, {:>2.1f}, {:>2.1f}.".format(b15[0],b15[1],b15[2]))
    print("   With initial b16:    {:>12,.1f}.".format(b17))
    print("
    print("       Final weights:    w0:{:>+0.2f}, w1:{:>+3.2f}, w2:{:>+3.3f}.".format(newW[0], newW[1], newW[2]))
    print("          Final b16:    {:>+12.1f}.".format(b9[-1]))
    print("                RMSE:    {:>+12.1f}, R-Squared: {:>+12.1f}".format(fonk1(b23, b18),fonk2(b23, b18)))
    print(b19)
def fonk6(b31,b24,b8):
    b20 = b31.shape[1]-1;
    b15 = (b20+1)*[0];
    b21 = np.ones(b31.shape[0]);
    b22 = np.column_stack((b21,b31.iloc[:, 1:(b20 + 1)].values));
    b23 = np.array(b31.iloc[:,0]);
    newW, b9,b10 = fonk4(b22, b23, b15, b24,b8)
    fonk5(b22, b23, b15, newW, b9, b8,b10);
    return
def fonk7():
    b24 = 0.0001;
    b8 = 2500000;
    np.random.seed(1234)
    b25 = 500;
    b26 = [70, 70]
    b27 = [9,9]
    a1 = 0.8
    b28 = [[b27[0] ** 2, b27[0] * b27[1] * a1],[b27[0] * b27[1] * a1, b27[1] ** 2]]
    b29 = np.random.multivariate_normal(b26, b28, b25).T
    b30 = (b29[0] + b29[1])/2.5 + np.random.normal(loc=25, scale=4, size=b25);
    b31 = np.vstack((b30, b29));
    b31 = pd.DataFrame({"JobPotential":b31[0],"AI":b31[1],"MachineLearning":b31[2]});
    fonk6(b31, b24, b8);
    print("Finished");
if b32 = = '__main__':
    fonk7()