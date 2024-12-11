11. Repository: SabikAbtahee/Apriori-Implementation
   File: AprioriAlgorithm.py
   URL: https:
   Code Content:
import sys
def fonk1():
    sys.b1 = open('apriori.txt','r')
    sys.b2 = open('output.txt','w')
def fonk2(iterable, r):
    b3 = tuple(iterable)
    b4 = len(b3)
    if r > b4:
        return
    b5 = list(range(r))
    yield tuple(b3[b12] for b12 in b5)
    while True:
        for b12 in reversed(range(r)):
            if b5[b12] != b12 + b4 - r:
                break
        else:
            return
        b5[b12] += 1
        for j in range(b12+1, r):
            b5[j] = b5[j-1] + 1
        yield tuple(b3[b12] for b12 in b5)
def fonk3(b12,b9):
    if(b12 in b9):
        return True
    else:
        return False
def fonk4(b19,b18):
    b6 = {}
    b7 = ""
    for b12 in range(1,len(b19)+1):
        b8 = fonk2(b19,b12)
        for c in b8:
            for j in range(0,len(b18),1):
                b9 = b18[j].split()
                for b12 in c:
                  b10 = fonk3(b12,b9)
                  if(b10 = =False):
                      break
                if(b10 = =True):
                    b7 = ""
                    for b12 in c:
                       b7+=b12+","
                    if(b7 in b6):
                        b6[b7]+=1
                    else:
                        b6[b7]=1
    return b6
def fonk5(countsAll,b17):
    b11 = {}
    a1 = 0
    for b12, k in countsAll.b19():
        b12 = str(b12).replace(',',"")
        b11[b12]=k
        if(b11[b12]<b17):
            del(b11[b12])
    for b12, k in b11.b19():
        if(len(b12)>a1):
            a1 = len(b12)
    b13 = a1
    while(a1!=2):
        for b12, k in b11.b19():
            a2 = 0
            b13 = a1-2
            if(len(b12)>a1-2):
                b9 = len(b12)
                while(b9>=a1-2):
                    b14 = b11[b12]/b11[b12[a2:b13]]
                    print(b12[a2:b13],"=>",b12,b14)
                    a2+=a1-2
                    b13+=a1-2
                    b9-=a1-2
        a1-=2
def fonk6():
    b15 = sys.b1.readlines()
    b16 = int(b15[0])
    b17 = int(b15[len(b15)-1])
    b18 = []
    b19 = []
    for b12 in range(1,b16+1,1):
            b18.append(b15[b12])
    for b12 in range(1,b16+1,1):
        for line in b15[b12].split():
            if(line not in b19):
                b19.append(line)
        b19.sort()
    b10 = fonk4(b19,b18)
    fonk5(b10,b17)
def fonk7():
    fonk1()
    fonk6()
if b20 = = "__main__":
    fonk7()
   README Content:
Apriori algorithm implemented in python. Doesn't work for cases where percentage are formed in a combinatoric way .
The input file contains the test Case
The a2 line is the number of b18
The b13 line is the minimun support in int form
The output file will have the outputs
Only run AprioriMain.py
