import sys
import math
import itertools
def read_input():
    var = sys.stdin.readlines()
    a = [i.rstrip('\n') for i in var]
    partitions = int(a[0])
    item_list = [item.split() for item in a[1:]]
    return partitions, item_list
def create_dim_list(item_list):
    dim1_list = []
    for i in range(len(item_list[0])):
        list1 = [item_list[j][i] for j in range(len(item_list))]
        dim1_list.append(list1)
    dim_list = [sorted(list(set(i))) for i in dim1_list]
    return dim_list
def create_partitions(item_list, partitions):
    lista = [[] for _ in range(partitions)]
    for j in range(len(item_list[0])):
        lista[j % partitions].append(j)
    ind_count = [len(i) for i in lista]
    return lista, ind_count
def fragment_list(dim_list, partitions, ind_count):
    m = 0
    list_fragmented = []
    for i in range(partitions):
        listc = []
        for j in range(ind_count[i]):
            listc.append(dim_list[m])
            m += 1
        list_fragmented.append(listc)
    return list_fragmented
def listcount(listd, item_list):
    l = 0
    for p in item_list:
        if set(listd) < set(p):
            l += 1
    return l
def compute_fragments(list_fragmented, item_list):
    for i in range(len(list_fragmented)):
        cf = []
        for j in range(len(list_fragmented[i])):
            for don in itertools.combinations(range(len(list_fragmented[i])), j+1):
                cf.append(list(don))
        for k in cf:
            list_comb = []
            merger = []
            for value in k:
                merger += list_fragmented[i][value]
            for h in itertools.combinations(merger, len(k)):
                list_comb.append(list(h))
            for p in list_comb:
                count = listcount(p, item_list)
                if count != 0:
                    print(" ".join(str(x) for x in p) + ': ' + str(count))
        print()
def main():
    partitions, item_list = read_input()
    dim_list = create_dim_list(item_list)
    lista, ind_count = create_partitions(item_list, partitions)
    list_fragmented = fragment_list(dim_list, partitions, ind_count)
    compute_fragments(list_fragmented, item_list)
if __name__ == "__main__":
    main()