import itertools
def fonk1(S):
    b1 = len(S) - 1
    return [list(subset) for subset in itertools.combinations(S, b1)]
def fonk2(b2, subsets):
    b2 = [set(item[0]) for item in b2]
    for subset in subsets:
        if not any(set(subset) < target_set for target_set in b2):
            return 0
    return 1
def fonk3(b12, a2, b6):
    b3 = {}
    for items in b12.values():
        for item in items:
            b3[item] = b3.get(item, 0) + 1
    b4 = len(b12)
    b3 = {item: freq / b4 for item, freq in b3.items() if freq / b4 >= a2}
    b5 = [[item, b10] for item, b10 in b3.items()]
    if b6 = = 1:
        return b5
    a1 = 2
    while a1 <= b6:
        b7 = []
        for i in range(len(b5)):
            for j in range(i + 1, len(b5)):
                if a1 = = 2:
                    b8 = [b5[i][0], b5[j][0]]
                else:
                    b8 = list(set(b5[i][0]) | set(b5[j][0]))
                if len(b8) != a1:
                    continue
                b8.sort()
                if fonk2(b5, fonk1(b8)) and b8 not in b7:
                    b7.append(b8)
        b9 = []
        for b8 in b7:
            b10 = sum(1 for items in b12.values() if set(b8) <= set(items)) / b4
            if b10 >= a2:
                b9.append([b8, b10])
        b5 = b9
        a1 += 1
    return b5
if b11 = = "__main__":
    b12 = {
        0: ['A', 'B', 'C'],
        1: ['A', 'C'],
        2: ['A', 'D'],
        3: ['B', 'C'],
        4: ['A', 'B', 'C', 'D']
    }
    a2 = 0.5
    b6 = 3
    b5 = fonk3(b12, a2, b6)
    print("Frequent Itemsets:")
    for itemset in b5:
        print(f"Itemset: {itemset[0]}, Support: {itemset[1]:.2f}")