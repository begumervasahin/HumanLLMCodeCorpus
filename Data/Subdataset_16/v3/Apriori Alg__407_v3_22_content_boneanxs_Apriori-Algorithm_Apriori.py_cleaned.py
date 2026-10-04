import itertools
def fonk1(S):
    b1 = len(S) - 1
    return [list(subset) for subset in itertools.combinations(S, b1)]
def fonk2(b2, subsets):
    b2 = [set(item[0]) for item in b2]
    for subset in subsets:
        if not any(set(subset).issubset(target_set) for target_set in b2):
            return 0
    return 1
def fonk3(b13):
    b3 = {}
    for items in b13.values():
        for item in items:
            b3[item] = b3.get(item, 0) + 1
    return b3
def fonk4(b3, b9, a1):
    return {item: freq / b9 for item, freq in b3.items() if freq / b9 >= a1}
def fonk5(b10, b5):
    b4 = []
    for i in range(len(b10)):
        for j in range(i + 1, len(b10)):
            if b5 = = 2:
                b6 = [b10[i][0], b10[j][0]]
            else:
                b6 = list(set(b10[i][0]) | set(b10[j][0]))
            if len(b6) != b5:
                continue
            b6.sort()
            if fonk2(b10, fonk1(b6)) and b6 not in b4:
                b4.append(b6)
    return b4
def fonk6(b4, b13, b9, a1):
    b7 = []
    for b6 in b4:
        b8 = sum(1 for items in b13.values() if set(b6).issubset(set(items))) / b9
        if b8 >= a1:
            b7.append([b6, b8])
    return b7
def fonk7(b13, a1, b11):
    b9 = len(b13)
    b3 = fonk3(b13)
    b3 = fonk4(b3, b9, a1)
    b10 = [[item, b8] for item, b8 in b3.items()]
    if b11 = = 1:
        return b10
    b5 = 2
    while b5 <= b11:
        b4 = fonk5(b10, b5)
        b10 = fonk6(b4, b13, b9, a1)
        b5 += 1
    return b10
if b12 = = "__main__":
    b13 = {
        0: ['A', 'B', 'C'],
        1: ['A', 'C'],
        2: ['A', 'D'],
        3: ['B', 'C'],
        4: ['A', 'B', 'C', 'D']
    }
    a1 = 0.5
    b11 = 3
    b10 = fonk7(b13, a1, b11)
    print("Frequent Itemsets:")
    for itemset in b10:
        print(f"Itemset: {itemset[0]}, Support: {itemset[1]:.2f}")