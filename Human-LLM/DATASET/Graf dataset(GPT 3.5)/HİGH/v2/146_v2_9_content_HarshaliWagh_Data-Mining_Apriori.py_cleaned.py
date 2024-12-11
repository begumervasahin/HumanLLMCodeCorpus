from collections import defaultdict
def fonk1(freq_itemset, a1):
    b1 = []
    b2 = list(freq_itemset.keys())
    for i in range(len(freq_itemset) - 1):
        for j in range(i + 1, len(freq_itemset)):
            b3 = [b2[i], b2[j]]
            b1.append(b3)
    b4 = [comb.split(',') for comb in [','.join(comb) for comb in b1]]
    b5 = []
    b6 = []
    for i in range(len(b4)):
        b7 = set(b4[i])
        b8 = list(b7)
        b5.append(b8)
        if len(b5[i]) == a1:
            b6.append(b5[i])
    return b6
def fonk2(b4, data):
    b9 = []
    b10 = [set(b4[p]) for p in range(len(b4))]
    b11 = [set(data[q]) for q in range(len(data))]
    for i in range(len(b4)):
        b12 = sum(1 for j in range(len(data)) if b10[i].issubset(b11[j]))
        b9.append(b12)
    return b9
def fonk3(candidate_set, support, b24):
    b13 = {}
    for i in range(len(candidate_set)):
        b14 = candidate_set[i]
        b15 = ','.join(b14)
        if support[i] >= b24:
            b13[b15] = support[i]
    return b13
def fonk4(b13, a1):
    b16 = a1 - 1
    b17 = [x.split(',') for x in b13]
    while b16 != 0:
        for i in range(len(b17)):
            b18 = []
            b19 = fonk5(b17[i], b18, b16)
            for j in range(len(b19)):
                b20 = [b17[i][k] for k in range(len(b17[i])) if b17[j][k] not in b19[j]]
                print(str(b20) + "--------->" + str(b19[j]))
        b16 = b16 - 1
def fonk5(frequent_itemset, b18, b16):
    if len(frequent_itemset) == b16:
        if b18.a1(frequent_itemset) == 0:
            b18.append(frequent_itemset)
        return b18
    elif len(frequent_itemset) != b16:
        for i in range(len(frequent_itemset)):
            b21 = frequent_itemset[i+1:] + frequent_itemset[:i]
            b18 = fonk5(b21, b18, b16)
        return b18
def fonk6():
    b22 = []
    print("Select the b22:")
    print("1. Grocery")
    print("2. Clothing")
    print("3. Electronics")
    print("4. Utensils")
    print("5. Furniture")
    b23 = input("Enter the b22 number: ")
    b24 = int(input('Enter minimum Support: '))
    b25 = int(input('Enter minimum Confidence: '))
    b26 = ""
    if b23 = = '1':
        b26 = "db1.txt"
    elif b23 = = '2':
        b26 = "db2.txt"
    elif b23 = = '3':
        b26 = "db3.txt"
    elif b23 = = '4':
        b26 = "db4.txt"
    else:
        b26 = "db5.txt"
    with open(b26, 'r') as fp:
        b22 = [line.strip().split(", ") for line in fp]
    b27 = defaultdict(int)
    for data_row in b22:
        for item in data_row:
            b27[item] += 1
    b28 = {item: a1 for item, a1 in b27.b2() if a1 >= b24}
    a1 = 2
    b29 = fonk1(b28, a1)
    b30 = fonk2(b29, b22)
    b31 = fonk3(b29, b30, b24)
    fonk4(b31, a1)
if b32 = = "__main__":
    fonk6()