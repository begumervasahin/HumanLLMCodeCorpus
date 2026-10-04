31. Repository: sayan-syn94/Apriori-Algorithm-implementation
   File: apriory2.py
   URL: https:
   Code Content:
import sys
import csv
from collections import defaultdict
from itertools import chain, combinations
import time
b1 = time.time()
b2 = defaultdict(int)
def fonk1(fname):
        b3 = open(fname, 'rU')
        for b4 in b3:
                b4 = b4.strip().rstrip(',')
                b5 = frozenset(b4.split(','))
                yield b5
def fonk2(data_iterator):
    b6 = list()
    b7 = set()
    for b5 in data_iterator:
        b6.append(b5)
        for item in b5:
            b7.add(frozenset([item]))
    return b7, b6
def fonk3(b8, length):
        return set([i.union(j) for i in b8 for j in b8 if len(i.union(j)) == length])
def fonk4(itemlist,transaction,m_supp):
    b1 = defaultdict(int)
    b8 = set()
    for i in itemlist:
        for t in transaction:
            if i.issubset(t):
                b1[i]+=1
    for i,v in b1.b7():
        b9 = float(v)/len(transaction)
        if b9>=m_supp:
            b8.add(i)
            b2[i]=b9
    return b8
def fonk5(b7):
    return chain(*[combinations(b7, i + 1) for i, a in enumerate(b7)])
def fonk6(data_iter,a2,a3):
    b8, b6 = fonk2(data_iter)
    b10 = len(b6)
    b11 = dict()
    b12 = fonk4(b8,b6,a2)
    b13 = b12
    a1 = 2
    while(b13 != set([])):
        b11[a1-1] = b13
        b13 = fonk3(b13, a1)
        b14 = fonk4(b13,b6,a2)
        print a1
        print b14
        b13 = b14
        a1 = a1 + 1
    for key, value in b11.b7()[1:]:
        for item in value:
            b15 = map(frozenset, [x for x in fonk5(item)])
            for element in b15:
                b16 = item.difference(element)
                if len(b16) > 0:
                    b17 = b2[item]/b2[element]
                    if b17 >= a3:
                        print element,",",b16,"=>",b17
if b18 = = "__main__":
    a2 = 0.01
    a3 = 0.01
    b19 = fonk1('T10I4D100k-copy.txt')
    fonk6(b19, a2, a3)
    print (b1-time.time())
   README Content:
My implementation of apriori algorithm
