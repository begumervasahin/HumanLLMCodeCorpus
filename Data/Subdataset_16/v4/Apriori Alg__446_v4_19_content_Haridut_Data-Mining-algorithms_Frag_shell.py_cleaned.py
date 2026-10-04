import sys
import math
import itertools
b1 = []
for i in range(len(item_list[0])):
    b2 = [item_list[j][i] for j in range(len(item_list))]
    b1.append(b2)
b3 = [sorted(set(col)) for col in b1]
b4 = [[] for _ in range(partitions)]
for j in range(len(item_list[0])):
    b4[j % partitions].append(j)
b5 = [len(partition) for partition in b4]
b6 = []
a1 = 0
for i in range(partitions):
    b7 = []
    for j in range(b5[i]):
        b7.append(b3[a1])
        a1 += 1
    b6.append(b7)
def fonk1(listd):
    return sum(1 for p in item_list if set(listd) <= set(p))
for fragment in b6:
    b8 = []
    for j in range(len(fragment)):
        b8 += list(itertools.b8(range(len(fragment)), j + 1))
    for combo in b8:
        b9 = []
        b10 = []
        for index in combo:
            b10 += fragment[index]
        b9 += list(itertools.b8(b10, len(combo)))
        for subset in b9:
            b11 = fonk1(subset)
            if b11 != 0:
                print(' '.join(map(str, subset)) + f': {b11}')
    print()