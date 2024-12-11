8. Repository: omjego/AR-Mining-Hash-Tree
   File: naive_apriori.py
   URL: https:
   Code Content:
import itertools
import csv
import parameters
def fonk1(filename, b1 = 100):
    with open(filename, 'b19') as f:
        b2 = b10(csv.reader(f, delimiter=','))
    b3 = []
    for i in xrange(len(b2)):
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
    b7 = []
    b8 = {}
    for row in b2:
        for word in row:
            if word not in b8.keys():
                b8[word] = 1
            else:
                b8[word] += 1
    b9 = []
    for key in b8:
        if (100 * b8[key] / b6) >= float(support):
            b9.append([key])
    return fonk6(b9, support, confidence)
def fonk3(S, b20):
    return set(itertools.combinations(S, b20))
def fonk4(dataset, b12, a1):
    b10 = fonk3(dataset, a1)
    for item in b10:
        b11 = []
        for l in item:
            b11.append(l)
        b11.sort()
        if b11 not in b12:
            return True
    return False
def fonk5(singles, support):
    a1 = 2
    b12 = []
    b13 = []
    for item in singles:
        b12.append(item)
    while b12:
        b14 = []
        b15 = fonk7(b12, a1 - 1)
        for b23 in b15:
            a2 = 0
            b16 = len(b2)
            b11 = set(b23)
            for b7 in b2:
                b17 = set(b7)
                if b11.issubset(b17):
                    a2 += 1
            if (100 * a2 / b16) >= float(support):
                b23.sort()
                b14.append(b23)
        b12 = []
        for l in b14:
            b12.append(l)
        a1 += 1
        if b14:
            b13.append(b14)
    return b13
def fonk6(singles, support, confidence):
    a3 = 1
    b13 = fonk5(singles, support)
    b3 = 0
    for b10 in b13:
        for l in b10:
            b18 = len(l)
            a4 = 1
            while a4 < b18:
                b19 = fonk3(l, a4)
                a4 += 1
                for item in b19:
                    a5 = 0
                    a6 = 0
                    b11 = []
                    b20 = []
                    for i in item:
                        b11.append(i)
                    for b7 in b2:
                        if set(b11).issubset(set(b7)):
                            a5 += 1
                        if set(l).issubset(set(b7)):
                            a6 += 1
                    if 100 * a6 / a5 >= float(confidence):
                        for index in l:
                            if index not in b11:
                                b20.append(index)
                        b21 = ','.join(b11)
                        b22 = ','.join(set(l) - set(b11))
                        print (' ==> '.join([b21, b22]))
                        b3 += 1
                        a3 += 1
    print('Total rules generated:', b3)
    return b3
def fonk7(b12, a1):
    b18 = a1
    b3 = []
    for list1 in b12:
        for list2 in b12:
            a4 = 0
            b23 = []
            if list1 != list2:
                while a4 < b18 - 1:
                    if list1[a4] != list2[a4]:
                        break
                    else:
                        a4 += 1
                else:
                    if list1[b18 - 1] < list2[b18 - 1]:
                        for item in list1:
                            b23.append(item)
                        b23.append(list2[b18 - 1])
                        if not fonk4(b23, b12, a1):
                            b3.append(b23)
    return b3
b2 = fonk1('1000-out1.csv')
fonk2(b2, parameters.SUPPORT, parameters.CONFIDENCE)
   README Content:
Python implementation of Association rule mining with Apriori Algorithm.  Used hash trees to optimize Apriori'b11 performance. Tested against
BAKERY dataset.
