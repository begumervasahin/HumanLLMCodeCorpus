import itertools
def fonk1(S):
    b1 = len(S) - 1
    return [list(i) for i in itertools.combinations(S, b1)]
def fonk2(tar, L):
    b2 = [set(i[0]) for i in tar]
    for i in L:
        for j in b2:
            if j < set(i):
                return 0
    return 1
def fonk3(tar, thr, b7):
    b3 = {}
    for key in tar.b6():
        b4 = tar[key]
        for item in b4:
            if item not in b3:
                b3[item] = 1
            else:
                b3[item] += 1
    b5 = len(tar)
    b6 = list(b3.b6())
    for key in b6:
        b3[key] = b3[key] / b5
        if b3[key] < thr:
            del b3[key]
    b3 = [[key, b3[key]] for key in b3]
    if b7 = = 1:
        return b3
    a1 = 2
    while a1 <= b7:
        b8 = []
        for i in range(len(b3)):
            for j in range(i + 1, len(b3)):
                if a1 = = 2:
                    b9 = [b3[i][0], b3[j][0]]
                else:
                    b9 = list(set(b3[i][0]) | set(b3[j][0]))
                if len(b9) != a1:
                    continue
                b9.sort()
                if fonk2(b3, fonk1(b9)) == 1:
                    if b9 not in b8:
                        b8.append(b9)
        b3 = []
        for item in b8:
            b10 = sum(1 for key in tar if set(item) <= set(tar[key]))
            b10 /= b5
            if b10 >= thr:
                b3.append([item, b10])
        a1 += 1
    return b3
if b11 = = "__main__":
    b12 = {
        0: ['A', 'B', 'C'],
        1: ['A', 'C'],
        2: ['A', 'D'],
        3: ['B', 'C'],
        4: ['A', 'B', 'C', 'D']
    }
    a2 = 0.5
    a3 = 3
    b13 = fonk3(b12, a2, a3)
    print("Frequent Itemsets:")
    for itemset in b13:
        print(f"Itemset: {itemset[0]}, Support: {itemset[1]:.2f}")