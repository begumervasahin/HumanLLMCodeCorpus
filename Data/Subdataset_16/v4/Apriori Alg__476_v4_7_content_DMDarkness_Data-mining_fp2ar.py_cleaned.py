
def fonk1(b5, subsets1, b7, length, temp, base):
    if length < 1:
        if temp not in subsets1:
            temp.sort()
            b5.sort()
            subsets1.append(temp)
            b7.append(b5)
    else:
        for i in range(base, len(b5)):
            fonk1(b5[:i] + b5[i+1:], subsets1, b7, length-1, temp + [b5[i]], i)
def fonk2(frequent_itemsets, total_transactions, min_confidence, min_lift):
    b1 = []
    b2 = {}
    for itemset in frequent_itemsets:
        b3 = itemset[:-1]
        b3.sort()
        b2[tuple(b3)] = itemset[-1]
    for itemset in frequent_itemsets:
        b4 = (len(itemset) - 1)
        b5 = itemset[:-1]
        b6 = itemset[-1]
        subsets1, b7 = [], []
        for j in range(1, b4 + 1):
            fonk1(b5, subsets1, b7, j, [], 0)
        for j in range(len(subsets1)):
            if subsets1.count(b7[j]) != 0:
                subsets1[j] = [-1, -9]
                b7[j] = [-2, -5]
            b8 = subsets1[j]
            b9 = b7[j]
            b8.sort()
            b9.sort()
            if tuple(b8) in b2 and tuple(b9) in b2:
                b10 = b2[tuple(b8)]
                b11 = b2[tuple(b9)]
                b12 = b6 * total_transactions / (b10 * b11)
                if b12 > min_lift:
                    b13 = b6 / b10
                    if b13 > min_confidence:
                        b14 = [b8, b9, b6, b13, b12]
                        b1.append(b14)
                    b15 = b6 / b11
                    if b15 > min_confidence:
                        b14 = [b9, b8, b6, b15, b12]
                        b1.append(b14)
    return b1