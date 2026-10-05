
from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
def fonk1(sic,c):
    a1 = 0
    for i in sic:
        a1+=c[i]
    return a1/len(sic)
b1 = list(open(sys.argv[1],'r'))
b2 = int(sys.argv[2])
b3 = int(b1[0])
b4 = int(b1[1])
b5 = np.zeros((b3,b4))
b6 = [];b=[];c=[]
for i in xrange(3,len(b1)):
    b7 = b1[i].strip("\n").split(" ")
    b6.append(int(b7[0])-1);b.append(int(b7[1])-1);c.append(int(b7[2]))
b8 = dict(Counter(b))
for i in range(len(b)):
    c[i]=c[i]*(math.log(float(b3+1)/(b8[b[i]]+1),2))
b9 = csc_matrix((c,(b6,b)),shape=(b3,b4))
b10 = np.asarray(np.sqrt(b9.power(2).sum(axis=1)))
b5 = csc_matrix(b9/b10)
print(b5[24])
b11 = {}
for i in range(b5.shape[0]):
    b11[i]=b5[i]
b12 = []
for i in b11:
    for j in b11:
        if(i<j):
            b13 = b11[i].multiply(b11[j])
            b14 = (np.sqrt(b11[i].power(2).sum()))*(np.sqrt(b11[j].power(2).sum()))
            b13 = (b13.sum())/b14
            hp.heappush(b12,(1-b13,i,j))
b15 = {}
a2 = 0
while a2<b3-b2:
    b16 = hp.heappop(b12)
    if (b15.has_key(b16[1]) or b15.has_key(b16[2])):
        continue
    elif(type(b16[1])==int and type(b16[2])==int):
        b15[b16[1]]=None
        b15[b16[2]]=None
        b17 = (b16[1],b16[2])
        b18 = fonk1(b17,b5)
        del b11[b16[1]]
        del b11[b16[2]]
    else:
        b15[b16[1]]=None
        b15[b16[2]]=None
        if(type(b16[1])==int):
            b17 = b16[2]+(b16[1],)
        elif(type(b16[2])==int):
            b17 = b16[1]+(b16[2],)
        else:
            b17 = b16[1]+b16[2]
        del b11[b16[1]]
        del b11[b16[2]]
        b18 = fonk1(b17,b5)
    for i in b11:
        if not b15.has_key(i):
            b13 = b18.multiply(b11[i])
            b14 = (np.sqrt(b11[i].power(2).sum()))*(np.sqrt(b18.power(2).sum()))
            b13 = (b13.sum())/b14
            hp.heappush(b12,(1-b13,b17,i))
    b11[b17]=b18
    a2+=1
for i in b11:
    if type(i)==int:
        print i+1
    else:
        b19 = ''
        for j in sorted(i):
            b19+=str(j+1)+','
        print b19[:-1]