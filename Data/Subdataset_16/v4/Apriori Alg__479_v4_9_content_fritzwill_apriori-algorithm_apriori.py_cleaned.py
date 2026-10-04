def fonk1(b14):
    b1 = []
    for row in b14:
        for item in row:
            if [item] not in b1:
                b1.append([item])
    b1.sort()
    return list(map(frozenset, b1))
def fonk2(b14, b8, b16):
    b2 = {}
    for cur_set in b14:
        for candidate in b8:
            if candidate.issubset(cur_set):
                if candidate not in b2:
                    b2[candidate] = 1
                else:
                    b2[candidate] += 1
    b3 = float(len(b14))
    b4 = []
    for key, count in b2.items():
        if count >= b16:
            b4.insert(0, key)
    return b4, b2
def fonk3(freq_sets, a1):
    b4 = []
    b5 = len(freq_sets)
    for i in range(b5):
        for j in range(i + 1, b5):
            b6 = list(freq_sets[i])[:a1-2]
            b7 = list(freq_sets[j])[:a1-2]
            b6.sort()
            b7.sort()
            if b6 = = b7:
                b4.append(freq_sets[i] | freq_sets[j])
    return b4
def fonk4(b14, b16):
    b8 = fonk1(b14)
    b9 = list(map(set, b14))
    b11, b10 = fonk2(b9, b8, b16)
    b11 = [b11]
    a1 = 2
    while len(b11[a1-2]) > 0:
        b12 = fonk3(b11[a1-2], a1)
        lst_cands_x, b13 = fonk2(b9, b12, b16)
        b10.update(b13)
        b11.append(b12)
        a1 += 1
    return b11, b10
def fonk5():
    b14 = []
    b15 = 'Dataset-apriori.txt'
    with open(b15, 'r') as file:
        for line in file:
            b14.append(line.strip().split(','))
    b16 = int(input("What min. support do you want to use? "))
    print(f"\b3**** Apriori with b17 = {b16} ****")
    sets, b18 = fonk4(b14, b16)
    print("\nSets:\b3")
    for item_set in sets:
        for item in item_set:
            print(item)
    print("\nCounts:\b3")
    for item_set, count in b18.items():
        print(item_set, count)
if b19 = = "__main__":
    fonk5()