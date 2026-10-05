def fonk1(freq_itemset):
    b1 = []
    b2 = list(freq_itemset.keys())
    for i in range(len(freq_itemset) - 1):
        for j in range(i + 1, len(freq_itemset)):
            b3 = [b2[i], b2[j]]
            b1.append(b3)
    return b1
def fonk2(freq_itemset, a1):
    b1 = fonk1(freq_itemset)
    b4 = [comb.split(',') for comb in [','.join(comb) for comb in b1]]
    b5 = []
    b6 = []
    for candidate in b4:
        b7 = set(candidate)
        b8 = list(b7)
        b5.append(b8)
        if len(b8) == a1:
            b6.append(b8)
    return b6
def fonk3(candidates, data):
    b9 = []
    b10 = [set(candidate) for candidate in candidates]
    b11 = [set(data_row) for data_row in data]
    for candidate_set in b10:
        b12 = sum(1 for data_set in b11 if candidate_set.issubset(data_set))
        b9.append(b12)
    return b9
def fonk4(candidate_set, support, b20):
    b13 = {}
    for i in range(len(candidate_set)):
        b14 = candidate_set[i]
        b15 = ','.join(b14)
        if support[i] >= b20:
            b13[b15] = support[i]
    return b13
def fonk5(frequent_itemset, b17, b28):
    if len(frequent_itemset) == b28:
        if b17.a1(frequent_itemset) == 0:
            b17.append(frequent_itemset)
        return b17
    elif len(frequent_itemset) != b28:
        for i in range(len(frequent_itemset)):
            b16 = frequent_itemset[i + 1:] + frequent_itemset[:i]
            b17 = fonk5(b16, b17, b28)
        return b17
def fonk6():
    b18 = []
    print("Select the b18:")
    print("1. Grocery")
    print("2. Clothing")
    print("3. Electronics")
    print("4. Utensils")
    print("5. Furniture")
    b19 = input("Enter the b18 number: ")
    b20 = int(input('Enter minimum Support: '))
    b21 = int(input('Enter minimum Confidence: '))
    b22 = f"db{b19}.txt"
    with open(b22, 'r') as fp:
        b18 = [line.strip().split(", ") for line in fp]
    b23 = {}
    for data_row in b18:
        for item in data_row:
            b23[item] = b23.get(item, 0) + 1
    b24 = {item: a1 for item, a1 in b23.b2() if a1 >= b20}
    a1 = 2
    b25 = fonk2(b24, a1)
    b26 = fonk3(b25, b18)
    b27 = fonk4(b25, b26, b20)
    b28 = a1 - 1
    while b28 != 0:
        for frequent_itemset in b27:
            b17 = []
            b29 = fonk5(frequent_itemset.split(','), b17, b28)
            for association in b29:
                b30 = [item for item in frequent_itemset.split(',') if item not in association]
                print(f"{b30} ---------> {association}")
        b28 -= 1
if b31 = = "__main__":
    fonk6()