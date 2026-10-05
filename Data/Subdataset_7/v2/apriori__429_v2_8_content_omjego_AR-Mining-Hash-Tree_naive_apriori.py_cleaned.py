import itertools
import csv
class class1:
    a1 = 30
    a2 = 70
def fonk1(filename, b1 = 100):
    with open(filename, 'r') as f:
        b2 = list(csv.reader(f, delimiter=','))
    b3 = []
    for i in range(len(b2)):
        b4 = []
        for b5 in b2[i][1:]:
            b5 = b5.strip()
            if int(b5) <= b1:
                b4.append(b5)
        if len(b4) > 0:
            b3.append(b4)
    return b3
def fonk2(S, b16):
    return set(itertools.combinations(S, b16))
def fonk3(dataset, b10, a4):
    b6 = fonk2(dataset, a4)
    for item in b6:
        b7 = []
        for l in item:
            b7.append(l)
        b7.sort()
        if b7 not in b10:
            return True
    return False
def fonk4(b10, a4):
    b8 = a4
    b3 = []
    for list1 in b10:
        for list2 in b10:
            a3 = 0
            b9 = []
            if list1 != list2:
                while a3 < b8 - 1:
                    if list1[a3] != list2[a3]:
                        break
                    else:
                        a3 += 1
                else:
                    if list1[b8 - 1] < list2[b8 - 1]:
                        for item in list1:
                            b9.append(item)
                        b9.append(list2[b8 - 1])
                        if not fonk3(b9, b10, a4):
                            b3.append(b9)
    return b3
def fonk5(b2, singles, support):
    a4 = 2
    b10 = []
    b11 = []
    for item in singles:
        b10.append(item)
    while b10:
        b12 = []
        b13 = fonk4(b10, a4 - 1)
        for b9 in b13:
            a5 = 0
            b14 = len(b2)
            b7 = set(b9)
            for T in b2:
                b15 = set(T)
                if b7.issubset(b15):
                    a5 += 1
            if (100 * a5 / b14) >= support:
                b9.sort()
                b12.append(b9)
        b10 = []
        for l in b12:
            b10.append(l)
        a4 += 1
        if b12:
            b11.append(b12)
    return b11
def fonk6(b2, singles, support, confidence):
    a6 = 1
    b11 = fonk5(b2, singles, support)
    b3 = 0
    for itemsets in b11:
        for itemset in itemsets:
            b8 = len(itemset)
            a3 = 1
            while a3 < b8:
                b6 = fonk2(itemset, a3)
                a3 += 1
                for item in b6:
                    a7 = 0
                    a8 = 0
                    b7 = []
                    b16 = []
                    for i in item:
                        b7.append(i)
                    for T in b2:
                        if set(b7).issubset(set(T)):
                            a7 += 1
                        if set(itemset).issubset(set(T)):
                            a8 += 1
                    if 100 * a8 / a7 >= confidence:
                        for index in itemset:
                            if index not in b7:
                                b16.append(index)
                        b17 = ','.join(b7)
                        b18 = ','.join(set(itemset) - set(b7))
                        print(' ==> '.join([b17, b18]))
                        b3 += 1
                        a6 += 1
    print('Total rules generated:', b3)
    return b3
def fonk7():
    b2 = fonk1('1000-out1.csv')
    solve(b2, class1.a1, class1.a2)
if b19 = = "__main__":
    fonk7()