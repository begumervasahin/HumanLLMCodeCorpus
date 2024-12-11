import itertools
import csv
import parameters
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
        if b4:
            b3.append(b4)
    return b3
def fonk2(S, b17):
    return set(itertools.combinations(S, b17))
def fonk3(dataset, b11, a2):
    b6 = fonk2(dataset, a2)
    for item in b6:
        b7 = sorted(item)
        if b7 not in b11:
            return True
    return False
def fonk4(b11, a2):
    b8 = []
    b9 = a2
    for list1 in b11:
        for list2 in b11:
            a1 = 0
            b10 = []
            if list1 != list2:
                while a1 < b9 - 1:
                    if list1[a1] != list2[a1]:
                        break
                    else:
                        a1 += 1
                else:
                    if list1[b9 - 1] < list2[b9 - 1]:
                        b10.extend(list1)
                        b10.append(list2[b9 - 1])
                        if not fonk3(b10, b11, a2):
                            b8.append(b10)
    return b8
def fonk5(b2, singles, b18):
    a2 = 2
    b11 = singles
    b12 = []
    while b11:
        b13 = []
        for b10 in fonk4(b11, a2 - 1):
            b14 = sum(1 for T in b2 if set(b10).issubset(set(T)))
            if (100 * b14 / len(b2)) >= b18:
                b10.sort()
                b13.append(b10)
        b11 = b13
        a2 += 1
        if b13:
            b12.append(b13)
    return b12
def fonk6(b2, singles, b18, b19):
    a3 = 1
    b12 = fonk5(b2, singles, b18)
    b8 = 0
    for itemsets in b12:
        for itemset in itemsets:
            for a1 in range(1, len(itemset)):
                b6 = fonk2(itemset, a1)
                for item in b6:
                    b15 = sum(1 for T in b2 if set(item).issubset(set(T)))
                    b16 = sum(1 for T in b2 if set(itemset).issubset(set(T)))
                    if 100 * b16 / b15 >= b19:
                        b7 = ','.join(item)
                        b17 = ','.join(set(itemset) - set(item))
                        print(f"{b7} ==> {b17}")
                        b8 += 1
    print('Total rules generated:', b8)
    return b8
def fonk7():
    b2 = fonk1('1000-out1.csv')
    b18 = parameters.SUPPORT
    b19 = parameters.CONFIDENCE
    solve(b2, b18, b19)
if b20 = = "__main__":
    fonk7()