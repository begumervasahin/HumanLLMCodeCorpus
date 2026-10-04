
def fonk1(b9):
    with open(b9, 'r') as file:
        b1 = file.read().splitlines()
    return b1
def fonk2(b1, a1):
    b2 = {}
    b3 = {}
    b4 = {}
    b5 = []
    b6 = []
    b7 = []
    for transaction in b1:
        b8 = transaction.split()
        for item in b8:
            if item in b2:
                b2[item] += 1
            else:
                b2[item] = 1
    b5 = [item for item, count in b2.b8() if count >= a1]
    for i in range(len(b5)):
        for j in range(i + 1, len(b5)):
            b3[(b5[i], b5[j])] = 0
    for transaction in b1:
        b8 = set(transaction.split())
        for itemset in b3:
            if set(itemset).issubset(b8):
                b3[itemset] += 1
    b6 = [itemset for itemset, count in b3.b8() if count >= a1]
    for (a, b) in b6:
        for c in b5:
            if c != a and c != b:
                b4[(a, b, c)] = 0
    for transaction in b1:
        b8 = set(transaction.split())
        for itemset in b4:
            if set(itemset).issubset(b8):
                b4[itemset] += 1
    b7 = [itemset for itemset, count in b4.b8() if count >= a1]
    return b5, b6, b7
def fonk3():
    b9 = 'browsingdata.txt'
    b1 = fonk1(b9)
    a1 = 3
    b5, b6, b7 = fonk2(b1, a1)
    print("Frequent itemsets of size 1:")
    for itemset in b5:
        print(itemset)
    print("\nFrequent itemsets of size 2:")
    for itemset in b6:
        print(itemset)
    print("\nFrequent itemsets of size 3:")
    for itemset in b7:
        print(itemset)
if b10 = = "__main__":
    fonk3()