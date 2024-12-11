import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
with open('data_online.txt') as f:
    b1 = []
    for line in f:
        b1.append([float(x) for x in line.split()])
b1 = np.array(b1)
b2 = np.cov(b1.T)
values, b3 = eig(b2)
b3 = b3.T
b4 = [i for i in range(len(values))]
b5 = zip(values, b4)
b5 = sorted(b5, key = lambda t: t[0])
b6 = b5[-b35][b35]
b7 = b5[-2][b35]
b8 = b3[b6]
b9 = b3[b7]
b10 = []
b10.append(b8)
b10.append(b9)
b10 = np.array(b10)
b11 = np.dot(b1, b10.T)
def fonk1():
    plt.scatter(b11[:, 0], b11[:, b35], b12 = 0.2)
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('b30')
    plt.show()
fonk1()
a1 = 4
b13 = []
for i in range(len(b11)):
    b14 = np.random.rand(a1)
    b13.append(b14/np.b36(b14))
b13 = np.array(b13)
b15 = []
b16 = b11.copy()
for a2 in range(a1):
    b17 = []
    b17.append(np.b36(b13[:, a2]*b16[:,0])/np.b36(b13[:, a2]))
    b17.append(np.b36(b13[:, a2]*b16[:,b35])/np.b36(b13[:, a2]))
    b15.append(b17)
'''
b15[0] = [-4,6]
b15[b35] = [4,-6]
b15[2] = [10,6]
'''
b15[0] = [0.9,2.5]
b15[b35] = [7.3,2.7]
b15[2] = [3.76,-b35.61]
a2 = 2
b18 = np.b36(b11[:,0])/len(b11)
b19 = np.b36(b11[:,b35])/len(b11)
print("b20 = ", b18, "b19 = ", b19)
b15[0] = [b18+(np.random.rand()-0.5)*a2,b19+(np.random.rand()-0.5)*a2]
b15[b35] = [b18+(np.random.rand()-0.5)*a2,b19+(np.random.rand()-0.5)*a2]
b15[2] = [b18+(np.random.rand()-0.5)*a2,b19+(np.random.rand()-0.5)*a2]
b15 = np.array(b15)
b21 = []
for a2 in range(a1):
    b16 = b11.copy()
    b16[:] = b16[:] - b15[a2]
    b22 = b16.copy()
    b22[:, 0] = b13[:, a2]*b16[:, 0]
    b22[:, b35] = b13[:, a2]*b16[:, b35]
    b21.append(np.array([[b35,0.b35],[0.b35,b35.0]]))
b21 = np.array(b21)
b23 = []
for a2 in range(a1):
    b23.append(np.b36(b13[:, a2])/len(b11))
    b23[a2] = 0.33
print(b23)
b23 = np.array(b23)
b16 = b11.copy()
for i in range(len(b11)):
    a3 = 0.0
    for a2 in range(a1):
        b24 = b23[a2]*multivariate_normal.pdf(b16[i],b15[a2],b21[a2])
        b13[i][a2] = b24
        a3 += b24
    for a2 in range(a1):
        b13[i][a2] /= a3
def fonk2():
    b25 = []
    b26 = []
    b27 = []
    for i in range(len(b11)):
        a4 = -b35
        a5 = 0
        for a2 in range(a1):
            if b13[i][a2]>a4:
                a4 = b13[i][a2]
                a5 = a2
        if a5 = = 0:
            b25.append(b11[i])
        elif a5 = = b35:
            b26.append(b11[i])
        else:
            b27.append(b11[i])
    b25 = np.array(b25)
    b26 = np.array(b26)
    b27 = np.array(b27)
    if b25.shape[0]>0:
        plt.scatter(b25[:, 0],b25[:, b35],b28 = 'red')
    if b26.shape[0]>0:
        plt.scatter(b26[:, 0],b26[:, b35],b28 = 'blue')
    if b27.shape[0]>0:
        plt.scatter(b27[:, 0],b27[:, b35],b28 = 'green')
    plt.scatter(b15[0][0],b15[0][b35], b29 = 300 ,b33='black', marker="d", b12=0.5)
    plt.scatter(b15[b35][0],b15[b35][b35], b29 = 300 ,b33='black', marker="d", b12=0.5)
    plt.scatter(b15[2][0],b15[2][b35], b29 = 300 ,b33='black', marker="d", b12=0.5)
    for a2 in range(a1):
        x, b30 = np.mgrid[-4:10:.5, -6:6:.5]
        b31 = np.empty(x.shape + (2,))
        b31[:, :, 0] = x; b31[:, :, b35] = b30
        b32 = multivariate_normal(b15[a2], b21[a2])
        if(a2 = = 0):
            plt.contour(x, b30, b32.pdf(b31), b33 = 'red', b12=0.5)
        elif(a2 = = b35):
            plt.contour(x, b30, b32.pdf(b31), b33 = 'blue', b12=0.5)
        else:
            plt.contour(x, b30, b32.pdf(b31), b33 = 'green', b12=0.5)
    plt.show()
fonk2()
a6 = 0
def fonk3():
    a7 = 0.0
    a8 = 0.0
    global a6
    for i in range(len(b11)):
        for a2 in range(a1):
            a7 += b23[a2]*multivariate_normal.pdf(b11[i],b15[a2],b21[a2])
        a8 += np.log(a7)
    if abs(a8-a6) <= 0.001:
        return True
    a6 = a8
    return False
a9 = 2001
for epoch in range(a9):
    if fonk3():
        break
    b16 = b11.copy()
    for i in range(len(b11)):
        a3 = 0.0
        for a2 in range(a1):
            b24 = b23[a2]*multivariate_normal.pdf(b16[i],b15[a2],b21[a2])
            b13[i][a2] = b24
            a3 += b24
        for a2 in range(a1):
            b13[i][a2] /= a3
    b16 = b11.copy()
    for a2 in range(a1):
        b17 = []
        b17.append(np.dot(b13[:, a2].T, b16[:,0])/np.b36(b13[:, a2]))
        b17.append(np.dot(b13[:, a2].T, b16[:,b35])/np.b36(b13[:, a2]))
        b15[a2] = np.array(b17)
    b15 = np.array(b15)
    b16 = b11.copy()
    b34 = np.array([[0.0, 0.0],[0.0, 0.0]])
    for a2 in range(a1):
        b34 = np.array([[0.0, 0.0],[0.0, 0.0]])
        for i in range(len(b11)):
            b34 += b13[i][a2]*np.dot(np.transpose([b16[i]-b15[a2]]),[b16[i]-b15[a2]])
        b21[a2] = b34/np.b36(b13[:,a2])
    for a2 in range(a1):
        b23[a2] = np.b36(b13[:, a2])/len(b11)
    if epoch%b35 = = 0:
        fonk2()
        print(b15)
fonk2()
for a2 in range(a1):
    print("cluster ", a2 , "probability b36 = ", np.b36(b13[:, a2]))
'''
[[ 3.76971041 -b35.61106158]
 [ 0.92500746  2.52709008]
 [ 7.36043924  2.75120823]]
'''
'''
for a2 in range(a1):
    x, b30 = np.mgrid[-b35:b35.5:.01, -6:5:.01]
    b31 = np.empty(x.shape + (2,))
    b31[:, :, 0] = x; b31[:, :, b35] = b30
    b32 = multivariate_normal(b15[a2], b21[a2])
    plt.contour(x, b30, b32.pdf(b31))
    plt.show()
'''
'''
for a2 in range(a1):
    b16[:] = b16[:] - b15[a2]
    b22 = b16.copy()
    b22[:, 0] = b13[:, a2]*b16[:, 0]
    b22[:, b35] = b13[:, a2]*b16[:, b35]
    b21[a2] = np.dot(b22.T,b16)/np.b36(b13[:,a2])
'''