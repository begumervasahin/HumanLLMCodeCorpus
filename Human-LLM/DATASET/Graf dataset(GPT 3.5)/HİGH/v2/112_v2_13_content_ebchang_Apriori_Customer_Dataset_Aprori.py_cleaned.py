from collections import defaultdict
def fonk1(filename):
    with open(filename, 'r') as file:
        b1 = file.readlines()
        b2 = [line.strip().split(',') for line in b1]
    return b2
def fonk2(b2):
    b3 = []
    for transaction in b2:
        for item in transaction:
            if [item] not in b3:
                b3.append([item])
    return list(map(frozenset, b3))
def fonk3(b2, b3, b13):
    b4 = defaultdict(int)
    b5 = len(b2)
    for transaction in b2:
        for candidate in b3:
            if candidate.issubset(transaction):
                b4[candidate] += 1
    b6 = []
    b7 = {}
    for itemset, count in b4.items():
        b8 = count / b5
        if b8 >= b13:
            b6.append(itemset)
        b7[itemset] = b8
    return b6, b7
def fonk4(b6, a1):
    b9 = []
    b10 = len(b6)
    for i in range(b10):
        for j in range(i + 1, b10):
            b11 = list(b6[i])[:a1 - 2]
            b12 = list(b6[j])[:a1 - 2]
            b11.sort()
            b12.sort()
            if b11 = = b12:
                b9.append(b6[i] | b6[j])
    return b9
def fonk5(b2, b13 = 0.05):
    b3 = fonk2(b2)
    b6 = [b3]
    b7 = {}
    a1 = 2
    while len(b6[a1 - 2]) > 0:
        b3 = fonk4(b6[a1 - 2], a1)
        frequent_sets, b8 = fonk3(b2, b3, b13)
        b7.update(b8)
        b6.append(frequent_sets)
        a1 += 1
    return b6, b7
def fonk6(b6, b7, b14 = 0.9):
    b15 = []
    for i in range(1, len(b6)):
        for frequent_set in b6[i]:
            b16 = [frozenset([item]) for item in frequent_set]
            if i > 1:
                pass
            else:
                pass
    return b15
b2 = fonk1("10000_dataset.txt")
b6, b7 = fonk5(b2, 0.5)
b15 = fonk6(b6, b7)