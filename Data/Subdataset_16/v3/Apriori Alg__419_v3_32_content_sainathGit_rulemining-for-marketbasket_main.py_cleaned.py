import sys
def fonk1(input_file):
    b1 = []
    with open(input_file, "r") as file:
        for line in file:
            b1.append([int(x) for x in line.split()])
    return b1
def fonk2(min_support, total_transactions):
    return min_support * total_transactions
def fonk3(itemset_counts, min_support):
    b2 = [a1 for a1 in itemset_counts.keys() if itemset_counts[a1] < min_support]
    for b3 in b2:
        del itemset_counts[b3]
def fonk4(itemset1, itemset2):
    b3 = list(itemset1[:-1])
    b3.extend([itemset1[-1], itemset2[-1]])
    return tuple(b3)
def fonk5(itemset1, itemset2):
    return itemset1[:-1] == itemset2[:-1] and itemset1[-1] < itemset2[-1]
def fonk6(current_itemsets):
    b4 = {}
    for itemset1 in current_itemsets.keys():
        for itemset2 in current_itemsets.keys():
            if fonk5(itemset1, itemset2):
                b4[fonk4(itemset1, itemset2)] = 0
    return b4
def fonk7(itemsets, b1):
    for itemset in itemsets.keys():
        for transaction in b1:
            if set(itemset).issubset(transaction):
                itemsets[itemset] += 1
def fonk8(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in fonk8(seq[1:]):
            yield [seq[0]] + item
            yield item
def fonk9(antecedent, consequent, b7):
    print(f"{antecedent} ==> {consequent}    Confidence: {b7:.2f}")
def fonk10(itemset, b12):
    global a2
    for b5 in fonk8(list(itemset)):
        if not b5 or b5 = = list(itemset):
            continue
        b6 = [x for x in itemset if x not in b5]
        b7 = b12[itemset] / b12[tuple(b5)]
        if b7 >= b10:
            fonk9(b5, b6, b7)
            a2 += 1
if b8 = = "__main__":
    b9 = float(sys.argv[1])
    b10 = float(sys.argv[2])
    b11 = sys.argv[3]
    b1 = fonk1(b11)
    b9 = fonk2(b9, len(b1))
    b12 = {}
    for transaction in b1:
        for item in transaction:
            if (item,) not in b12:
                b12[(item,)] = 1
            else:
                b12[(item,)] += 1
    fonk3(b12, b9)
    b13 = [b12]
    a1 = 1
    while len(b13[a1-1]) != 0:
        b12 = fonk6(b13[a1-1])
        fonk7(b12, b1)
        fonk3(b12, b9)
        b13.append(b12)
        a1 += 1
    b13.pop()
    b14 = {}
    for level in b13:
        b14.update(level)
    a2 = 0
    for itemset in b14.keys():
        if len(itemset) > 1:
            fonk10(itemset, b14)
    print(f"Mined file {b11}")
    print(f"Found a total of {a2} association rules")