32. Repository: sainathGit/rulemining-for-marketbasket
   File: main.py
   URL: https:
   Code Content:
import sys
b1 = float(sys.argv[2])
b2 = float(sys.argv[4])
b3 = [];
b4 = open(sys.argv[5], "r")
for line in b4:
    b3.append([int(x) for x in line.split()])
b1 = b1*len(b3)
def fonk1(b14):
    b5 = []
    for a1 in b14.keys():
        if b14[a1] < b1:
            b5.append(a1)
    for i in b5:
        del b14[i]
def fonk2(l1, l2):
    b6 = []
    b7 = len(l1) - 1;
    for i in range(b7):
        b6.append(l1[i])
    b6.append(l1[b7])
    b6.append(l2[b7])
    return tuple(b6)
def fonk3(l1, l2):
    b7 = len(l1) - 1
    for i in range(b7):
        if l1[i] != l2[i]:
            return False
    if l1[b7] >= l2[b7]:
        return False
    return True
def fonk4(b14):
    b8 = {}
    for l1 in b14.keys():
        for l2 in b14.keys():
            if fonk3(l1,l2):
                b8[fonk2(l1,l2)] = 0;
    return b8
def fonk5(b14):
    for a1 in b14.keys():
        for t in b3:
            if set(a1).issubset(set(t)):
                b14[a1] += 1
def fonk6(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in fonk6(seq[1:]):
            yield [seq[0]]+item
            yield item
def fonk7(b10, b11, b12):
        print(b10,b9 = " ==> ")
        print(b11, b9 = "              " )
        print(b12)
def fonk8(item, b15):
    global a2
    for b10 in fonk6(list(item)):
        if b10 = = [] or b10 == list(item):
            continue
        b11 = [x for x in item if x not in b10]
        b12 = b15[item]/b15[tuple(b10)]
        if  b12 > b2:
            fonk7(b10,b11,b12)
            a2 += 1
b13 = []
b14 = {}
for t in b3:
    for x in t:
        if (x,) not in b14.keys():
            b14[(x,)] = 1
        else:
            b14[(x,)] += 1
fonk1(b14)
b13.append(b14)
a1 = 1
while (len(b13[a1-1]) != 0) :
    b14 = fonk4(b13[a1-1])
    fonk5(b14)
    fonk1(b14)
    b13.append(b14)
    a1 += 1
b13.pop()
b15 = {}
for a1 in range(len(b13)):
    b15.update(b13[a1])
a2 = 0
for item in b15.keys():
    if len(item) > 1:
         fonk8(item,b15)
print("mined file ", sys.argv[5])
print("and found a total of ",a2,"  association rules")
   README Content:
it uses apriori algorithm to mine the rules form transaction database
