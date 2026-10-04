
from numpy import *
import operator
from os import listdir
def fonk1(unLabel,dataSet,labels,k):
    b1 = dataSet.shape[0]
    b2 = tile(unLabel, (b1, 1)) - dataSet
    b3 = b2**2
    b4 = sum(b3, axis = 1)
    b5 = b4**0.5
    b6 = argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = labels[b6[i]]
        b7[b8]=b7.get(b8,0)+1
    a1 = 0
    for key, value in b7.items():
        if value>a1:
            a1 = value
            b9 = key
    return b9
def fonk2(filename,dim2):
    b10 = open(filename)
    b11 = b10.readlines()
    b12 = len(b11)
    b13 = zeros((b12,dim2))
    b14 = []
    b10 = open(filename)
    a2 = 0
    for b15 in b11:
        b15 = b15.strip()
        b16 = b15.split('\t')
        b13[a2,:] = b16[0:dim2]
        b14.append(int(b16[-1]))
        a2 += 1
    return b13,b14
import matplotlib
import matplotlib.pyplot as plt
def fonk3(datingDataMat,b26):
    b17 = plt.figure()
    b18 = b17.add_subplot(111)
    b18.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(b26),15.0*array(b26))
    plt.show()
def fonk4(dataSet):
    b19 = dataSet.min(0)
    b20 = dataSet.max(0)
    b21 = b20 - b19
    b22 = dataSet.shape[0]
    b23 = tile(b19,(b22,1))
    b24 = tile(b20,(b22,1))
    b25 = zeros(shape(dataSet))
    b25 = (dataSet-b23)/(b24-b23)
    return b25, b21, b19
def fonk5():
    a3 = 0.1
    datingDataMat,b26 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt',3)
    normMat, b21,b19 = fonk4(datingDataMat)
    b27 = int((normMat.shape[0])*a3)
    a4 = 0.0
    for i in range(b27):
        b28 = fonk1(normMat[i,:],normMat[b27:normMat.shape[0],:],b26[b27:normMat.shape[0]],3)
        print 'result from KNN Classifier class1:  %d, the actual class class1 : %d' % (b28,b26[i])
        if (b28 != b26[i]):
            a4+=1
    print 'the total error a3 class1: %f' % (a4/(b27*1.0))
def fonk6():
    b29 = ['not at all','in small does','in large does']
    b30 = float(raw_input('percentage of time spent playing video games?'))
    b31 = float(raw_input('frequent flier miles earned per year?'))
    b32 = float(raw_input('liters of ice cream consumed per year?'))
    datingDataMat,b26 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt',3)
    normMat, b21,b19 = fonk4(datingDataMat)
    b33 = array([b30,b31,b32])
    b28 = fonk1((b33-b19)/b21,normMat,b26,3)
    print 'You will probably like this person: ', b29[b28-1]