
def fonk1(b6, subsets1, b8, length, temp, base):
    if length < 1:
        if temp not in subsets1:
            temp.sort()
            b6.sort()
            subsets1.append(temp)
            b8.append(b6)
    else:
        for i in range(base, len(b6)):
            b1 = temp + [b6[i]]
            b2 = b6[:i] + b6[i+1:]
            fonk1(b2, subsets1, b8, length - 1, b1, i)
def fonk2(frequent_itemsets, total_transactions, min_confidence, min_lift):
    b3 = []
    b4 = {}
    for itemset in frequent_itemsets:
        b5 = itemset[:-1]
        b5.sort()
        b4[tuple(b5)] = itemset[-1]
    for itemset in frequent_itemsets:
        b6 = itemset[:-1]
        b7 = itemset[-1]
        subsets1, b8 = [], []
        for length in range(1, len(b6)):
            fonk1(b6, subsets1, b8, length, [], 0)
        for subset1, subset2 in zip(subsets1, b8):
            subset1.sort()
            subset2.sort()
            if tuple(subset1) in b4 and tuple(subset2) in b4:
                b9 = b4[tuple(subset1)]
                b10 = b4[tuple(subset2)]
                b11 = b7 * total_transactions / (b9 * b10)
                if b11 >= min_lift:
                    b12 = b7 / b9
                    if b12 >= min_confidence:
                        b3.append([subset1, subset2, b7, b12, b11])
                    b13 = b7 / b10
                    if b13 >= min_confidence:
                        b3.append([subset2, subset1, b7, b13, b11])
    return b3