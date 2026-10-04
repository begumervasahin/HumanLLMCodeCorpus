import sys
import math
import itertools
dim1_list = []
for i in range(len(item_list[0])):
    column = [item_list[j][i] for j in range(len(item_list))]
    dim1_list.append(column)
dim_list = [sorted(set(col)) for col in dim1_list]
partitions_list = [[] for _ in range(partitions)]
for j in range(len(item_list[0])):
    partitions_list[j % partitions].append(j)
ind_count = [len(partition) for partition in partitions_list]
list_fragmented = []
m = 0
for i in range(partitions):
    listc = []
    for j in range(ind_count[i]):
        listc.append(dim_list[m])
        m += 1
    list_fragmented.append(listc)
def listcount(listd):
    return sum(1 for p in item_list if set(listd) <= set(p))
for fragment in list_fragmented:
    combinations = []
    for j in range(len(fragment)):
        combinations += list(itertools.combinations(range(len(fragment)), j + 1))
    for combo in combinations:
        list_comb = []
        merger = []
        for index in combo:
            merger += fragment[index]
        list_comb += list(itertools.combinations(merger, len(combo)))
        for subset in list_comb:
            count = listcount(subset)
            if count != 0:
                print(' '.join(map(str, subset)) + f': {count}')
    print()