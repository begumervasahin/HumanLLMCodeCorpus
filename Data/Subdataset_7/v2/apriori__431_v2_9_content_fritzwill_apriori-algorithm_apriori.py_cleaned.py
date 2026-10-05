def fonk1(b15):
    b1 = []
    for row in b15:
        for item in row:
            if [item] not in b1:
                b1.append([item])
    b1.sort()
    return list(map(frozenset, b1))
def fonk2(b15, b8, min_support):
    b2 = {}
    for cur_set in b15:
        for candidate in b8:
            if candidate.issubset(cur_set):
                b2[candidate] = b2.get(candidate, 0) + 1
    b3 = float(len(b15))
    b4 = [key for key, support in b2.items() if support >= min_support]
    return b4, b2
def fonk3(freq_sets, a1):
    b4 = []
    b5 = len(freq_sets)
    for i in range(b5):
        for j in range(i + 1, b5):
            b6 = list(freq_sets[i])[:a1 - 2]
            b7 = list(freq_sets[j])[:a1 - 2]
            b6.sort()
            b7.sort()
            if b6 = = b7:
                b4.append(freq_sets[i] | freq_sets[j])
    return b4
def fonk4(b15, min_support):
    b8 = fonk1(b15)
    b9 = list(map(set, b15))
    b11, b10 = fonk2(b9, b8, min_support)
    b11 = [b11]
    a1 = 2
    while len(b11[a1 - 2]) > 0:
        b12 = fonk3(b11[a1 - 2], a1)
        list_candidates_x, b13 = fonk2(b9, b12, min_support)
        b10.update(b13)
        b11.append(b12)
        a1 += 1
    return b11, b10
if b14 = = "__main__":
    b15 = []
    b16 = 'Dataset-apriori.txt'
    with open(b16, 'r') as file:
        for line in file:
            b15.append(line.strip().split(','))
    print("What min. support do you want to use? ")
    b17 = int(input())
    print("\b3**** Apriori with b18 = {} ****".format(b17))
    sets, b19 = fonk4(b15, b17)
    print("\nSets:\b3")
    for x in sets:
        for y in x:
            print(y)
    print("\nCounts:\b3")
    for a1, v in b19.items():
        print(a1, v)