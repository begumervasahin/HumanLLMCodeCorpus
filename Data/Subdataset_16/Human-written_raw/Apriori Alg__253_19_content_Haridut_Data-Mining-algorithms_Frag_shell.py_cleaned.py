19. Repository: Haridut/Data-Mining-algorithms
   File: Frag_shell.py
   URL: https:
   Code Content:
import sys
import math
import itertools
b1 = []
for i in range(0, len(item_list[0])):
    b2 = []
    for j in range(0,len(item_list)):
        b2.append(item_list[j][i])
    b1.append(b2)
b3 = []
for i in b1:
    b3.append(sorted(list(set(i))))
b4 = []
for i in range(0,partitions):
    b4.append([])
for j in range(0,len(item_list[0])):
    b4[j%partitions].append(j)
b5 = []
for i in b4:
    b5.append(len(i))
a1 = 0
b6 = []
for i in range(0,partitions):
    b7 = []
    for j in range(0,b5[i]):
        b7.append(b3[a1])
        a1 = a1+1
    b6.append(b7)
def listcount (listd):
    a2 = 0
    for p in item_list:
        if set(listd)<set(p):
            a2 = a2+1
    return a2
for i in range(len(b6)):
    b8 = []
    for j in range(len(b6[i])):
        for don in (list(itertools.combinations(range(len(b6[i])),j+1))):
            b8.append(list(don))
    for k in b8:
        b9 = []
        b10 = []
        for value in k:
            b10 = b10+b6[i][value]
        for h in (list(itertools.combinations(b10,len(k)))):
            b9.append(list(h))
        for p in b9:
            b11 = listcount(p)
            if b11 is not 0:
                for d in range(len(p)):
                    print (str(p[d])+' ',b12 = '')
                print(': '+ str(b11))
    print()
   README Content:
This repository contains codes for Apriori algorithm, online query computation using shell-fragments.
