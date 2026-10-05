def fonk1(filename):
    with open(filename, 'r') as file:
        b1 = file.readlines()
        b2 = {}
        for line in b1:
            b3 = line.strip().split(',')
            b2.setdefault(b3[0], []).append(b3[1])
    return list(b2.values())
def fonk2(dataset):
    b4 = []
    for transaction in dataset:
        for item in transaction:
            if [item] not in b4:
                b4.append([item])
    b4.sort()
    return map(frozenset, b4)
def fonk3(dataset, b14, b13):
    b5 = {}
    b6 = len(dataset)
    for transaction in dataset:
        for candidate in b14:
            if candidate.issubset(transaction):
                b5[candidate] = b5.get(candidate, 0) + 1
    b4 = []
    b7 = {}
    for itemset, count in b5.items():
        b8 = count / b6
        if b8 >= b13:
            b4.insert(0, itemset)
        b7[itemset] = b8
    return b4, b7
def fonk4(b4, a1):
    b9 = []
    b10 = len(b4)
    for i in range(b10):
        for j in range(i + 1, b10):
            b11 = list(b4[i])[:a1 - 2]
            b12 = list(b4[j])[:a1 - 2]
            b11.sort()
            b12.sort()
            if b11 = = b12:
                b9.append(b4[i] | b4[j])
    return b9
def fonk5(dataset, b13 = 0.05):
    b14 = list(fonk2(dataset))
    b4 = [b14]
    b7 = {}
    a1 = 2
    while len(b4[a1 - 2]) > 0:
        b14 = fonk4(b4[a1 - 2], a1)
        freq, b8 = fonk3(dataset, b14, b13)
        b7.update(b8)
        b4.append(freq)
        a1 += 1
    return b4, b7
def fonk6(b4, b7, b15 = 0.9):
    b16 = []
    for i in range(1, len(b4)):
        for freq_set in b4[i]:
            b17 = [frozenset([item]) for item in freq_set]
            if i > 1:
                pass
            else:
                pass
    return b16