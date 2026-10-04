import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = 'p6_reg0'
a1 = 6
a2 = 1
a3 = 0.01
a4 = 10000
a5 = 0.0
def fonk1(z):
    b2 = 1/(1 + np.exp(-z))
    return b2
def fonk2(X, b30):
    b3 = np.zeros([X.shape[0],1])
    b4 = fonk3(X,b30)
    for a7 in range(len(b4)) :
        if b4[a7] > 0.5:
            b3[a7] = 1
        else:
            b3[a7] = 0
    return b3
def fonk3(X, b30):
    b5 = fonk1(b30[0]+np.dot(X,np.transpose(b30[1])))
    return b5
def fonk4(p, y):
    b6 = np.log(p)
    b7 = np.log(1-p)
    b8 = np.multiply(-b27,b6)
    b9 = np.multiply(-(np.ones([b27.shape[0],b27.shape[1]])-b27),b7)
    return b8+b9
def fonk5(X, y, b30, a2):
    b5 = fonk3(X,b30)
    b10 = fonk4(b5,y)
    b11 = np.sum(b10)
    b12 = np.sum(np.square(b30[1]))
    return (0.5/len(X))*(b11 + a2 * b12)
def fonk6(X, y, b30, a2):
    b13 = fonk3(X,b30)-b27
    b14 = np.multiply(b13,X)
    b15 = np.sum(b14,b24 = 0)
    b16 = np.sum(b13)
    b17 = ((b16)/len(X), (b15+a2*b30[1])/len(X))
    return b17
b18 = os.getcwd() + '/data/DecisionBoundaryData.dat'
b19 = pd.read_csv(b18, header=None, names=['Test 1', 'Test 2', 'Accepted'])
b20 = b19[b19['Accepted'].isin([1])]
b21 = b19[b19['Accepted'].isin([0])]
b22 = b19['Test 1']
b23 = b19['Test 2']
a6 = 0
for a7 in range(1, a1+1):
	for j in range(0, a7+1):
		b19['F' + str(a7) + str(j)] = np.power(b22, a7-j) * np.power(b23, j)
		a6 += 1
b19.drop('Test 1', b24 = 1, inplace=True)
b19.drop('Test 2', b24 = 1, inplace=True)
b25 = b19.shape[1]
b26 = b19.iloc[:,1:b25]
b27 = b19.iloc[:,0:1]
b26 = np.array(b26.values)
b27 = np.array(b27.values)
b28 = np.zeros((1,b26.shape[1]))
b29 = np.array([0])
b30 = (b29, b28)
b31 = fonk5(b26, b27, b30, a2)
print("-1 b31 = {0}".format(b31))
a7 = 0
a8 = 0
while(a7 < a4 and a8 = = 0):
    b16, b15 = fonk6(b26, b27, b30, a2)
    b29 = b30[0]
    b28 = b30[1]
    b29 = b29 - a3*b16
    b28 = b28 - a3*b15
    b31 = fonk5(b26, b27, b30, a2)
    b30 = (b29,b28)
    print(" {0} b31 = {1}".format(a7,b31))
    a7 += 1
print("b28 = ",b28)
print("b29 = ",b29)
b32 = fonk2(b26, b30)
b33 = b32 == b27
b33 = b33*1
a9 = 0
for a7 in range(len(b33)):
    if b33[a7] == 1:
        a9 += 1
b34 = 118 - a9
b35 = (a9/118)*100
b36 = 100 - b35
print('b37 = {0}%'.format(b36))
xx, b38 = np.mgrid[-1.2:1.2:.01, -1.2:1.2:.01]
b39 = xx.ravel()
b40 = b38.ravel()
b41 = np.c_[b39, b40]
b42 = []
for a7 in range(1, a1+1):
	for j in range(0, a7+1):
		b43 = np.power(b39, a7-j) * np.power(b40, j)
		if (len(b42) > 0):
			b42 = np.c_[b42, b43]
		else:
			b42 = b43
b44 = fonk3(b42, b30).reshape(xx.shape)
b5, b45 = plt.subplots(figsize=(8, 6))
b45.contour(xx, b38, b44, b46 = [.5], b48="Greys", vmin=0, vmax=.6)
b45.scatter(b22, b23, b47 = b27, s=50,
           b48 = "RdBu", vmin=-.2, vmax=1.2,
           b49 = "white", linewidth=1)
b45.set(b50 = "equal",
       b51 = (-1.5, 1.5), ylim=(-1.5, 1.5),
       b52 = "$X_1$", ylabel="$X_2$")
plt.show()