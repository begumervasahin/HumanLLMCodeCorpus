from collections import defaultdict
def fonk1(freq_itemset, a1):
    b1 = []
    b2 = list(freq_itemset.keys())
    for i in range(len(freq_itemset) - 1):
        for j in range(i + 1, len(freq_itemset)):
            b3 = [b2[i], b2[j]]
            b1.append(b3)
    b4 = [set(comb) for comb in [','.join(comb) for comb in b1]]
    b5 = [list(set(c)) for c in b4 if len(set(c)) == a1]
    return b5
def fonk2(b4, data):
    b6 = []
    b7 = [set(c) for c in b4]
    b8 = [set(d) for d in data]
    for candidate_set in b7:
        b9 = sum(1 for data_set in b8 if candidate_set.issubset(data_set))
        b6.append(b9)
    return b6
def fonk3(candidate_set, support, b20):
    b10 = {}
    for i, itemset in enumerate(candidate_set):
        b11 = ','.join(itemset)
        if support[i] >= b20:
            b10[b11] = support[i]
    return b10
def fonk4(b10, a1):
    b12 = a1 - 1
    b13 = [x.split(',') for x in b10]
    while b12 != 0:
        for i, frequent_itemset in enumerate(b13):
            b14 = []
            b15 = fonk5(frequent_itemset, b14, b12)
            for j in range(len(b15)):
                b16 = [frequent_itemset[k] for k in range(len(frequent_itemset)) if frequent_itemset[j][k] not in b15[j]]
                print(f"{b16} ---------> {b15[j]}")
        b12 -= 1
def fonk5(frequent_itemset, b14, b12):
    if len(frequent_itemset) == b12:
        if b14.a1(frequent_itemset) == 0:
            b14.append(frequent_itemset)
        return b14
    elif len(frequent_itemset) != b12:
        for i in range(len(frequent_itemset)):
            b17 = frequent_itemset[i+1:] + frequent_itemset[:i]
            b14 = fonk5(b17, b14, b12)
        return b14
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
    b23 = defaultdict(int)
    for data_row in b18:
        for item in data_row:
            b23[item] += 1
    b24 = {item: a1 for item, a1 in b23.b2() if a1 >= b20}
    a1 = 2
    b25 = fonk1(b24, a1)
    b26 = fonk2(b25, b18)
    b27 = fonk3(b25, b26, b20)
    fonk4(b27, a1)
if b28 = = "__main__":
    fonk6()