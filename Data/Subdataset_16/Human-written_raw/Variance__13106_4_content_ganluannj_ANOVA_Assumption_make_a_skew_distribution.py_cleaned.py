import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as stats
b1 = [-1.73,1.73]
def lessthan (listlessthan, alpha):
    b2 = len (listlessthan)
    a1 = 0
    a2 = 0.000
    while a1 < b2:
        if listlessthan[a1]<alpha:
            a2 = a2+1
        a1 = a1+1
    b3 = a2/b2
    return (b3)
def pdf (b11, uniformvalue):
    return (1-uniformvalue)*stats.norm.pdf(b11)+0.289*uniformvalue
def fonk1(rangen, uniformvalue1):
    a3 = 100000
    a4 = 0
    b4 = np.arange(rangen[0], rangen[1],0.01)
    a5 = 0
    b5 = []
    while a5<len(b4):
        b6 = b4[a5]
        if pdf(b6, uniformvalue1)< a3:
            a3 = pdf(b6, uniformvalue1)
        if pdf(b6, uniformvalue1)>a4:
            a4 = pdf(b6, uniformvalue1)
        a5 = a5+1
    b5.append(a3)
    b5.append(a4)
    return b5
a6 = 0
while a6<0.01:
    b7 = fonk1(b1,a6)[0]
    b8 = fonk1(b1,a6)[1]
    a7 = 0
    b9 = []
    while a7<1000:
        a8 = 0
        b10 = []
        while a8<100:
            b11 = np.random.uniform(b1[0],b1[1])
            b12 = np.random.uniform (b7, b8)
            if b12<pdf (b11,a6):
                b10.append(b11)
                a8 = a8+1
            else:
                a8 = a8
        b13 = stats.normaltest(b10)[1]
        b9.append(b13)
        a7 = a7+1
    print a6
    print lessthan(b9,0.05)
    a6 = a6+0.1