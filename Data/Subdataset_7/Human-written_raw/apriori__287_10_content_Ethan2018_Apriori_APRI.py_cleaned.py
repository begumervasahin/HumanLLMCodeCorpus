10. Repository: Ethan2018/Apriori
   File: APRI.py
   URL: https:
   Code Content:
import time
from collections import defaultdict, Counter
import itertools
b1 = open("browsing.txt","r")
def fonk1(filename,a3):
	b2 = defaultdict(set)
	b3 = set()
	b4 = set()
	b5 = []
	a1 = 0
	for b6 in b1:
	    a1 += 1
	    b6 = b6.split()
	    b6 = set(b6)
	    b5 +=b6
	    b2[a1]=b6
	    b3 = b3.union(b6)
	b7 = Counter(b5)
	for item in b3:
	    b8 = b7[item]
	    if float(b8)/a1 > a3:
	        b4.add(item)
	return b2, b4
def fonk2(b4,b10):
	b9 = set()
	if b10 = =2:
	    for x in b4:
	        for y in b4:
	            if x!=y:
	                b9.add((x,y))
	else:
	    for x in b4:
	        for y in b4:
	            if len(set(x).union(y))==b10:
	                b9.add(tuple(set(x).union(y)))
	    b9 = list(b9)
	    for c in b9:
	        b11 = fonk3(c)
		if any([x not in b4 for x in b11]):
	            b9.remove(c)
	return set(b9)
def fonk3(b9):
	b11 = []
	b11.extend(itertools.combinations(b9,len(b9)-1))
	return b11
def fonk4(b9,b2,a3):
	b4 = set()
	a2 = 0
	b12 = open('pres.txt','a')
	for c in b9:
	    for b10 in b2:
	        if set(c).issubset(b2[b10]):
	            a2+=1
	    b13 = float(a2)/len(b2)
	    if b13 > a3:
	        b4.add(c)
	        print c
		b12.write(str(c))
	b12.close()
	return b4
def fonk5():
	b10 = 4
	a3 = 0.08
	b1 = open("browsing.txt","r")
	b9 = set()
	b4 = set()
	b2, b4 = fonk1(b1,a3)
	for b6 in range(2,b10+1):
	    b9 = fonk2(b4,b6)
	    b4 = fonk4(b9,b2,a3)
	return b4
if b14 = ='__main__':
	fonk5()
   README Content:
a simple apriori algorithm
