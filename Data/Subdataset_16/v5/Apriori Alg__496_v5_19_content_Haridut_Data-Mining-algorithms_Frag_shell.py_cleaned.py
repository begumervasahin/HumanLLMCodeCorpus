import itertools
a1 = 3
b1 = [
    ['a', 'b', 'c'],
    ['a', 'b', 'd'],
    ['b', 'c', 'd']
]
b2 = [[b1[j][i] for j in range(len(b1))] for i in range(len(b1[0]))]
b3 = [sorted(set(col)) for col in b2]
b4 = [[] for _ in range(a1)]
for j in range(len(b1[0])):
    b4[j % a1].append(j)
b5 = [len(partition) for partition in b4]
b6 = []
a2 = 0
for i in range(a1):
    b7 = []
    for _ in range(b5[i]):
        b7.append(b3[a2])
        a2 += 1
    b6.append(b7)
def fonk1(subset, b1):
    return sum(1 for item in b1 if set(subset) <= set(item))
for b7 in b6:
    b8 = []
    for r in range(1, len(b7) + 1):
        b8 += itertools.combinations(range(len(b7)), r)
    for combo in b8:
        b9 = []
        for a2 in combo:
            b9 += b7[a2]
        for subset in itertools.combinations(b9, len(combo)):
            b10 = fonk1(subset, b1)
            if b10 != 0:
                print(' '.join(map(str, subset)) + f': {b10}')
    print()