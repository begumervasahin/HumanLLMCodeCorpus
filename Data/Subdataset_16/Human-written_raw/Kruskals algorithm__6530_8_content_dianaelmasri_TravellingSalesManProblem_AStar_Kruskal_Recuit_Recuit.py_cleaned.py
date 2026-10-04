from Graph import Graph
import random as rd
import numpy.matlib as m
import time
def fonk1(b9,b7):
    a1 = 0
    for b5 in range (len(b9)-1):
        a1 += b7.costs[b9[b5],b9[b5+1]]
    return a1
def fonk2(sol1,b1,b7):
    return fonk1(sol1,b7) - fonk1(b1,b7)
def fonk3(b9,b7,temp):
    b1 = fonk4(b9)
    b2 = fonk2(b1,b9,b7)
    if b2<0:
        return b1
    else:
        b3 = rd.random()
        if b3 < m.exp(-b2/temp):
            return b1
        else:
            return b9
def fonk4(b9):
    b1 = b9.copy()
    b4 = list(range(1,len(b9)-2))
    b5 = rd.choice(b4)
    b4.remove(b5)
    b6 = rd.choice(b4)
    b1[b5],b1[b6]=b1[b6],b1[b5]
    return b1
def fonk5():
    a2 = 17
    b7 = Graph("N17.data")
    a3 = 0
    a4 = 0
    for k in range(10):
        b8 = [b5 for b5 in range(1,a2)]
        rd.shuffle(b8)
        b9 = [0]+b8+[0]
        a5 = 1000
        b10 = time.time()
        while a5 > 5:
            for b5 in range(a2**2):
                b9 = fonk3(b9,b7,a5)
            a5*=0.98
        b11 = time.time()-b10
        print(b9)
        a3+=fonk1(b9,b7)
        a4+= b11
    print(a3/10)
    print(a4/10)
if b12 = = '__main__':
    fonk5()