def fonk1(b14):
    b1 = []
    for transaction in b14:
        for item in transaction:
            if [item] not in b1:
                b1.append([item])
    b1.sort()
    return list(map(frozenset, b1))
def fonk2(b14, b8, b16):
    b2 = {}
    for transaction in b14:
        for candidate in b8:
            if candidate.issubset(transaction):
                if candidate not in b2:
                    b2[candidate] = 1
                else:
                    b2[candidate] += 1
    b3 = float(len(b14))
    b4 = []
    for itemset, count in b2.items():
        if count >= b16:
            b4.append(itemset)
    return b4, b2
def fonk3(b4, a1):
    b1 = []
    b5 = len(b4)
    for i in range(b5):
        for j in range(i + 1, b5):
            b6 = list(b4[i])[:a1 - 2]
            b7 = list(b4[j])[:a1 - 2]
            b6.sort()
            b7.sort()
            if b6 = = b7:
                b1.append(b4[i] | b4[j])
    return b1
def fonk4(b14, b16):
    b8 = fonk1(b14)
    b9 = list(map(set, b14))
    b4, b10 = fonk2(b9, b8, b16)
    b11 = [b4]
    a1 = 2
    while len(b11[a1 - 2]) > 0:
        b8 = fonk3(b11[a1 - 2], a1)
        b4, b12 = fonk2(b9, b8, b16)
        b10.update(b12)
        b11.append(b4)
        a1 += 1
    return b11, b10
if b13 = = "__main__":
    b14 = []
    b15 = 'Dataset-apriori.txt'
    with open(b15, 'r') as file:
        for line in file:
            b14.append(line.strip().split(','))
    b16 = int(input("What min. support do you want to use? "))
    print("\n**** Apriori with b17 = {} ****".format(b16))
    b4, b10 = fonk4(b14, b16)
    print("\nFrequent Itemsets:\n")
    for itemset_level in b4:
        for itemset in itemset_level:
            print(itemset)
    print("\nItemset Counts:\n")
    for itemset, count in b10.items():
        print(itemset, count)