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
def fonk2(b2, support, confidence):
    b6 = len(b2)
    b7 = {}
    for row in b2:
        for word in row:
            if word not in b7:
                b7[word] = 1
            else:
                b7[word] += 1
    b8 = []
    for key in b7:
        if (100 * b7[key] / b6) >= support:
            b8.append([key])
    return fonk7(b2, b8, support, confidence)
def fonk3(S, b19):
    return set(itertools.combinations(S, b19))
def fonk4(dataset, b13, a4):
    b9 = fonk3(dataset, a4)
    for item in b9:
        b10 = []
        for l in item:
            b10.append(l)
        b10.sort()
        if b10 not in b13:
            return True
    return False
def fonk5(b13, a4):
    b11 = a4
    b3 = []
    for list1 in b13:
        for list2 in b13:
            a3 = 0
            b12 = []
            if list1 != list2:
                while a3 < b11 - 1:
                    if list1[a3] != list2[a3]:
                        break
                    else:
                        a3 += 1
                else:
                    if list1[b11 - 1] < list2[b11 - 1]:
                        for item in list1:
                            b12.append(item)
                        b12.append(list2[b11 - 1])
                        if not fonk4(b12, b13, a4):
                            b3.append(b12)
    return b3
def fonk6(b2, singles, support):
    a4 = 2
    b13 = []
    b14 = []
    for item in singles:
        b13.append(item)
    while b13:
        b15 = []
        b16 = fonk5(b13, a4 - 1)
        for b12 in b16:
            a5 = 0
            b17 = len(b2)
            b10 = set(b12)
            for T in b2:
                b18 = set(T)
                if b10.issubset(b18):
                    a5 += 1
            if (100 * a5 / b17) >= support:
                b12.sort()
                b15.append(b12)
        b13 = []
        for l in b15:
            b13.append(l)
        a4 += 1
        if b15:
            b14.append(b15)
    return b14
def fonk7(b2, singles, support, confidence):
    a6 = 1
    b14 = fonk6(b2, singles, support)
    b3 = 0
    for itemsets in b14:
        for itemset in itemsets:
            b11 = len(itemset)
            a3 = 1
            while a3 < b11:
                b9 = fonk3(itemset, a3)
                a3 += 1
                for item in b9:
                    a7 = 0
                    a8 = 0
                    b10 = []
                    b19 = []
                    for i in item:
                        b10.append(i)
                    for T in b2:
                        if set(b10).issubset(set(T)):
                            a7 += 1
                        if set(itemset).issubset(set(T)):
                            a8 += 1
                    if 100 * a8 / a7 >= confidence:
                        for index in itemset:
                            if index not in b10:
                                b19.append(index)
                        b20 = ','.join(b10)
                        b21 = ','.join(set(itemset) - set(b10))
                        print(' ==> '.join([b20, b21]))
                        b3 += 1
                        a6 += 1
    print('Total rules generated:', b3)
    return b3
def fonk8():
    b2 = fonk1('1000-out1.csv')
    fonk2(b2, class1.a1, class1.a2)
if b22 = = "__main__":
    fonk8()