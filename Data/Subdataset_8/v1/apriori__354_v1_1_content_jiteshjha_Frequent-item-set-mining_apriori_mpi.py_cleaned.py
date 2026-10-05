import csv
import sys
import operator
import time
from math import floor
from mpi4py import MPI
from os import getcwd, walk, system, path
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
start_time = time.time()
def find_frequent_1_itemsets(D, min_sup):
    dataset = None
    itemset = {}
    with open(D, 'r') as f:
        dataset = csv.reader(f)
        for i in dataset:
            for j in i:
                if j in itemset:
                    itemset[j.strip()] += 1
                else:
                    itemset[j.strip()] = 1
    for item in list(itemset):
        if itemset[item] < min_sup:
            del itemset[item]
    return sorted(itemset.items(), key=operator.itemgetter(0))
def powerset(s, k):
    x = len(s)
    powerset = []
    list = None
    for i in range(1, 1 << x):
        list = [s[j] for j in range(x) if (i & (1 << j))]
        if len(list) == k:
            powerset.append(list)
    return powerset
def has_frequent_subset(c, L, k):
    subsets = powerset(c, k)
    for subset in subsets:
        frequent_subset = False
        for item in L:
            if set(subset) == set(item[0].split(",")):
                frequent_subset = True
                break
        if not frequent_subset:
            return False
    return True
def apriori_gen(L, k):
    C = []
    for l1 in L:
        for l2 in L:
            first_itemlist = l1[0].split(",")
            second_itemlist = l2[0].split(",")
            i = 0
            flag = True
            while i <= k-2-1:
                if first_itemlist[i] != second_itemlist[i]:
                    flag = False
                    break
                i += 1
            if not first_itemlist[k-1-1] < second_itemlist[k-1-1]:
                flag = False
            if flag:
                c = sorted(set(first_itemlist) | set(second_itemlist))
                if has_frequent_subset(list(c), L, k-1):
                    C.append(",".join(list(c)))
    return C
def generate_association_rules(itemset, min_conf, row_count):
    if len(itemset) < 2:
        print("No association rules")
    else:
        D = str(sys.argv[1])
        print("\nMinimum Confidence Threshold: ", min_conf*100, "%\n")
        print("Association rules:\n")
        for k in range(1, len(itemset)):
            for pair in itemset[k]:
                for i in range(1, len(itemset[k][0][0].split(','))):
                    for item in powerset(pair[0].split(','), i):
                        item_sup = None
                        for j in itemset[i-1]:
                            if j[0] == ",".join(item):
                                item_sup = int(j[1])
                        if item_sup is not None and pair[1]/float(item_sup) >= min_conf:
                            print(",".join(item), "=>", ",".join(list(set(pair[0].split(',')) - set(item))), "Support: ", float("{0:.2f}".format(float(item_sup)/row_count))*100, "%", "Confidence: ", float("{0:.2f}".format(pair[1]/float(item_sup)*100)), "%")
def main(D):
    min_sup = float(sys.argv[2])
    min_conf = float(sys.argv[3])
    row_count = 0
    with open(D, 'r') as f:
        dataset = csv.reader(f)
        row_count = sum(1 for row in dataset)
    min_sup = min_sup * row_count
    min_conf = min_conf * row_count
    L1 = find_frequent_1_itemsets(D, min_sup)
    itemset = [L1]
    k = 2
    while True:
        if not itemset[k-2]:
            break
        C = apriori_gen(itemset[k-2], k)
        L = {}
        with open(D, 'r') as f:
            dataset = csv.reader(f)
            for t in dataset:
                for c in C:
                    if set(c.split(",")).issubset(set(t)):
                        if c in L:
                            L[c] += 1
                        else:
                            L[c] = 1
        for item in list(L):
            if L[item] < min_sup:
                del L[item]
        itemset.append(sorted(L.items(), key=operator.itemgetter(0)))
        k += 1
    itemset.pop()
    return itemset
if __name__ == "__main__":
    onlyfiles = []
    if rank == 0:
        system("mkdir temp")
        dataset = str(sys.argv[1])
        num_process = comm.Get_size()
        file_size = int(floor(path.getsize(dataset)/(float(1000000) * num_process)))
        system("split --bytes=" + str(file_size)+"M " + dataset + " temp/retail")
        cwd = getcwd()
        for (dirpath, dirnames, filenames) in walk(cwd+"/temp"):
            onlyfiles.extend(filenames)
            break
    dataset = comm.scatter(onlyfiles, root=0)
    itemset = main("temp/"+dataset)
    set_itemsets = comm.gather(itemset, root=0)
    if rank == 0:
        itemsetsi = []
        max_itemsets_length = max([len(itemsets) for itemsets in set_itemsets])
        for i in range(0, max_itemsets_length):
            iset = set()
            for j in range(0, num_process):
                temp_set = []
                if(i <= (len(set_itemsets[j])-1)):
                    for item in set_itemsets[j][i]:
                        temp_set.append(list(item)[0])
                    iset = iset.union(list(temp_set))
            itemsetsi.append(dict((k,0) for k in list(iset)))
        system("rm -rf temp")
        D = str(sys.argv[1])
        row_count = 0
        with open(D, 'r') as f:
            dataset = csv.reader(f)
            for t in dataset:
                for itemset in itemsetsi:
                    for item in itemset:
                        if set(item.split(",")).issubset(set(t)):
                            itemset[item] += 1
                row_count += 1
        min_sup = float(sys.argv[2])
        for itemset in itemsetsi:
            for item in list(itemset):
                if (itemset[item]/float(row_count)) < min_sup:
                    del itemset[item]
        print("\nResultant Item sets:")
        k = 1
        for itemset in itemsetsi:
            if itemset:
                print("\n", k, "-itemsets:\n")
                k += 1
                for item in itemset:
                    print(item, "| Support ", float("{0:.2f}".format(itemset[item]/float(row_count)))*100, "%")
        list_itemsets = [(sorted(itemset.items(), key=operator.itemgetter(0))) for itemset in itemsetsi if itemset]
        min_conf = float(sys.argv[3])
        generate_association_rules(list_itemsets, min_conf, row_count)
    print("\nRank : ", rank, " - Program Execution Time: ", time.time() - start_time, " seconds")