def fonk1(filename):
    b1 = open(filename)
    b2 = b1.readline()
    b3 = b1.readlines()
    b4 = {}
    b1.close()
    for i in range(len(b3)):
        b3[i] = b3[i].split(',')
    for t in range(len(b3)):
        b4.setdefault(b3[t][0], []).append(b3[t][1])
    b3 = list(b4.values())
    return b3
def fonk2(b3):
    b5 = []
    for c in b3:
        for b18 in c:
            if [b18] not in b5:
                b5.append([b18])
    b5.sort()
    return map(frozenset, b5)
def fonk3(b16, b17, candidates, min_support):
    b6 = {}
    for item in b16:
        for can in candidates:
            if can.issubset(item):
                b6.setdefault(can, 0)
                b6[can] += 1
    b7 = float(b17)
    b5 = []
    b8 = {}
    for key in b6:
        b9 = b6[key] / b7
        if b9 >= min_support:
            b5.insert(0, key)
        b8[key] = b9
    return b5, b8
def fonk4(b5, a1):
    b10 = []
    b11 = len(b5)
    for i in range(b11):
        for j in range(i + 1, b11):
            b12 = list(b5[i])[:a1 - 2]
            b13 = list(b5[j])[:a1 - 2]
            b12.sort()
            b13.sort()
            if b12 = = b13:
                b10.append(b5[i] | b5[j])
    return b10
def fonk5(b3, b14 = 0.05):
    b15 = list(fonk2(fonk1("10000_dataset.txt")))
    b16 = map(set, b3)
    b17 = len(list(map(set, b3)))
    b12, b8 = fonk3(b16, b17, b15, b14)
    b5 = [b12]
    b16 = map(set, b3)
    a1 = 2
    while len(b5[a1 - 2]) > 0:
        b18 = fonk4(b5[a1 - 2], a1)
        b16 = map(set, b3)
        lk, b19 = fonk3(b16, b17, b18, b14)
        b8.update(b19)
        b5.append(lk)
        a1 += 1
    return b5, b8
def fonk6(b5, b8, b20 = 0.9):
    b21 = []
    for i in range(1, len(b5)):
        for freqSet in b5[i]:
            b22 = [frozenset([item]) for item in freqSet]
            if i > 1:
                fonk8(freqSet, b22, b8, b21, b20)
            else:
                fonk7(freqSet, b22, b8, b21, b20)
    return b21
def fonk7(freqSet, b22, b8, b21, b20):
    b23 = []
    for conseq in b22:
        b24 = b8[freqSet] / b8[freqSet - conseq]
        if b24 >= b20:
            b21.append((freqSet - conseq, conseq, b24))
            b23.append(conseq)
    return b23
def fonk8(freqSet, b22, b8, b21, b20):
    b25 = len(b22[0])
    if len(freqSet) > (b25 + 1):
        b26 = fonk4(b22, b25 + 1)
        b26 = fonk7(freqSet, b26, b8, b21, b20)
        if len(b26) > 1:
            fonk8(freqSet, b26, b8, b21, b20)