from collections import defaultdict
def fonk1(b14):
    b1 = set()
    for row in b14:
        for item in row:
            b1.add(frozenset([item]))
    return sorted(b1)
def fonk2(b14, b7, min_support):
    b2 = defaultdict(int)
    for cur_set in b14:
        for candidate in b7:
            if candidate.issubset(cur_set):
                b2[candidate] += 1
    b3 = [key for key, support in b2.items() if support >= min_support]
    return b3, b2
def fonk3(freq_sets, a1):
    b3 = []
    b4 = len(freq_sets)
    for i in range(b4):
        for j in range(i + 1, b4):
            b5 = list(freq_sets[i])[:a1 - 2]
            b6 = list(freq_sets[j])[:a1 - 2]
            if b5 = = b6:
                b3.append(freq_sets[i] | freq_sets[j])
    return b3
def fonk4(b14, min_support):
    b7 = fonk1(b14)
    b8 = [set(row) for row in b14]
    b10, b9 = fonk2(b8, b7, min_support)
    b10 = [b10]
    a1 = 2
    while len(b10[a1 - 2]) > 0:
        b11 = fonk3(b10[a1 - 2], a1)
        list_candidates_x, b12 = fonk2(b8, b11, min_support)
        b9.update(b12)
        b10.append(b11)
        a1 += 1
    return b10, b9
if b13 = = "__main__":
    b14 = []
    b15 = 'Dataset-apriori.txt'
    with open(b15, 'r') as file:
        for line in file:
            b14.append(line.strip().split(','))
    print("What min. support do you want to use? ")
    b16 = int(input())
    print("\n**** Apriori with b17 = {} ****".format(b16))
    sets, b18 = fonk4(b14, b16)
    print("\nSets:\n")
    for item_set in sets:
        for item in item_set:
            print(item)
    print("\nCounts:\n")
    for item_set, support in b18.items():
        print(item_set, support)