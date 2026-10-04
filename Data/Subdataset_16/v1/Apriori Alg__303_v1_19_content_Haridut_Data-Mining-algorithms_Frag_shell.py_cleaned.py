import sys
import math
import itertools
def fonk1():
    b1 = sys.stdin.readlines()
    b2 = [i.rstrip('\n') for i in b1]
    b3 = int(b2[0])
    b4 = [item.split() for item in b2[1:]]
    return b3, b4
def fonk2(b4):
    b5 = []
    for i in range(len(b4[0])):
        b6 = [b4[j][i] for j in range(len(b4))]
        b5.append(b6)
    b7 = [sorted(list(set(i))) for i in b5]
    return b7
def fonk3(b4, b3):
    b8 = [[] for _ in range(b3)]
    for j in range(len(b4[0])):
        b8[j % b3].append(j)
    b9 = [len(i) for i in b8]
    return b8, b9
def fonk4(b7, b3, b9):
    a1 = 0
    b10 = []
    for i in range(b3):
        b11 = []
        for j in range(b9[i]):
            b11.append(b7[a1])
            a1 += 1
        b10.append(b11)
    return b10
def fonk5(listd, b4):
    a2 = 0
    for p in b4:
        if set(listd) < set(p):
            a2 += 1
    return a2
def fonk6(b10, b4):
    for i in range(len(b10)):
        b12 = []
        for j in range(len(b10[i])):
            for don in itertools.combinations(range(len(b10[i])), j+1):
                b12.append(list(don))
        for k in b12:
            b13 = []
            b14 = []
            for value in k:
                b14 += b10[i][value]
            for h in itertools.combinations(b14, len(k)):
                b13.append(list(h))
            for p in b13:
                b15 = fonk5(p, b4)
                if b15 != 0:
                    print(" ".join(str(x) for x in p) + ': ' + str(b15))
        print()
def fonk7():
    b3, b4 = fonk1()
    b7 = fonk2(b4)
    b8, b9 = fonk3(b4, b3)
    b10 = fonk4(b7, b3, b9)
    fonk6(b10, b4)
if b16 = = "__main__":
    fonk7()