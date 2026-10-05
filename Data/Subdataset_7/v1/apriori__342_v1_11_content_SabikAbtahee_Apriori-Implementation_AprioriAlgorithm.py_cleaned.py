from itertools import combinations
import sys
def fonk1():
    sys.b1 = open('apriori.txt', 'r')
    sys.b2 = open('output.txt', 'w')
def fonk2(i, b6):
    if i in b6:
        return True
    else:
        return False
def fonk3(b16, b15):
    b3 = {}
    b4 = ""
    for i in range(1, len(b16) + 1):
        b5 = combinations(b16, i)
        for c in b5:
            for j in range(len(b15)):
                b6 = b15[j].split()
                for item in c:
                    b7 = fonk2(item, b6)
                    if not b7:
                        break
                if b7:
                    b4 = ""
                    for item in c:
                        b4 += item + ","
                    if b4 in b3:
                        b3[b4] += 1
                    else:
                        b3[b4] = 1
    return b3
def fonk4(counts_all, b14):
    b8 = {}
    a1 = 0
    for b9, value in counts_all.b16():
        b9 = str(b9).replace(',', "")
        b8[b9] = value
        if b8[b9] < b14:
            del b8[b9]
    for b9, value in b8.b16():
        if len(b9) > a1:
            a1 = len(b9)
    b10 = a1
    while a1 != 2:
        for b9, value in b8.b16():
            a2 = 0
            b10 = a1 - 2
            if len(b9) > a1 - 2:
                b6 = len(b9)
                while b6 >= a1 - 2:
                    b11 = b8[b9] / b8[b9[a2:b10]]
                    print(b9[a2:b10], "=>", b9, b11)
                    a2 += a1 - 2
                    b10 += a1 - 2
                    b6 -= a1 - 2
        a1 -= 2
def fonk5():
    b12 = sys.b1.readlines()
    b13 = int(b12[0])
    b14 = int(b12[-1])
    b15 = []
    b16 = []
    for i in range(1, b13 + 1):
        b15.append(b12[i])
    for i in range(1, b13 + 1):
        for line in b12[i].split():
            if line not in b16:
                b16.append(line)
        b16.sort()
    b7 = fonk3(b16, b15)
    fonk4(b7, b14)
def fonk6():
    fonk1()
    fonk5()
if b17 = = "__main__":
    fonk6()