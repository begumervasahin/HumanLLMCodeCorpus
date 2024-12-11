import itertools
import csv
class class1:
    a1 = 30
    a2 = 70
def fonk1(filename, b1 = 100):
    with open(filename, 'r') as f:
        b2 = list(csv.reader(f, delimiter=','))
    b3 = []
    for row in b2:
        b4 = [val.strip() for val in row[1:] if int(val.strip()) <= b1]
        if b4:
            b3.append(b4)
    return b3
def fonk2(S, b16):
    return set(itertools.combinations(S, b16))
def fonk3(dataset, b10, a4):
    b5 = fonk2(dataset, a4)
    for item in b5:
        b6 = sorted(item)
        if b6 not in b10:
            return True
    return False
def fonk4(b10, a4):
    b7 = []
    b8 = a4
    for list1 in b10:
        for list2 in b10:
            a3 = 0
            b9 = []
            if list1 != list2:
                while a3 < b8 - 1:
                    if list1[a3] != list2[a3]:
                        break
                    a3 += 1
                else:
                    if list1[b8 - 1] < list2[b8 - 1]:
                        b9.extend(list1)
                        b9.append(list2[b8 - 1])
                        if not fonk3(b9, b10, a4):
                            b7.append(b9)
    return b7
def fonk5(b2, singles, support):
    a4 = 2
    b10 = singles
    b11 = []
    while b10:
        b12 = []
        for b9 in fonk4(b10, a4 - 1):
            b13 = sum(1 for T in b2 if set(b9).issubset(set(T)))
            if (100 * b13 / len(b2)) >= support:
                b9.sort()
                b12.append(b9)
        b10 = b12
        a4 += 1
        if b12:
            b11.append(b12)
    return b11
def fonk6(b2, singles, support, confidence):
    a5 = 1
    b11 = fonk5(b2, singles, support)
    b7 = 0
    for itemsets in b11:
        for itemset in itemsets:
            for a3 in range(1, len(itemset)):
                b5 = fonk2(itemset, a3)
                for item in b5:
                    b14 = sum(1 for T in b2 if set(item).issubset(set(T)))
                    b15 = sum(1 for T in b2 if set(itemset).issubset(set(T)))
                    if 100 * b15 / b14 >= confidence:
                        b6 = ','.join(item)
                        b16 = ','.join(set(itemset) - set(item))
                        print(f"{b6} ==> {b16}")
                        b7 += 1
    print('Total rules generated:', b7)
    return b7
def fonk7():
    b2 = fonk1('1000-out1.csv')
    fonk6(b2, class1.a1, class1.a2)
if b17 = = "__main__":
    fonk7()