import itertools
partitions = 3
item_list = [
    ['a', 'b', 'c'],
    ['a', 'b', 'd'],
    ['b', 'c', 'd']
]
dim1_list = [[item_list[j][i] for j in range(len(item_list))] for i in range(len(item_list[0]))]
dim_list = [sorted(set(col)) for col in dim1_list]
partitions_list = [[] for _ in range(partitions)]
for j in range(len(item_list[0])):
    partitions_list[j % partitions].append(j)
ind_count = [len(partition) for partition in partitions_list]
list_fragmented = []
index = 0
for i in range(partitions):
    fragment = []
    for _ in range(ind_count[i]):
        fragment.append(dim_list[index])
        index += 1
    list_fragmented.append(fragment)
def count_subset_occurrences(subset, item_list):
    return sum(1 for item in item_list if set(subset) <= set(item))
for fragment in list_fragmented:
    all_combinations = []
    for r in range(1, len(fragment) + 1):
        all_combinations += itertools.combinations(range(len(fragment)), r)
    for combo in all_combinations:
        merged = []
        for index in combo:
            merged += fragment[index]
        for subset in itertools.combinations(merged, len(combo)):
            count = count_subset_occurrences(subset, item_list)
            if count != 0:
                print(' '.join(map(str, subset)) + f': {count}')
    print()