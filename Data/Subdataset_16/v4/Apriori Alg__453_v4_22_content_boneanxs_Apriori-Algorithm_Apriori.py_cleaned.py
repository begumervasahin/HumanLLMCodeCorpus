import itertools
def fonk1(S):
    b1 = len(S) - 1
    return [list(i) for i in itertools.combinations(S, b1)]
def fonk2(tar, subsets):
    b2 = [set(subset) for subset in subsets]
    for transaction in tar:
        b3 = set(transaction)
        if all(subset <= b3 for subset in b2):
            return 1
    return 0
def fonk3(transactions, threshold, b8):
    b4 = {}
    for items in transactions.values():
        for item in items:
            if item in b4:
                b4[item] += 1
            else:
                b4[item] = 1
    b5 = len(transactions)
    b6 = {item: b12 / b5 for item, b12 in b4.items() if b12 / b5 >= threshold}
    b7 = [[item, b12] for item, b12 in b6.items()]
    if b8 = = 1:
        return b7
    a1 = 2
    while a1 <= b8:
        b9 = []
        for i in range(len(b7)):
            for j in range(i + 1, len(b7)):
                b10 = list(set(b7[i][0]) | set(b7[j][0]))
                if len(b10) != a1:
                    continue
                b10.sort()
                if fonk2(b7, fonk1(b10)):
                    if b10 not in b9:
                        b9.append(b10)
        b7 = []
        for b10 in b9:
            b11 = sum(1 for items in transactions.values() if set(b10) <= set(items))
            b12 = b11 / b5
            if b12 >= threshold:
                b7.append([b10, b12])
        a1 += 1
    return b7
