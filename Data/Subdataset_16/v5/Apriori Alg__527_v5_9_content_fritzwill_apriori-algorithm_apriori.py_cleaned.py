def fonk1(b12):
    b1 = set()
    for row in b12:
        for item in row:
            b1.add(frozenset([item]))
    return sorted(b1)
def fonk2(b12, b6, b14):
    b2 = defaultdict(int)
    for transaction in b12:
        for candidate in b6:
            if candidate.issubset(transaction):
                b2[candidate] += 1
    b3 = [key for key, count in b2.items() if count >= b14]
    return b3, b2
def fonk3(freq_sets, a1):
    b1 = []
    b4 = len(freq_sets)
    for i in range(b4):
        for j in range(i + 1, b4):
            lst_cands1, b5 = list(freq_sets[i])[:a1-2], list(freq_sets[j])[:a1-2]
            if sorted(lst_cands1) == sorted(b5):
                b1.append(freq_sets[i] | freq_sets[j])
    return b1
def fonk4(b12, b14):
    b6 = fonk1(b12)
    b7 = list(map(set, b12))
    lst_cands, b8 = fonk2(b7, b6, b14)
    b9 = [lst_cands]
    a1 = 2
    while len(b9[a1-2]) > 0:
        b10 = fonk3(b9[a1-2], a1)
        lst_cands_k, b11 = fonk2(b7, b10, b14)
        b8.update(b11)
        b9.append(lst_cands_k)
        a1 += 1
    return b9, b8
def fonk5():
    b12 = []
    b13 = 'Dataset-apriori.txt'
    with open(b13, 'r') as file:
        for line in file:
            b12.append(line.strip().split(','))
    b14 = int(input("What min. support do you want to use? "))
    print(f"\n**** Apriori with b15 = {b14} ****")
    b9, b16 = fonk4(b12, b14)
    print("\nFrequent Itemsets:\n")
    for itemset_level in b9:
        for itemset in itemset_level:
            print(itemset)
    print("\nSupport Counts:\n")
    for itemset, count in b16.items():
        print(itemset, count)
if b17 = = "__main__":
    fonk5()