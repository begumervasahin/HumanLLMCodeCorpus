import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import pickle
from mlxtend.data import loadlocal_mnist
X_train, b1 = loadlocal_mnist(images_path='./train-images.idx3-ubyte', labels_path='./train-labels.idx1-ubyte')
X_test, b2 = loadlocal_mnist(images_path='./t10k-images.idx3-ubyte', labels_path='./t10k-labels.idx1-ubyte')
b3 = []
b4 = []
for i in range(len(b1)):
    if(b1[i]== 1 or b1[i]== 2):
        b3.append(b1[i]-1)
for i in range(len(b2)):
    if(b2[i]== 1 or b2[i]== 2):
        b4.append(b2[i]-1)
b1 = b3
b2 = b4
b5 = open('./bintrain.pkl', 'rb')
b6 = pickle.load(b5)
b5 = open('./bintest.pkl', 'rb')
b7 = pickle.load(b5)
b8 = np.load('./b8.mat')
b9 = np.load('./b9.mat')
b10 = b1.count(0)
b11 = b1.count(1)
b12 = b10/(b10+b11)
b13 = b11/(b10+b11)
for i in range(len(b8)):
    for b14 in range(2):
        if(b14 = = 0):
            b8[i][b14]/= b10
            b9[i][b14]/= b10
        else:
            b8[i][b14]/= b11
            b9[i][b14]/= b11
print ("The prior trouser is: ", b12)
print ("The prior pullover is: ", b13)
b15 = np.zeros(shape= (5, len(b7)))
b16 = [0.3, 0.4, 0.5, 0.6, 0.7]
for k in range(len(b16)):
    for i in range(len(b7)):
        a1 = 0
        a2 = 0
        for b14 in range(len(b7[0])):
            if(b7[i][b14]== 1):
                a1+= math.log(b9[b14][0])
                a2+= math.log(b9[b14][1])
            else:
                a1+= math.log(b8[b14][0])
                a2+= math.log(b8[b14][1])
        b17 = (a1*b12)/(a1*b12 + a2*b13)
        if(b17<= b16[k]):
            b15[k][i]=0
        else:
            b15[k][i]=1
print ("Lengths: ", len(b15), len(b2))
print (b15[:, 0], b15[:, 1])
b18 = []
b19 = []
for i in range(5):
    b20 = np.zeros(shape=(2, 2))
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    for b14 in range(len(b2)):
        if(b15[i][b14]== 0 and b2[b14]== 0):
            a3+= 1
        elif(b15[i][b14]== 1 and b2[b14]== 1):
            a6+= 1
        elif(b15[i][b14]== 0 and b2[b14]== 1):
            a4+= 1
        elif(b15[i][b14]== 1 and b2[b14]== 0):
            a5+= 1
    b20[0][0]= a3
    b20[1][1]= a6
    b20[0][1]= a4
    b20[1][0]= a5
    b18.append(a3/(a3+a5))
    b19.append(a4/(a4+a6))
    print ("CASE" + str(i+1) + " :-")
    print (b20)
    print ("The precision is: " + str((a3/(a3+a4))))
    print ("The recall is: " + str((a3/(a3+a5))))
plt.plot(b19, b18)
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.title("ROC Curve")
plt.show()