
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
def fonk2(fileName):
    b10 = zeros((1,1024))
    b11 = open(fileName)
    for i in range(32):
        b12 = b11.readline()
        for j in range(32):
            b10[0,32*i+j] = int(b12[j])
    return b10
def fonk3():
    b13 = []
    b14 = listdir('/Users/ceciliaLee/Desktop/digits/trainingDigits')
    b15 = len(b14)
    b16 = zeros((b15,1024))
    for i in range(b15):
        b17 = b14[i]
        b18 = b17.split('.')[0]
        b19 = int(b18.split('_')[0])
        b13.append(b19)
        b16[i,:]=fonk2('/Users/ceciliaLee/Desktop/digits/trainingDigits/%s' % b17)
    b20 = listdir('/Users/ceciliaLee/Desktop/digits/testDigits')
    b21 = len(b20)
    a2 = 0.0
    for i in range(b21):
        b17 = b20[i]
        b18 = b17.split('.')[0]
        b19 = int(b18.split('_')[0])
        b22 = fonk2('/Users/ceciliaLee/Desktop/digits/testDigits/%s' % b17)
        b23 = fonk1(b22,b16,b13,3)
        print 'The classified result by KNN class1: %d, the actual class class1: %d' % (b23,b19)
        if (b23 != b19):
            a2+=1
    print '\nThe total number of incorrectly classified samples class1: %d' % a2
    print '\nThe error rate class1: %f' % (a2/(b21*0.1))