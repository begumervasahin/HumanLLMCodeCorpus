def fonk1(b16):
    b1 = []
    for row in b16:
        for item in row:
            if [item] not in b1:
                b1.append([item])
    b1.sort()
    return list(map(frozenset, b1))
def fonk2(b16, b9, min_support):
    b2 = {}
    for cur_set in b16:
        for candidate in b9:
            if candidate.issubset(cur_set):
                if candidate not in b2:
                    b2[candidate] = 1
                else:
                    b2[candidate] += 1
    b3 = float(len(b16))
    b4 = []
    for key in b2:
        b5 = b2[key]
        if b5 >= min_support:
            b4.insert(0, key)
    return b4, b2
def fonk3(freq_sets, a1):
    b4 = []
    b6 = len(freq_sets)
    for i in range(b6):
        for j in range(i + 1, b6):
            b7 = list(freq_sets[i])[:a1 - 2]
            b8 = list(freq_sets[j])[:a1 - 2]
            b7.sort()
            b8.sort()
            if b7 = = b8:
                b4.append(freq_sets[i] | freq_sets[j])
    return b4
def fonk4(b16, min_support):
    b9 = fonk1(b16)
    b10 = list(map(set, b16))
    b12, b11 = fonk2(b10, b9, min_support)
    b12 = [b12]
    a1 = 2
    while len(b12[a1 - 2]) > 0:
        b13 = fonk3(b12[a1 - 2], a1)
        list_candidates_x, b14 = fonk2(b10, b13, min_support)
        b11.update(b14)
        b12.append(b13)
        a1 += 1
    return b12, b11
if b15 = = "__main__":
    b16 = []
    b17 = 'Dataset-apriori.txt'
    with open(b17, 'r') as file:
        for line in file:
            b16.append(line.strip().split(','))
    print("What min. b5 do you want to use? ")
    b18 = int(input())
    print("\b3**** Apriori with b19 = {} ****".format(b18))
    sets, b20 = fonk4(b16, b18)
    print("\nSets:\b3")
    for x in sets:
        for y in x:
            print(y)
    print("\nCounts:\b3")
    for a1, v in b20.items():
        print(a1, v)