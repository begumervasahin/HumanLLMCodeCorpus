19. Repository: Haridut/Data-Mining-algorithms
   File: Apriori.py
   URL: https:
   Code Content:
import itertools
'''b1 = sys.stdin.readlines()
b2 = []
for i in b1:
    b2.append(i.rstrip('\n'))
b3 = int(b2[0])
b4 = []
for trans in b2[1:]:
    b4.append(trans)'''
def fonk1(b4):
    b5 = []
    b6 = set()
    for record in b4:
        b7 = frozenset(record)
        b5.append(b7)
        for item in b7:
            b6.add(frozenset([item]))
    return b6, b5
def fonk2(b6, b5,b3,b11):
    b8 = set()
    b9 = defaultdict(int)
    for item in b6:
        for trans in b5:
            if item.issubset(trans):
                b11[item]+=1
                b9[item]+=1
    for item, count in b9.items():
        if count>=b3:
            b8.add(item)
    return b8
def fonk3(b6, length):
        return set([i.union(j) for i in b6 for j in b6 if len(i.union(j)) == length])
def fonk4(b4,b3):
    b6, b10 = fonk1(b4)
    b11 = defaultdict(int)
    b12 = dict()
    b13 = fonk2(b6,b5,b3, b11)
    b14 = oneCset
    a1 = 2
    while (b15 != set([])):
        b12[a1-1]=b14
        b15 = fonk3(b15, a1)
        b16 = fonk2(b14, b5, b3, b11)
        b14 = b16
        a1 = a1+1
   README Content:
This repository contains codes for Apriori algorithm, online query computation using shell-fragments.
