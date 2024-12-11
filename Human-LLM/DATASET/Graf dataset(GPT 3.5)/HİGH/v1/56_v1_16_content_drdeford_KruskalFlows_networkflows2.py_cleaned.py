import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
import itertools
import time
from operator import itemgetter
def fonk1(b22):
    a1 = 0
    a2 = 0
    fonk2(b22)
    ktime,b1 = fonk3(b22)
    b16,b2 = fonk4(b22,a2)
    b19,b3 = fonk5(b22,a2)
    print ('Kruskal Time:',ktime,'\nKruskal Cost:', b1,'\nPrim Time:',b16,'\nPrim Cost:', b2,'\nSollin Time:',b19,'\nSollin Cost:', b3)
    plt.show()
def fonk2(b22):
    b4 = len(b22)
    b5 = []
    b6 = []
    b7 = 2*math.pi/b4
    plt.figure(1)
    plt.title('Original Graph')
    for i in range(b4):
        b5.append(b4*math.cos(i*b7))
        b6.append(b4*math.sin(i*b7))
        plt.text(b5[i],b6[i],i+1,b8 = 15,color='green')
    for i in range(b4):
        for j in range(i,b4):
            if b22[i][j] != 0:
                plt.plot([b5[i],b5[j]],[b6[i],b6[j]],'b-',b9 = 3)
                plt.text((b5[i]+b5[j])/2,(b6[i]+b6[j])/2,b22[i][j],b8 = 15,color='red')
    plt.scatter(b5,b6,b10 = 50)
def fonk3(b22):
    b11 = time.time()
    b12 = []
    b13 = []
    b14 = []
    b15 = []
    for i in range(len(b22)):
        b15.append([i])
    for i in range(len(b22)):
        for j in range(i,len(b22)):
            b12.append([i,j,b22[i][j]])
    b12 = sorted(b12,key=itemgetter(-1))
    for k in b12:
        if k[2] != 0:
            b13.append(k)
    for l in b13:
        b14.append(l)
        a1 = 0
        for m in b15:
            if l[0] in m and l[1] in m:
                a1 = a1 +1
        if a1 != 0:
            b14.pop()
        if a1 = =0:
            a3 = 0
            a4 = 0
            for n in range(len(b15)):
                if l[0] in b15[n]:
                    a3 = n
                if l[1] in b15[n]:
                    a4 = n
            b15[a3]=list(set(b15[a3]+b15[a4]))
            b15.pop(a4)
    b5 = []
    b6 = []
    a5 = 0
    b7 = 2*math.pi/len(b22)
    plt.figure(2)
    plt.title('Kruskal Tree')
    for i in range(len(b22)):
        b5.append(math.cos(i*b7))
        b6.append(math.sin(i*b7))
        plt.text(b5[i],b6[i],i+1,b8 = 15,color='green')
    for k in b14:
        plt.plot([b5[k[0]],b5[k[1]]],[b6[k[0]],b6[k[1]]],'c-',b9 = 3)
        plt.text((b5[k[0]]+b5[k[1]])/2,(b6[k[0]]+b6[k[1]])/2,k[2],b8 = 15,color='red')
        a5 = a5 + k[2]
    plt.scatter(b5,b6,b10 = 50)
    b10 = time.time()-b11
    return b10, a5
def fonk4(b22,a2):
    b16 = time.time()
    b12 = []
    a2 = 0
    b13 = []
    b17 = [0]
    b14 = []
    for i in range(len(b22)):
        for j in range(i,len(b22)):
            b12.append([i,j,b22[i][j]])
    for k in b12:
        if k[2] != 0:
            b13.append(k)
    for m in range(len(b22)-1):
        b18 = []
        for n in b13:
            if (n[0] in b17 and n[1] not in b17) or (n[1] in b17 and n[0] not in b17):
                b18.append(n)
        b18 = sorted(b18,key=itemgetter(-1))
        b14.append(b18[0])
        b17.append(b18[0][0])
        b17.append(b18[0][1])
        b17 = list(set(b17))
    b5 = []
    b6 = []
    b2 = 0
    b7 = 2*math.pi/len(b22)
    plt.figure(3)
    plt.title('Prim Tree')
    for i in range(len(b22)):
        b5.append(math.cos(i*b7))
        b6.append(math.sin(i*b7))
        plt.text(b5[i],b6[i],i+1,b8 = 15,color='green')
    for k in b14:
        plt.plot([b5[k[0]],b5[k[1]]],[b6[k[0]],b6[k[1]]],'c-',b9 = 3)
        plt.text((b5[k[0]]+b5[k[1]])/2,(b6[k[0]]+b6[k[1]])/2,k[2],b8 = 15,color='red')
        b2 = b2 + k[2]
    plt.scatter(b5,b6,b10 = 50)
    b16 = time.time()-b16
    return b16,b2
def fonk5(b22,a2):
    b19 = time.time()
    b12 = []
    b13 = []
    b17 = [0]
    b14 = []
    b15 = []
    for i in range(len(b22)):
        b15.append([i])
    for i in range(len(b22)):
        for j in range(i,len(b22)):
            b12.append([i,j,b22[i][j]])
    for k in b12:
        if k[2] != 0:
            b13.append(k)
    b18 = []
    while (len(b14)<len(b22)-1):
        b20 = b15[:]
        for l in range(len(b20)):
            for n in b13:
                if (n[0] in b20[l] and n[1] not in b20[l]) or (n[1] in b20[l] and n[0] not in b20[l]):
                    b18.append(n)
            b18 = sorted(b18,key=itemgetter(-1))
            if b18[0] not in b14:
                b14.append(b18[0])
                a3 = 'b22'
                a4 = 'b22'
                for m in range(len(b15)):
                    if b18[0][0] in b15[m]:
                        a3 = m
                    if b18[0][1] in b15[m]:
                        a4 = m
                b15[a3]=list(set(b15[a3]+b15[a4]))
                b15.pop(a4)
            b18 = []
    b5 = []
    b6 = []
    b3 = 0
    b7 = 2*math.pi/len(b22)
    plt.figure(4)
    plt.title('Sollin Tree')
    for i in range(len(b22)):
        b5.append(math.cos(i*b7))
        b6.append(math.sin(i*b7))
        plt.text(b5[i],b6[i],i+1,b8 = 15,color='green')
    for k in b14:
        plt.plot([b5[k[0]],b5[k[1]]],[b6[k[0]],b6[k[1]]],'c-',b9 = 3)
        plt.text((b5[k[0]]+b5[k[1]])/2,(b6[k[0]]+b6[k[1]])/2,k[2],b8 = 15,color='red')
        b3 = b3 + k[2]
    plt.scatter(b5,b6,b10 = 50)
    b19 = time.time()-b19
    return b19,b3
def fonk6(n,b22):
    b21 = []
    a1 = 0
    for i in range(n):
        b21.append([])
    for i in range(n):
        for j in range(n):
            b21[i].append(0)
    for k in b22:
        b21[k[0]][k[1]]=k[2]
        b21[k[1]][k[0]]=k[2]
    for i in b21[0]:
        a1 = a1 + i
    if a1 = = 0:
        b21.pop(0)
        for i in range(len(b21)):
            b21[i].pop(0)
    return b21
b22 = [[0, 1, 3, 4, 0], [1, 0, 0, 2, 0], [3, 0, 0, 0, 5], [4, 2, 0, 0, 0], [0, 0, 5, 0, 0]]
fonk1(b22)